#!/usr/bin/env python3
"""Fetch the full text of a published paper by DOI, via Europe PMC.

Cell / Science / Nature landing pages are paywalled and bot-hostile, so
WebFetch on a doi.org URL usually returns an abstract or a block page. Nearly
every SARS-CoV-2 paper in those journals, however, was deposited in PMC with
free or open access. This resolves DOI -> PMCID -> Europe PMC full-text XML and
prints it as plain text.

Usage:
    python3 scripts/fetch_paper.py 10.1038/s41586-020-2008-3
    python3 scripts/fetch_paper.py https://doi.org/10.1126/science.abp8715

Exit codes:
    0  full text printed
    3  record found but no full text in PMC (metadata + abstract printed;
       the caller must keep claims to what the abstract supports)
    4  DOI not found in Europe PMC
"""
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

UA = {"User-Agent": "ai-nuggets/1.0 (mailto:caceves@scripps.edu)"}
REST = "https://www.ebi.ac.uk/europepmc/webservices/rest"


def get(url, timeout=60):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read()


def normalize(doi):
    doi = doi.strip()
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi)
    return doi.rstrip("/")


def lookup(doi):
    url = f"{REST}/search?" + urllib.parse.urlencode(
        {"query": f'DOI:"{doi}"', "format": "json", "resultType": "core"}
    )
    hits = json.loads(get(url))["resultList"]["result"]
    return hits[0] if hits else None


def xml_to_text(xml):
    """Crude but adequate JATS -> text: drop refs/tables, keep headings + paras."""
    xml = re.sub(r"<ref-list\b.*?</ref-list>", "", xml, flags=re.S)
    xml = re.sub(r"<table-wrap\b.*?</table-wrap>", "", xml, flags=re.S)
    xml = re.sub(r"<(front|back)\b.*?</\1>", "", xml, flags=re.S)
    xml = re.sub(r"<title[^>]*>(.*?)</title>", r"\n\n## \1\n", xml, flags=re.S)
    xml = re.sub(r"</(p|sec|abstract|caption)>", "\n\n", xml)
    xml = re.sub(r"<[^>]+>", "", xml)
    for ent, ch in (("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'), ("&#x2019;", "'")):
        xml = xml.replace(ent, ch)
    return re.sub(r"\n{3,}", "\n\n", xml).strip()


def main():
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    doi = normalize(sys.argv[1])

    rec = lookup(doi)
    if rec is None:
        print(f"ERROR: DOI not found in Europe PMC: {doi}", file=sys.stderr)
        return 4

    print(f"# {rec.get('title', '').strip()}")
    print(f"\nJournal: {rec.get('journalInfo', {}).get('journal', {}).get('title', '?')}")
    print(f"Published: {rec.get('firstPublicationDate', '?')}")
    print(f"DOI: {doi}    PMCID: {rec.get('pmcid', '-')}    PMID: {rec.get('pmid', '-')}")
    authors = rec.get("authorString", "")
    print(f"Authors: {authors}\n")

    pmcid = rec.get("pmcid")
    if pmcid:
        try:
            text = xml_to_text(get(f"{REST}/{pmcid}/fullTextXML").decode("utf-8", "replace"))
            if len(text) > 2000:
                print(text)
                return 0
            print(f"NOTE: full-text XML for {pmcid} was unexpectedly short; "
                  f"falling back to abstract.", file=sys.stderr)
        except urllib.error.HTTPError as e:
            print(f"NOTE: no full-text XML for {pmcid} ({e.code}); "
                  f"falling back to abstract.", file=sys.stderr)

    print("## Abstract (FULL TEXT UNAVAILABLE — keep all claims to what this supports)\n")
    print(re.sub(r"<[^>]+>", "", rec.get("abstractText", "(no abstract available)")))
    return 3


if __name__ == "__main__":
    sys.exit(main())
