# Episode 9: Mpox doubles up in eastern Congo

Paper link: https://www.medrxiv.org/content/10.64898/2026.06.25.26356562v2
Paper link: https://www.biorxiv.org/content/10.64898/2026.06.29.735386v1
Paper link: https://www.anthropic.com/news/claude-sonnet-5
Paper link: https://www.tipranks.com/news/company-announcements/theravance-biopharma-to-be-acquired-by-zymeworks
Paper link: https://www.sciencenews.org/article/octopus-hunt-crabs-with-mirror

## Script

Good morning and welcome to The Genome Brief for Tuesday, July first, 2026. Five stories today.

A new preprint from the Democratic Republic of Congo and the Netherlands documents something that complicates the mpox outbreak: both of the virus's major circulating lineages are now confirmed co-circulating in the same part of eastern DRC, with implications for how the outbreak is tracked, diagnosed, and responded to. On the business side, a Canadian biotech best known for cancer drugs paid nearly a billion dollars to add a COPD therapy to its portfolio — and the reasoning tells you something about where oncology companies see their next funding problem. In the AI space, a new benchmark puts a number on exactly where today's best models fall short on real genomics reasoning tasks. Anthropic released a new model yesterday that aims to close that gap for agentic work. And we close with an octopus, a mirror, and a crab.

---

Pathogen watch.

To understand why today's preprint matters, you need a little background on how mpox has been categorized.

Mpox is caused by monkeypox virus, which belongs to the same genus as smallpox — Orthopoxvirus. The virus comes in two major lineages, called Clade I and Clade II. Clades are just evolutionary lineages — groups of viruses that share a common ancestor and a set of defining mutations. Clade II is the lineage behind the 2022 global outbreak, which spread primarily through sexual contact networks and was brought under control with vaccines and behavioral interventions. Clade I is the Central African lineage, endemic in the DRC for decades, historically associated with animal-to-human transmission, with rodents serving as the main reservoir.

But in 2023, something shifted inside Clade I. A sub-lineage, now called Clade Ib, began spreading in eastern DRC — specifically in South Kivu province — in a pattern that looked very different from historical Clade I behavior. It was spreading efficiently between people, through close contact including sexual networks, without the same dependence on animal spillover that characterized classic Clade I outbreaks. It spread across borders into Uganda, Rwanda, Burundi, and Kenya, and then further. In August 2024, the World Health Organization declared Clade Ib a public health emergency of international concern — only the second mpox PHEIC in history. That emergency remains active today.

Meanwhile, Clade Ia — the older endemic sub-lineage — has continued to circulate in the DRC alongside it. These aren't two separate events in separate places. They're two viruses running in parallel in overlapping territory. And South Kivu, where Clade Ib first emerged, has always been the most concerning corner of the map precisely because that's where both are present.

A preprint posted on medRxiv Sunday and revised Monday, from a team at the DRC Institute of Epidemiology and Biomedical Research in partnership with Erasmus Medical Center in Rotterdam and collaborators in Denmark, now documents this systematically. I'm working from a limited abstract here — the full text wasn't retrievable at time of recording — but the title is explicit: the paper covers January through May of 2026 and confirms both the emergence and co-circulation of Clade Ia and Clade Ib in South Kivu simultaneously.

Why does that co-circulation matter, and what does it actually change?

The first reason is diagnostic and operational. Mpox from Clade Ia and Clade Ib looks clinically very similar at presentation — fever, a characteristic skin rash, often swollen lymph nodes. Distinguishing the two clades requires genome sequencing. If surveillance teams in the field are testing samples for mpox without routinely sequencing, they can detect that an outbreak is happening but they can't tell which clade is driving it. And that distinction is not academic — it has direct implications for the intervention. Clade Ia outbreaks historically have required control strategies focused on the animal-to-human interface: identifying the animal source, protecting hunters and people with occupational wildlife exposure, vaccinating around the spillover event. Clade Ib requires a different intervention layer, one that addresses human-to-human transmission through close and sexual contact networks — different outreach, different partner notification protocols, different vaccination targeting. If you're responding to a cluster in South Kivu without knowing which clade you're dealing with, you may be running the wrong playbook, or an incomplete one.

