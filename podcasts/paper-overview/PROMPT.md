You are creating a podcast called "SARS-CoV-2: A History Run-Through" (slug:
`paper-overview` — the slug is historical, don't rename it; feed and episode
URLs depend on it). It lives under `podcasts/paper-overview/` in the
`ai-nuggets` repo. Production mechanics (TTS, R2 publish, feed updates,
commits) are documented in `podcasts/PIPELINE.md`, prepended above.

# 0. What this show is — READ FIRST (overrides PIPELINE.md discovery)

**This show does NOT search the news and does NOT discover its own topics.**
Ignore every "search strategy / source discovery / candidate funnel / recency
filter" instruction in `PIPELINE.md` — those are for daily news shows, and
their bias toward *recent* material is exactly backwards here.

This show walks through the SARS-CoV-2 literature **in historical order**,
from the first 2020 papers to the present day. One paper per episode, taken
from a fixed queue in publication order. Every paper is from *Cell*, *Science*,
or a Nature-family journal, is entirely about SARS-CoV-2, and the queue leans
heavily toward genomics.

The chronology is the point. A listener going through the feed in order should
experience the pandemic the way the field did: not knowing yet what the next
variant would do, watching the tools get built, watching ideas get revised.
**Never skip ahead in the queue**, and never let a later paper's knowledge leak
backwards into an earlier episode (see §3).

New episodes publish Monday, Wednesday, and Friday.

# 1. Audience

A scientifically literate listener who wants to understand a paper in depth
without having read it — like a really good journal-club presentation. They
are comfortable with technical detail but are not necessarily experts in this
paper's subfield, so define terms and explain methods. This is science
education: you are explaining already-published research. Explain mechanisms
and methods conceptually, for understanding — never as operational lab
protocols.

# 2. Input — take the next paper from the queue

The queue is `podcasts/paper-overview/papers.md`, ordered by publication date.
Each paper is a markdown checkbox line:

```
- [ ] <URL or DOI>  <!-- YYYY-MM-DD | Journal | Title -->   <- pending
- [x] <URL or DOI>  <!-- YYYY-MM-DD | Journal | Title -->   <- already an episode
```

Steps:

1. Read `papers.md`. Take the **first `- [ ]` (pending) line, top to bottom**.
   That single paper is this episode's subject. It is the oldest uncovered
   paper, and that is deliberate — **do not** scan down for a more interesting
   one.
2. **If there are no pending lines, STOP.** Do not invent a topic, do not reach
   for a paper outside the queue, do not produce an episode. Print
   `no pending papers — queue is empty, top up papers.md` and exit cleanly.
   (Note: `scripts/run_all_shows.sh` treats "no mp3 produced today" as a soft
   failure and will retry on a model ladder for ~20 minutes before giving up.
   That is harmless noise in the empty-queue case, but it's the signal to add
   more papers — see the inclusion rules at the top of `papers.md`.)
3. Fetch the paper's full text. These journals are paywalled and bot-hostile,
   so go through PMC rather than the publisher:
   - **First:** `python3 scripts/fetch_paper.py <DOI or doi.org URL>`. Exit 0
     means you have the full text. **Exit 3 means full text was unavailable and
     you only have the abstract** — try the next two fallbacks before accepting
     that.
   - **Fallback:** `WebFetch` the PMC article page the script printed as
     `PMCID`, i.e. `https://www.ncbi.nlm.nih.gov/pmc/articles/<PMCID>/`.
   - **Fallback:** `WebFetch` the doi.org URL itself and follow to the
     publisher full text.
   - Read the **whole paper** you can access (abstract, intro, methods,
     results, figure captions, discussion) before writing. Never invent
     findings. If you could only reach the abstract, say so on-air in one
     sentence and keep every claim to what the abstract supports.
4. After the episode is published and the feed updated, **edit `papers.md` to
   change this paper's line from `- [ ]` to `- [x]`** so it isn't repeated.
   Leave the trailing `<!-- ... -->` comment intact.

# 3. Episode structure — the walkthrough

One paper per episode. Length is whatever the paper needs (typically
~10-20 minutes). Cover these parts, in order, in plain spoken language:

1. **Where we are in the story** — 2-3 sentences placing this paper in the
   timeline. Name the publication date and what the pandemic looked like at
   that moment. This is the spine of the show; it opens every episode.
2. **Headline / main points** — in 3-4 sentences: what the paper did and what
   it found, so the listener has the gist before the details.
3. **Background & motivation** — the problem the field faced *at the time*,
   the prior work, and the gap this paper set out to fill. Define the key
   concepts and jargon the listener needs. This is where you teach.
4. **What they did — the experiments / methods** — walk through the study
   design and the main experiments. Explain each technique conceptually (what
   it measures and why they chose it), defining terms as you go. For the
   genomics papers, that means actually explaining the sequencing approach,
   the phylogenetic or population-genetic method, and what its assumptions
   are — not just naming the tool. Enough that the listener understands *how*
   they got their answer, not a lab protocol.
5. **Results** — what the experiments showed, the key figures/numbers, and
   what each result means. Connect results back to the questions in §3.3.
6. **Discussion — significance & limitations** — why it mattered, how it
   changed the field, what the authors claimed, the caveats, and the open
   questions they named.
7. **What happened next — optional, max ~45 seconds.** Only if it genuinely
   helps: a brief, clearly-flagged note on how this held up. Mark it
   explicitly ("stepping outside the paper for a moment") so it never blurs
   into what the authors actually showed.

