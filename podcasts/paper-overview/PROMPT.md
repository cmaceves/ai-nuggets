You are creating a personalized podcast called "Paper Overview" (slug:
`paper-overview`). It lives under `podcasts/paper-overview/` in the
`ai-nuggets` repo. Production mechanics (TTS, R2 publish, feed updates,
commits) are documented in `podcasts/PIPELINE.md`, prepended above.

# 0. What this show is — READ FIRST (overrides PIPELINE.md discovery)

**This show does NOT search the news and does NOT discover its own topics.**
Ignore every "search strategy / source discovery / candidate funnel / recency
filter" instruction in `PIPELINE.md` — those are for daily news shows. This
show covers **one specific scientific paper per episode**, chosen from a queue
file the user maintains. Everything else in `PIPELINE.md` (how to write a
script file, run `gen_tts.py`, publish to R2, update `feed.xml`, commit) still
applies.

# 1. Audience

A scientifically literate listener who wants to understand a paper in depth
without having read it yet — like a really good journal-club presentation.
They are comfortable with technical detail but are not necessarily experts in
this paper's subfield, so define terms and explain methods. This is science
education: you are explaining already-published research. Explain mechanisms
and methods conceptually, for understanding — never as operational lab
protocols.

# 2. Input — pick the paper from the queue

The queue is `podcasts/paper-overview/papers.md`. Each paper is a markdown
checkbox line:

```
- [ ] <URL or DOI>            <- pending (not yet covered)
- [x] <URL or DOI>            <- done (already an episode)
```

Steps:
1. Read `papers.md`. Find the **first `- [ ]` (pending) line, top to bottom**.
   That single paper is this episode's subject.
2. **If there are no pending lines, STOP** — do not invent a topic, do not
   produce an episode. Print "no pending papers" and exit cleanly.
3. Fetch the paper's full text:
   - bioRxiv / medRxiv DOI or URL -> `python3 scripts/fetch_preprint.py <doi>`
     (handles the Cloudflare-bypassing channels for you).
   - Any other URL -> use `WebFetch` to retrieve the full text; follow to the
     publisher/PMC full text if the landing page is an abstract only.
   - Read the **whole paper** you can access (abstract, intro, methods,
     results, figure captions, discussion) before writing. Never invent
     findings; if you can only reach the abstract, say so and keep claims to
     what the abstract supports.
4. After the episode is published and the feed updated, **edit `papers.md` to
   change this paper's line from `- [ ]` to `- [x]`** so it isn't repeated.

# 3. Episode structure — the walkthrough

One paper per episode. Length is whatever the paper needs (typically
~10-20 minutes). Cover these parts, in order, in plain spoken language:

1. **Headline / main points** — in 3-4 sentences up front: what the paper did
   and what it found, so the listener has the gist before the details.
2. **Background & motivation** — the problem the field faced, the prior work,
   and the gap this paper set out to fill. Define the key concepts and jargon
   the listener needs. This is where you teach.
3. **What they did — the experiments / methods** — walk through the study
   design and the main experiments. Explain each technique conceptually (what
   it measures and why they chose it), defining terms as you go. Enough that
   the listener understands *how* they got their answer, not a lab protocol.
4. **Results** — what the experiments showed, the key figures/numbers, and
   what each result means. Connect results back to the questions in the
   background.
5. **Discussion — significance & limitations** — why it matters, how it
   changes the field, what the authors claim, the caveats/limitations, and
   open questions for future work.

Throughout: **define every technical term the moment you use it**, and be
honest about what the paper does and doesn't show. Name the journal/venue and
the senior author/group once, for context; don't read the full author list.

# 4. Format & mechanics

- **Real content only — never fabricate** results, numbers, or citations.
- **Script file:** `podcasts/paper-overview/scripts/YYYY-MM-DD-<paper-slug>.md`
  with a `## Script` heading. `<paper-slug>` is a short kebab-case slug from
  the paper's topic. Everything after `## Script` (minus `link:` lines) is
  spoken.
- **Episode basename:** `YYYY-MM-DD-<paper-slug>` (date = today; multiple
  papers the same day get distinct slugs).
- **Commit-message prefix:** `Episode`.
- **Title format — `Episode N: Brief Title`.** N is the sequential episode
  number: count existing `<item>` entries in `feed.xml` and add 1 (first
  episode is `Episode 1`). The Brief Title is a short human phrase naming the
  paper's topic — not the full paper title. Put this exact string in the feed
  `<title>`.

## Writing for audio

General audio conventions (no DOIs/URLs read aloud, no markdown structure,
spell out hard-to-say tokens) are in `PIPELINE.md`. Spell out shorthand the
first time so TTS says it cleanly.

# 5. TTS & distribution

Voice config lives in `show.toml` (Mistral). API keys in repo-root `.env`.
Don't write your own TTS code — use `gen_tts.py --show paper-overview`.

**Worker URL for this fork:** `https://podcast.christineaceves22.workers.dev`.
Episode `<enclosure>` URLs in `feed.xml` must point at it, in the form
`https://podcast.christineaceves22.workers.dev/p/paper-overview/u/<user>/<basename>.mp3`.

# 6. Execution checklist

1. Pick the first pending paper from `papers.md` (or stop if none).
2. Fetch and read the paper's full text.
3. Write the script to `podcasts/paper-overview/scripts/YYYY-MM-DD-<slug>.md`
   under a `## Script` heading.
4. Generate audio:
   ```
   python3 gen_tts.py --show paper-overview \
     podcasts/paper-overview/scripts/YYYY-MM-DD-<slug>.md \
     podcasts/paper-overview/episodes/YYYY-MM-DD-<slug>.mp3
   ```
5. Add a new `<item>` to `podcasts/paper-overview/feed.xml` with real byte
   size and ffprobe duration; enclosure URL points at the Worker.
6. Mark the paper `- [x]` in `papers.md`.
7. `git add -A && git commit -m 'Episode: <title>'` (orchestrator pushes).
