#!/usr/bin/env python3
"""Validate one RSS feed read from stdin.

Used by .githooks/pre-commit. Reports feed XML well-formedness and pubDate
weekday correctness. Exit 0 = clean, 1 = error (with messages on stderr).

For shows listed in CITATION_REQUIRED, additionally requires every <item> to
carry a resolvable paper reference (a doi.org link) in BOTH <description> and
<itunes:summary> — clients differ in which field they show, so each must stand
alone. See podcasts/paper-overview/PROMPT.md, "Show notes".
"""
import datetime
import re
import sys
import xml.etree.ElementTree as ET

WD = {0: "Mon", 1: "Tue", 2: "Wed", 3: "Thu",
      4: "Fri", 5: "Sat", 6: "Sun"}
MONTHS = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
          "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}

# Shows whose every episode covers one specific paper, and so must cite it.
CITATION_REQUIRED = ("paper-overview",)
ITUNES = "{http://www.itunes.com/dtds/podcast-1.0.dtd}"
DOI_RE = re.compile(r"doi\.org/10\.\d{4,9}/\S+")
YEAR_RE = re.compile(r"\b(?:19|20)\d{2}\b")


def check_citations(root, label: str) -> list[str]:
    """Every <item> must cite its paper in both description and itunes:summary,
    and name the paper's publication year in its title."""
    errors = []
    for i, item in enumerate(root.iterfind(".//item"), 1):
        title = (item.findtext("title") or f"<item> #{i}").strip()
        if not YEAR_RE.search(title):
            errors.append(f"  {label}: title '{title}' has no four-digit year "
                          f"— titles must end '<Paper title> — <Journal>, "
                          f"<D Month YYYY>'")
        for field, path in (("description", "description"),
                            ("itunes:summary", f"{ITUNES}summary")):
            text = item.findtext(path)
            if text is None:
                errors.append(f"  {label}: '{title}' has no <{field}> — "
                              f"it must carry the paper citation")
            elif not DOI_RE.search(text):
                errors.append(f"  {label}: '{title}' <{field}> has no doi.org "
                              f"link — every episode must cite its paper")
    return errors


def main() -> int:
    label = sys.argv[1] if len(sys.argv) > 1 else "<stdin>"
    text = sys.stdin.read()
    errors: list[str] = []

    try:
        root = ET.fromstring(text)
    except ET.ParseError as e:
        errors.append(f"  {label}: XML parse error: {e}")
    else:
        if any(show in label for show in CITATION_REQUIRED):
            errors.extend(check_citations(root, label))

    for m in re.finditer(r"<pubDate>(\w{3}), (\d{2}) (\w{3}) (\d{4})", text):
        claimed, day, mon, year = m.group(1), int(m.group(2)), m.group(3), int(m.group(4))
        try:
            actual = WD[datetime.date(year, MONTHS[mon], day).weekday()]
        except (KeyError, ValueError) as e:
            errors.append(f"  {label}: bad pubDate '{m.group(0)}': {e}")
            continue
        if claimed != actual:
            errors.append(
                f"  {label}: pubDate '{claimed}, {day:02d} {mon} {year}' "
                f"-> weekday should be '{actual}'"
            )

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