**Honour the contemporaneous view.** Outside of §3.7, write the episode from
the standpoint of what was known when the paper was published. Do not
retroactively grade the authors with information from later papers, and do not
mention variants or findings that didn't exist yet. If a paper was later
revised or contradicted, §3.7 is where that goes.

Throughout: **define every technical term the moment you use it**, and be
honest about what the paper does and doesn't show. Name the journal, the
publication date, and the senior author/group once, for context; don't read the
full author list.

# 4. Format & mechanics

- **Real content only — never fabricate** results, numbers, or citations.
- **Script file:** `podcasts/paper-overview/scripts/YYYY-MM-DD-<paper-slug>.md`
  with a `## Script` heading. `<paper-slug>` is a short kebab-case slug from
  the paper's topic. Everything after `## Script` (minus `link:` lines) is
  spoken.
- **Episode basename:** `YYYY-MM-DD-<paper-slug>` — the date is **today's
  production date**, not the paper's publication date.
- **Commit-message prefix:** `Episode`.
- **Title format — `Episode N: <Full paper title> — <Journal>, <D Month YYYY>`.**

  Example:

  ```
  Episode 1: A new coronavirus associated with human respiratory disease in China — Nature, 3 February 2020
  ```

  - `N` is the sequential episode number: count existing `<item>` entries in
    `feed.xml` and add 1 (the feed starts empty, so the first episode is
    `Episode 1`).
  - **Use the paper's full official title, verbatim**, exactly as
    `scripts/fetch_paper.py` prints it — not a paraphrase and not a shortened
    topic phrase. Some of these titles are long; that is fine and expected.
    The only permitted edits are dropping a trailing period and fixing
    SHOUTED or all-lowercase journal styling.
  - The date is the paper's **publication** date, not the production date, and
    it is what makes the chronology readable in a podcast client. Write it as
    `3 February 2020` — day, full month name, year.
  - Use an em dash (`—`) before the journal, so the title splits cleanly at a
    predictable point when a client truncates it.

  Put this exact string in the feed `<title>`. The pre-commit hook checks that
  every title in this show's feed carries a four-digit year.

## Show notes — the paper reference is MANDATORY

Every episode must carry a full, resolvable reference to the paper it covers.
A listener should never have to guess which paper they just heard about. This
is not optional and there is no episode for which it doesn't apply.

Build the citation once, in this exact form:

```
<First author surname> et al., "<Full paper title>." <Journal>, <D Month YYYY>. https://doi.org/<doi>
```

Use the paper's **publication** date, and the full official title — not the
short Brief Title from the episode title. For a paper with one or two authors,
name them both instead of `et al.`. Take the authors, title, journal, and date
from the header `scripts/fetch_paper.py` prints, so they match the record.

That citation then goes in three places:

1. **The script file** — as a `Paper link:` line immediately under the
   `## Script` heading. `gen_tts.py` strips `Paper link:` lines before TTS
   (see `podcasts/PIPELINE.md`), so this is recorded without being read aloud.
2. **The feed `<description>`** — as the *first line*, followed by a blank
   line, then the prose summary.
3. **The feed `<itunes:summary>`** — append the same citation as the *last*
   line. Podcast clients differ in which of the two fields they display, so
   both must stand alone.

Escape the citation for XML like any other feed text: a literal `&` in a title
becomes `&amp;`. The `<` and `>` characters do not appear in a DOI, but if a
title contains them they must be escaped too.

The pre-commit hook (`.githooks/check-feed.py`) enforces this: it fails the
commit if any `<item>` in this show's `feed.xml` lacks a `doi.org` link in both
its `<description>` and its `<itunes:summary>`.

Spoken-word counterpart: the script itself should still *say* the journal,
publication date, and senior author once (§3), since the listener can't see the
show notes while listening. Never read the DOI aloud.

## Writing for audio

General audio conventions (no DOIs/URLs read aloud, no markdown structure,
spell out hard-to-say tokens) are in `PIPELINE.md`. Spell out shorthand the
first time so TTS says it cleanly — "B.1.1.7" as "B-one-one-seven", "D614G" as
"D-six-one-four-G", "RBD" as "receptor binding domain" on first use.

# 5. TTS & distribution

Voice config lives in `show.toml` (Mistral). API keys in repo-root `.env`.
Don't write your own TTS code — use `gen_tts.py --show paper-overview`.

**Worker URL for this fork:** `https://podcast.christineaceves22.workers.dev`.
Episode `<enclosure>` URLs in `feed.xml` must point at it, in the form
`https://podcast.christineaceves22.workers.dev/p/paper-overview/u/<user>/<basename>.mp3`.

# 6. Execution checklist

1. Take the first pending paper from `papers.md` (or stop if none).
2. Fetch and read its full text via `scripts/fetch_paper.py`.
3. Write the script to `podcasts/paper-overview/scripts/YYYY-MM-DD-<slug>.md`
   under a `## Script` heading.
4. Generate audio:
   ```
   python3 gen_tts.py --show paper-overview \
     podcasts/paper-overview/scripts/YYYY-MM-DD-<slug>.md \
     podcasts/paper-overview/episodes/YYYY-MM-DD-<slug>.mp3
   ```
5. Publish the mp3: `scripts/publish_episode.sh paper-overview YYYY-MM-DD-<slug>`
6. Add a new `<item>` to `podcasts/paper-overview/feed.xml` with real byte
   size and ffprobe duration; enclosure URL points at the Worker.
7. Mark the paper `- [x]` in `papers.md`.
8. `git add -A && git commit -m 'Episode: <title>'` (orchestrator pushes).
