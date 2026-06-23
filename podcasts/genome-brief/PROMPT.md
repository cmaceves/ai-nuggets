You are creating a personalized podcast called "The Genome Brief" (slug:
`genome-brief`). It lives under `podcasts/genome-brief/` in the `ai-nuggets`
repo. Production mechanics (TTS, R2 publish, feed updates, commits) are
documented in `podcasts/PIPELINE.md`, prepended above.

# 1. Audience

A working biomedical scientist who listens each morning to genuinely
*understand* the day's developments — not just hear headlines. Cares about
pathogen genomics and surveillance, the biotech/pharma business landscape, and
how AI is changing biomedical research — and likes to end on something fun.
Comfortable with technical detail but is not a specialist in every subfield,
so wants each story actually explained (concepts, mechanisms, significance).
Prefers depth and clear explanation over speed; does not want hype or fluff.

## What they like

- **Viral clinical & wastewater genomics**: surveillance, lineage/variant
  evolution, and clinical genomics for SARS-CoV-2, H5N1 (avian influenza),
  RSV, malaria (*Plasmodium*), and tuberculosis (*M. tuberculosis*). New
  variants, drug-resistance mutations, wastewater signal trends, and notable
  sequencing/surveillance methods all count.
- **Biotech & pharma business news**: funding rounds, IPOs, M&A, clinical
  trial readouts, FDA/EMA approvals and rejections, major partnerships.
- **AI in the biomedical sciences**: agentic AI, foundation models for
  biology/chemistry, AI for drug discovery, genomics, and diagnostics.
- **Major AI tool & platform updates**: notable model releases, capability
  jumps, and developer-platform changes from the major AI labs — only when
  genuinely significant, not incremental version bumps.
- **Fun animal news**: one light, true, delightful animal story to close
  every episode. Global, surprising, science-flavored when possible.

## What to avoid

- Hype, breathless tone, and unverified claims.
- Incremental product noise (minor version bumps, routine pricing tweaks).
- Stale items — see the hard recency filter below.

## Past feedback

- (none yet — will update based on feedback)

# 2. Search strategy

Cast a wide net across the source types below — don't voluntarily skip any.
The best nugget might come from any of them. If one source fails transiently
(bioRxiv 5xx, arXiv 429, etc.) follow the source-level-failures rule in
`PIPELINE.md` — proceed with the rest, note the gap, ship the episode.

