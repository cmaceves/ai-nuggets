# Episode 32: The math on Ebola travel screening

Paper link: https://www.medrxiv.org/content/10.64898/2026.06.11.26355442v2
Paper link: https://www.biorxiv.org/content/10.64898/2026.07.23.740427v1
Paper link: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0349857
Paper link: https://peerj.com/articles/21362/
Company link: https://www.otsuka-us.com/news
Company link: https://www.anthropic.com/news/claude-opus-5

## Script

Good morning. This is The Genome Brief for Friday, July 25th, 2026. Today we've got five items: what airport screening actually catches for the ongoing Bundibugyo Ebola outbreak — a modelling study with a number that should recalibrate expectations; a first-in-class FDA approval in ADHD, the first genuinely new drug class in that space in a long time; a preprint out of Frances Arnold's lab that uses machine learning to build enzyme libraries with expanded catalytic scope; Anthropic's new flagship model, Claude Opus five, which came out yesterday; and finally, animals — a lost lineage of giant salamander pulled out of three fossil vertebrae that sat in a Japanese museum drawer for almost thirty years.

Let's start with pathogen watch.

The item today is a medRxiv preprint that dropped on July 23rd from Billy Quilty at Charité in Berlin, working with the CMMID Bundibugyo Working Group. The question is simple: how much protection does syndromic airport screening actually give us against Bundibugyo virus disease?

Some quick context. Bundibugyo is one of the six known species of ebolavirus. It's not the classic Zaire ebolavirus behind the West African outbreak of 2013 to 2016 — it's a distinct virus, first identified in western Uganda in 2007, with a case fatality ratio that has historically run around thirty to forty percent. The reason we're talking about it now is the ongoing 2026 outbreak in the Democratic Republic of Congo and Uganda, which was declared a Public Health Emergency of International Concern earlier this year. Airport syndromic screening — thermometers, symptom questionnaires, sometimes visual inspection — is one of the standard border-control tools that gets deployed in that setting, both on the way out of affected countries and on the way in to receiving countries.

Quilty's team built a stochastic simulation model of that whole pipeline. They asked: for a hypothetical twelve-hour international flight leaving DRC or Uganda, at a screening sensitivity of eighty-six percent — which is a reasonable, if optimistic, number for these programmes — how many infected travellers slip through combined exit and entry screening?

The answer is about seventy-three percent. Roughly three out of four infected people who present for travel get through both screens undetected. And of the infected travellers who manage to board the plane at all — because some are stopped at the exit end — about ninety-two percent arrive at destination without being detected on entry.

Now the immediate question is: is that number an artefact of assumptions about asymptomatic disease? So the team also ran a deliberately conservative scenario in which every single confirmed case is assumed to be febrile — no asymptomatic-equivalent slippage at all. The undetected fraction still comes out at about sixty-four percent. It gets worse, not better, during periods of active epidemic growth, because the pool of travellers is disproportionately made up of people recently infected, still in incubation.

Why is the number this bad? It comes down to the mismatch between two timescales. The incubation period for Bundibugyo runs at about seven point seven days on average. And the time between symptom onset and severe illness is only about four days. So most infected travellers board flights while they are still pre-symptomatic and undetectable by any temperature-and-questionnaire screen. And the ones who cross into the symptomatic window progress to severe illness fast enough that they are usually too sick to travel, or get diverted before boarding. Airport screening is looking for a very narrow, transient window — mildly symptomatic but still ambulatory — and biology doesn't linger there very long.

The take-home for the audience is that you should not be reassured by the existence of airport screening. Not because it's badly run, but because the biology of Bundibugyo, and of ebolaviruses more generally, means that the incubation and onset dynamics leave almost no room for symptom-based detection to work at scale. The authors argue that meaningful protection has to come from three other things: outbreak control at source in DRC and Uganda; strengthened clinical surveillance in receiving countries with high travel connectivity to the affected region — meaning if a returning traveller shows up in an emergency department with unexplained fever, the clinical index of suspicion has to be high; and post-departure self-monitoring guidance for travellers. Airport screening is theatre; the real work is at the source and in the receiving-country clinic.