The second reason is scientific and longer-horizon. When two related viruses circulate in overlapping host populations — in this case people — there is potential for co-infection of single cells, which can occasionally produce hybrid progeny through recombination. Poxvirus recombination is documented in other members of the family, and it can produce progeny with properties from both parents. This is not an imminent alarm — it's not what this paper is reporting. But a preprint that places both Clade Ia and Clade Ib in the same region during the same five-month window is precisely the kind of surveillance documentation you need before you can ask questions about co-infection dynamics rigorously. The Erasmus team has led European mpox sequencing since the 2022 outbreak, which lends weight to the genomic classification in this work.

This is a preprint and peer review may refine some of the case counts and classification specifics. But the factual core — co-circulation of both Clade I sub-lineages confirmed in South Kivu through early 2026 — is an important reference point for anyone working on the mpox response.

---

On the business side, a deal announced Monday morning: Zymeworks, a Canadian biopharmaceutical company, has agreed to acquire Theravance Biopharma in an all-cash deal valuing the company at approximately nine hundred twenty-nine million dollars, or seventeen dollars per share.

The asset at the center of this transaction is a drug called YUPELRI — generic name revefenacin — which occupies a specific niche in the treatment of chronic obstructive pulmonary disease, or COPD. COPD is a progressive lung condition, primarily caused by smoking, in which airways narrow and trap air, making every breath harder than the last. It's the third leading cause of death globally.

The standard maintenance pharmacology for COPD includes two main drug classes. Long-acting beta-agonists relax airway muscle by stimulating one receptor type. Long-acting muscarinic antagonists — LAMAs for short — relax the same muscle by blocking a different receptor type, the muscarinic receptor. Most LAMAs on the market, including tiotropium and glycopyrrolate, are delivered by handheld inhalers, which require the patient to time a strong inhalation with activating the device. In older patients or those with advanced disease, that coordination is genuinely difficult. Nebulizers — devices that aerosolize liquid medicine into a fine mist that patients breathe passively over about ten minutes — have no coordination requirement. YUPELRI is the only long-acting muscarinic antagonist approved for nebulizer delivery. It generates roughly sixty million dollars a year in operating cash flow.

What Zymeworks is really buying is two things: a profitable respiratory drug to fund its oncology pipeline without needing fresh equity, and an entry into a disease area with durable revenue. The company has built out a bispecific antibody platform in cancer in recent years — bispecific antibodies are engineered proteins designed to bind two different targets at once, allowing them to do things a conventional single-target antibody can't. Those programs are approaching expensive late-stage trials. Theravance's cash flow helps bridge the gap. The acquisition is financed with a note secured solely against YUPELRI's royalty stream, a structure that keeps the oncology pipeline assets off the collateral table.

---

Now, AI in the biomedical sciences.

A preprint posted on bioRxiv this week introduces GeneBench-Pro, an updated benchmark designed to test whether today's AI agents can actually perform the multi-step statistical reasoning that computational biologists and bioinformaticians do in their day-to-day work. The answer, based on testing today's best models, is: not reliably — and the paper is usefully specific about why.

The benchmark consists of one hundred twenty-nine problems spanning genomics, population genetics, survival analysis, clinical biomarker work, and related domains, each reviewed by external domain experts before inclusion. What makes it different from most biology benchmarks is that the problems are not factual lookups or single-step tasks. Each one requires the agent to navigate multiple decision points in sequence, where an incorrect early choice — the wrong statistical estimator, a missed data diagnostic, the wrong model for the data type — produces a wrong final answer even if all subsequent steps are executed correctly. The goal is to simulate what it looks like when a skilled bioinformatician runs a real analysis: not just knowing that a method exists, but knowing when to use it, catching when the data violates its assumptions, and reading the output correctly in context.