1. **Pathogen genomics & surveillance** (last 2–3 days):
   - **bioRxiv / medRxiv** via the details API:
     `curl 'https://api.biorxiv.org/details/biorxiv/YYYY-MM-DD/YYYY-MM-DD'`
     (and the `medrxiv` server) for yesterday and today. Pull the FULL
     collection, paginating via `cursor` if `messages[0].count` exceeds the
     page size. Filter title+abstract for: "SARS-CoV-2", "wastewater",
     "H5N1", "avian influenza", "RSV", "malaria", "Plasmodium",
     "tuberculosis", "M. tuberculosis", "lineage", "variant", "genomic
     surveillance", "drug resistance".
   - **PubMed** (last 5 days; indexing lags). Prefer the PubMed MCP
     (`mcp__claude_ai_PubMed__search_articles`); otherwise NCBI E-utilities
     term-filtered server-side. Same pathogen keyword set.
   - **Public-health surveillance pages** as candidates: CDC respiratory
     virus / wastewater pages, WHO disease outbreak news
     (https://www.who.int/emergencies/disease-outbreak-news), and ECDC.
     A new outbreak report or variant designation is a first-rate item.
2. **Biotech & pharma business news** (last 1–2 days): headlines from
   science/biotech business outlets (Endpoints, STAT, Fierce Biotech,
   BioPharma Dive) and primary FDA/EMA pages. Funding, M&A, trial readouts,
   approvals.
3. **AI in biomedicine** (last 2 days): bioRxiv/arXiv (cs.AI, cs.LG, q-bio)
   and science-news coverage of foundation models, agentic AI, and AI for
   drug discovery / genomics / diagnostics. If a shared arXiv day-cache
   exists at `/tmp/ai-nuggets-arxiv-cache.xml`, read it first (see
   `PIPELINE.md`); respect arXiv's 1-request-per-3-seconds limit.
4. **Major AI tool/platform updates** (last 1–2 days): notable releases from
   the major AI labs and developer platforms. Significant only — capability
   jumps, new model families, major API/agent features. Skip minor bumps.
5. **Fun animal news** (last few days): one true, delightful animal story
   from reputable outlets worldwide. Always include one as the closer.

**Recency is a hard filter, not a hint.** Items outside the stated windows
are out-of-scope regardless of merit. If a segment has nothing fresh, say so
briefly and move on — a short episode beats a padded one.

# 3. Episode format

**This is an explainer show, not a headline reader.** The listener is smart
but is NOT a specialist in every topic — they want to actually *understand*
each story, not just hear that it happened. Depth beats breadth. Length is
not capped: take the time each item needs (a typical episode runs ~8–15
minutes). It is better to cover **fewer items in real depth** than to skim
many. Aim for the best **3–5 items** total across the segments below.

- Structure: a brief cold open that says what's in today's episode, then
  segments in this order — **Pathogen watch → Biotech & pharma → AI in
  biomedicine → AI tools → And finally, animals.** Drop any segment with
  nothing genuinely fresh rather than padding it. The animal closer stays.
- **For every item, explain it — don't just report it.** Walk through, in
  plain language:
  1. **Context** — what the thing *is* and the background needed to follow it.
  2. **The finding/news** — what actually happened or was shown.
  3. **The mechanism / the "how"** — *define every technical term you use* and
     explain the underlying biology, chemistry, or method. Assume the listener
     has not heard the jargon before.
  4. **Why it matters** — the implication, who it affects, what changes.
- **Define jargon the moment you use it.** Never let a technical term go by
  unexplained. For example, if a study is about "saltational" evolution in
  SARS-CoV-2, explain that *saltation* means the virus accumulated a large
  batch of mutations all at once (a sudden jump) rather than one-at-a-time
  drift, that these jumps are thought to happen inside long-term infections in
  immunocompromised people, and that this matters because such leaps are how
  surprise variants like Omicron seem to appear — then connect it back to the
  finding. Hold every item to that standard: a curious non-expert should come
  away understanding *what it means and why it's important*.
- Be opinionated about significance, but ground claims in the source.
- **Real, verified URLs only — never fabricate.** If you can't find the
  primary source for an item, drop it.
- **Script file:** `podcasts/genome-brief/scripts/YYYY-MM-DD-<slug>.md` with a
  `## Script` heading. Everything after that heading (minus `link:` lines) is
  what gets spoken.
- **Episode basename:** `YYYY-MM-DD-<slug>`.
- **Commit-message prefix:** `Episode`.
- **Title format — `Episode N: Brief Title`.** N is the sequential episode
  number: count the existing `<item>` entries in `feed.xml` and add 1 (so the
  first episode after a reset is `Episode 1`). The Brief Title is a short,
  human phrase naming the day's lead story or theme — keep it tight, not a
  list of every segment. Example: `Episode 1: How surprise COVID variants are
  born`. Put this exact `Episode N: Brief Title` string in the feed `<title>`.

## Writing for audio

General audio conventions (no DOIs/URLs, no markdown structure, spell out
hard-to-say tokens) are in `PIPELINE.md`. Show-specific rules:

- **Don't list authors.** Name the corresponding author or lab only when it
  anchors the work to prior work the audience knows; otherwise the group
  affiliation alone is fine.
- **Spell out pathogen shorthand the first time** so TTS says it cleanly:
  "H5N1" → "H five N one"; "SARS-CoV-2" → "SARS cov two"; "RSV" and "TB" are
  fine spoken as letters.
- Keep transitions between segments crisp ("On the business side…",
  "And finally, animals…").

# 4. TTS & distribution

Voice config lives in `show.toml`. API keys in repo-root `.env`. Don't write
your own TTS code — use `gen_tts.py --show genome-brief`.

**Worker URL for this fork:** `https://podcast.christineaceves22.workers.dev`.
Episode `<enclosure>` URLs in `feed.xml` must point at it, in the form
`https://podcast.christineaceves22.workers.dev/p/genome-brief/u/<user>/<basename>.mp3`.

# 5. Daily execution

1. Write script to `podcasts/genome-brief/scripts/YYYY-MM-DD-slug.md` with a
   `## Script` heading.
2. Generate audio:
   ```
   python3 gen_tts.py --show genome-brief \
     podcasts/genome-brief/scripts/YYYY-MM-DD-slug.md \
     podcasts/genome-brief/episodes/YYYY-MM-DD-slug.mp3
   ```
3. Add a new `<item>` to `podcasts/genome-brief/feed.xml` with real byte size
   and ffprobe duration. Enclosure URLs point at the Worker.
4. `git add -A && git commit -m 'Episode: <title>' && git push`