On the business side.

Yesterday, July 24th, the FDA approved Otsuka's centanafadine — brand name Simtriyo — for attention deficit hyperactivity disorder in adults and in kids age six and up, weighing at least twenty kilograms. It's a once-daily extended-release oral capsule. What makes this a story is the mechanism. Centanafadine is what's called an N-D-S-R-I, a norepinephrine-dopamine-serotonin reuptake inhibitor. That's a first-in-class pharmacology for ADHD.

Here's why that's more than a marketing label. The existing ADHD pharmacopoeia is essentially three buckets. There are the stimulants — methylphenidate and the amphetamines — which mostly increase synaptic dopamine and norepinephrine by blocking their reuptake and, in the case of amphetamines, forcing their release. Then there's atomoxetine, which is a selective norepinephrine reuptake inhibitor and the main non-stimulant option. And then there are the alpha-two adrenergic agonists like guanfacine and clonidine, which don't touch reuptake at all but modulate norepinephrine signalling in prefrontal cortex. Serotonin, notably, has been mostly absent from this list — the ADHD story has classically been a norepinephrine-and-dopamine story.

Centanafadine adds serotonin reuptake inhibition to the norepinephrine-plus-dopamine mix. That is expected to matter for the substantial fraction of ADHD patients who present with comorbid anxiety, mood symptoms, or emotional dysregulation, because serotonin reuptake inhibition is the workhorse mechanism of the SSRI class. The approval is backed by four pivotal Phase three trials — two in adults, one in adolescents, one in children — showing statistically significant improvements on the standard ADHD rating scales versus placebo. And a Phase three-b readout in adults with comorbid anxiety showed separation from placebo by the end of the first week, which is a helpful signal because SSRIs on their own typically take longer than that.

The commercial and clinical significance is real. ADHD is one of the largest neuropsychiatric drug markets, and adding a novel non-stimulant class matters clinically because stimulants aren't tolerated by everyone, have abuse liability, and don't help every phenotype. It's also a real post-Abilify growth driver for Otsuka. If you're a clinician, this is a new tool with a plausible niche in patients with comorbid anxiety or affective symptoms. If you're a scientist, it's an interesting test of whether triple monoamine reuptake actually delivers meaningfully better real-world outcomes than the existing double-monoamine story we've been running on for decades.

Now, AI in biomedicine.

There's a bioRxiv preprint from Frances Arnold's group at Caltech, posted July 24th, first author Rachael Lal, that I want to walk through carefully because it's a nice illustration of where machine-learning-plus-directed-evolution is heading.

Quick primer for anyone not steeped in this. Directed evolution is the technique that shared the 2018 Nobel Prize in Chemistry — Arnold's method for engineering enzymes by iteratively mutating a starting protein, screening the mutants for a desired activity, taking the best ones, mutating those, and so on. The catch is that you need a starting point — a parent enzyme that already shows at least some detectable level of the activity you want. If you're trying to evolve an enzyme to do a reaction that no natural enzyme does well, finding that starting point is the hard part. People typically screen large libraries of proteins, mostly get nothing, and count themselves lucky when anything above background falls out.

Arnold's group flipped the problem. Instead of hunting for a starting point for one target reaction, they took a promiscuous parent enzyme — a protein called protoglobin, which is a heme-containing enzyme that naturally handles a range of unusual chemistries — and asked whether they could use machine learning to design a single small library of variants that would be good at many different reactions at the same time.

The method is called active-learning-assisted directed evolution, or ALDE. Active learning is the flavour of supervised machine learning where the model doesn't just get trained once on a fixed dataset — it actively picks which variants to synthesise and measure next, in order to reduce its own uncertainty. You iterate: measure a small batch, retrain, pick the next batch, and so on.