On the full problem set, the best-performing model — GPT 5.6 Sol Pro — reached a pass rate of thirty-one point five percent. Claude Opus 4.8, the strongest non-OpenAI model tested, reached sixteen percent. GPT 5.5 reached twelve percent. These numbers represent meaningful improvement over a few prior model generations, but the absolute performance is clearly below what a trained bioinformatician would achieve on the same problems.

The authors put a name on the dominant failure mode: they call it a gap between noticing and acting. Models would often correctly identify a warning sign in the data — a diagnostic signal suggesting the current analysis path was wrong — but then fail to change course. They'd spot the indicator and keep going in the original direction anyway. This is worth distinguishing from hallucination. Hallucination is generating false information. This is a coherence failure: correctly perceiving a local signal and failing to propagate its consequence to the downstream decision. It's a more subtle and arguably more dangerous kind of error in autonomous scientific work, because the output looks locally reasonable even when it's globally wrong.

For researchers currently thinking about how much to trust an AI agent running a genomics or bioinformatics workflow with any degree of autonomy: a thirty-one percent end-to-end pass rate on expert-reviewed realistic problems is a useful calibration. Not a reason to put the tools away, but a clear signal that verification checkpoints at the consequential decision nodes matter.

---

Speaking of agentic AI, Anthropic released Claude Sonnet 5 yesterday, a new model designed specifically for the kind of work GeneBench-Pro is evaluating — multi-step tasks where an AI plans, uses external tools, executes code, and carries a workflow through to completion with minimal human interruption.

Anthropic's model lineup has historically divided into a flagship called Opus, for the hardest problems, and a midsize model called Sonnet for day-to-day work. Sonnet 5 meaningfully blurs that line. On certain knowledge-work benchmarks, it matches or slightly outperforms Opus 4.8 while costing considerably less. On an agentic coding benchmark — a reasonable proxy for general complex task completion — Sonnet 5 scores sixty-three point two percent, compared to Opus 4.8's sixty-nine percent and the previous Sonnet 4.6's fifty-eight percent. Early users testing it on multi-step workflows describe it as finishing complex tasks that previous Sonnet models would stall partway through, and checking its own outputs without being prompted.

The model also shows lower rates of hallucination and improved resistance to prompt injection — that's the attack type where malicious instructions embedded in a document or data file can redirect an AI's behavior during an automated workflow. That safety improvement matters if you're running agents on clinical data or research files you haven't authored yourself. At introductory pricing of two dollars per million input tokens through August, it makes capable agentic workflows accessible at lower running cost than flagship rates.

---

And finally, animals.

Octopuses are already famous for problem-solving, but a paper published this month in Current Biology adds a new one to the list. Octopus bimaculoides — the California two-spot octopus — can learn to use a mirror to locate food that's hidden from direct view.

Here's the setup: researchers fitted a tank with a mirror at one end and placed a crab behind a corner partition, where it was visible only as a reflection in the mirror. To reach the crab, an octopus couldn't just approach the mirror — it had to understand that the image it was seeing corresponded to an object located elsewhere in the tank, and then navigate around the partition to that actual location. After about ten to twelve training trials, all three octopuses in the study learned the task. On test trials, they chose the correct side roughly seventy-three percent of the time, and in more than half of their successful trials they climbed directly over the side walls of the chamber rather than going around — suggesting they'd formed a spatial model of where the crab actually was, not just a conditioned response to the reflection.

This is the first time any invertebrate — any animal without a backbone — has been shown to use a mirror as a navigational tool to locate prey. Mirror-based spatial reasoning had previously been documented in primates and some birds. What the study adds to the growing picture of octopus cognition is the idea that they can hold spatially abstract representations of their environment: they don't just see an image in a mirror, they compute what it implies about a location they cannot see. For an animal with a nervous system that evolved entirely independently from vertebrates, that's a remarkable inference. Everything about an octopus mind is built differently — and yet here it is, doing spatial geometry.

That's The Genome Brief for Tuesday, July first, 2026. See you tomorrow.