They ran that loop across twenty-six carbene and nitrene transfer reactions. These are non-natural chemistries — carbenes and nitrenes are very reactive, useful-in-industrial-synthesis intermediates — and getting an enzyme to catalyse them cleanly is the kind of thing chemists really want. The results: every single one of the reactions that the parent protoglobin could already do was improved by at least one ALDE-designed variant, in either activity or selectivity. That's a nice validation of the loop. But the striking result is on the reactions the parent could not do at all. There were ten of those. The ALDE-designed library catalysed five of them.

Half of the previously inaccessible chemistries fell out of an ML-designed library built from a promiscuous starting point.

The significance, if you think about the enzyme-engineering pipeline as a whole, is that this changes the shape of what you screen. Instead of screening enormous natural libraries hoping to find a starting point for one target reaction, you can invest the ML compute up front and build a compact, purpose-designed library that covers a whole slate of chemistries in one screen. It compresses the front end of biocatalyst discovery — the slowest and often the most expensive part of the pipeline. And it's a working example of the pattern Arnold has been advocating for a while: machine learning doesn't replace the directed-evolution loop, it reshapes which library you actually build.

On the AI tool side.

Yesterday, Anthropic released Claude Opus five. This is the fourth Claude five-generation model in a couple of months — following Mythos five, Fable five, and Sonnet five — and it slots into the Opus tier, which is Anthropic's positioning for long-running agents, coding, and professional workloads.

The pricing is where the story is. Opus five sits at five dollars per million input tokens and twenty-five dollars per million output tokens — identical to Opus four point eight, but with performance that Anthropic characterises as close to Fable five's frontier intelligence at half the price. On agentic coding benchmarks like SWE-bench Pro they're reporting around seventy-nine percent, on ARC-AGI-three roughly three times the next-best model, and on the professional-work benchmark GDPval double-A version two, one thousand eight hundred sixty-one Elo. Context window stays at one million tokens, with up to one hundred twenty-eight thousand tokens of synchronous output, and there's a new five-level effort control that lets developers tune how much reasoning the model spends per request.

For working biomedical scientists, the practical read is straightforward. Opus is the tier that fits long computational-pipeline agents, literature-review agents, and code-heavy analysis workflows. A price drop of this magnitude on a frontier-class model, combined with a one-million-token context window, puts things like whole-repo code review, large multi-paper summarisation, or a multi-hour agentic run inside a normal research budget. Anthropic also flags a substantial drop in over-refusal rates from the safety classifiers, which is directly relevant to anyone whose queries touch dual-use biology, clinical topics, or public-health surveillance.

And finally, animals.

Between 1995 and 1997, three small fossil vertebrae were dug up from the Tsubusagawa Formation on Kyushu, in southern Japan. They got catalogued as belonging to Andrias, which is the living genus of Japanese giant salamander — those enormous, wonderfully weird amphibians, running up to a metre and a half long, that still hunt in fast-flowing rivers. And then the fossils sat in a drawer for about thirty years.

This week, in PeerJ, Masahiro Noda and colleagues at Kyoto University pulled those three vertebrae back out, ran them through micro-CT scanning and geometric morphometrics — basically quantitative shape comparison — and concluded that they had been misclassified the whole time. The combination of traits doesn't match any known genus. They erected a new one: Limnospondylus ajimuensis. From three vertebrae, a lost lineage.

Two things make this delightful beyond the base level of "new giant salamander." The first is the ecology. Modern giant salamanders live in fast-flowing rivers — that's the ecological niche the family occupies today. Limnospondylus, judging from the sediments it was preserved in, lived in freshwater lakes. So this is direct evidence that the family Cryptobranchidae used to occupy a broader range of habitats than it does now; the lake-dwelling lineages went extinct, most likely around the Pliocene-to-Pleistocene climate cooling, and only the river-adapted lineages survived. Today's Japanese giant salamander is a survivor of what used to be a more ecologically diverse family.

The second thing is the amount of information those three little bones actually contained. It's a good reminder that a lot of paleontological "new discoveries" are actually old fossils, sitting in museum drawers, waiting for someone to look at them again with better tools. The specimens were collected in the nineties. What's new is the CT scanner, the morphometric software, and the willingness to look.

That's the show for Friday, July 25th. Thanks for listening.
