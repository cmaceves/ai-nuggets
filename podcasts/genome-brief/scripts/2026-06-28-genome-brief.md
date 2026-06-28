# Episode 6: Surveillance goes airborne

Paper link: https://www.medrxiv.org/content/10.64898/2026.06.23.26354644v1
Paper link: https://www.fiercebiotech.com/biotech/moderna-enters-vivo-car-t-granting-autoimmune-asset-007-license-kill-pathogenic-cells
Paper link: https://arxiv.org/abs/2606.26179
Paper link: https://www.sciencedaily.com/releases/2026/06/260621052722.htm

## Script

Good morning. Today we have four stories.

First: researchers have demonstrated that the GeneXpert, a point-of-care PCR device already deployed in thousands of hospitals and clinics worldwide, can detect SARS cov two and influenza A directly from air samples — a step toward turning every clinical site into a surveillance node.

On the business side: Moderna announced an in vivo CAR-T program for autoimmune disease — a strategy that would let patients receive the benefits of cell therapy through an injection rather than through the weeks-long process of engineering their own cells in a laboratory.

Then: a new AI framework predicts antibiotic resistance in tuberculosis from whole-genome sequence data and, unlike most machine-learning approaches, actually explains its reasoning — by combining a neural network with the WHO's curated map of resistance mutations.

And finally: a juvenile great white shark netted by Spanish fishermen in the Mediterranean has reignited a 160-year debate about whether a ghost population of these sharks has been quietly breeding there the entire time.

Let's get into it.

---

Pathogen watch.

Most people are familiar with two modes of respiratory pathogen surveillance. One is clinical testing: a sick person presents at a healthcare facility, gets a nasal swab, and the result tells you that individual is infected. The other is wastewater surveillance: sampling the aggregate sewage output of a community to catch the molecular traces of circulating viruses before they produce a wave of illness. Both are valuable, but they track different things — individual clinical events on one end, population-level signal on the other.

What is much less developed is the middle ground: ambient air surveillance in healthcare settings. The air inside hospitals, schools, nursing homes, and transit hubs carries aerosols produced by infected people, and in principle, sampling that air could detect active circulation of respiratory pathogens at a specific location before a clinical outbreak becomes apparent. The problem has been logistics. Standard air surveillance requires collecting aerosols onto a substrate, then sending that substrate to a centralized laboratory for RT-qPCR — that is, real-time quantitative PCR, the gold-standard molecular amplification technique that detects viral genetic material. The roundtrip means delays of hours to days, and reliance on laboratory infrastructure that many facilities lack.

A preprint posted to medRxiv this week from a team at the University of Wisconsin-Madison and the University of Missouri asked whether there was a simpler path. They paired a commercially available air sampler — the ThermoFisher AerosolSense — with the Cepheid GeneXpert system, using the Xpert Xpress SARS cov two, flu, and RSV Plus cartridge.

The GeneXpert is probably familiar to anyone who works in infectious disease or global health. It is an automated, self-contained PCR analyzer: you insert a sample cartridge, close the lid, and the machine amplifies and detects nucleic acid without any additional laboratory steps. It was originally developed for tuberculosis diagnosis — specifically to detect the TB bacterium and flag rifampicin resistance mutations — and since then has been adapted for HIV viral load measurement, SARS cov two, hepatitis, and dozens of other pathogens. Roughly eleven thousand GeneXpert systems are deployed in more than a hundred and thirty countries, with particularly heavy penetration in low- and middle-income settings precisely because it does not require a trained laboratory technologist to operate.

The question the study tested: could you combine an air sampler's collection substrate with a GeneXpert cartridge and get a meaningful result?

The answer is a qualified yes. In laboratory spike experiments — where the researchers deposited known quantities of inactivated virus directly onto the air sampler's collection substrate — the GeneXpert could detect as few as ten copies of influenza A or B and ten copies of RSV. SARS cov two required at least a hundred copies before the system registered a positive, indicating lower analytical sensitivity for that target. In real-world longitudinal sampling across congregate settings in Missouri and Wisconsin over 2024 and 2025, collecting two hundred and eighty-one air samples in total, the system detected SARS cov two most frequently, followed by influenza A.

When the team compared GeneXpert results against standard RT-qPCR run on the same samples, the agreement was fair to moderate for SARS cov two — they report kappa statistics in the range of point three to point four four depending on the cycle threshold cutoff used. Kappa is a statistic that measures agreement between two methods while accounting for the possibility they would agree by coincidence. A kappa of zero means no agreement beyond chance; a kappa of one is perfect agreement. For influenza A, the concordance was somewhat better: a kappa of point five six, with eighty-five percent sensitivity and eighty-one percent specificity at the optimal cycle threshold.

The numbers are honest about the limitations. The GeneXpert is not yet ready to replace RT-qPCR as the reference method in a research context. But for near-real-time environmental monitoring — where the goal is speed and on-site deployability rather than perfect sensitivity — a system that returns a result in under an hour, using hardware already sitting in a hospital corridor or clinic waiting room, has obvious appeal.

The broader argument the study is making is one of infrastructure leverage. The world invested heavily in wastewater surveillance over the past five years, and it proved its value for detecting community respiratory and enteric pathogen trends before clinical systems saw a signal. Air surveillance within facilities could be a complementary layer — catching transmission in specific high-risk settings like intensive care units, emergency departments, and nursing homes, where the concentration of vulnerable people is highest and early detection has the most impact. The GeneXpert's massive global installed base means the hardware is already there. This study is asking whether it can do double duty, and the preliminary answer is that it can, within limits that future work will need to refine.

---

On the business side.

One of the more striking trends in biomedicine over the past two years has been the push to bring CAR-T cell therapy into autoimmune disease. A brief recap of the underlying technology: CAR-T stands for chimeric antigen receptor T cell therapy. It was developed as a cancer treatment. The approach works by removing a patient's own T cells — the immune system's cytotoxic, or cell-killing, lymphocytes — engineering them in a laboratory to express a synthetic protein called a chimeric antigen receptor, which gives the T cells a new targeting capability, and then infusing those engineered cells back into the patient. For certain aggressive B cell lymphomas and leukemias, CAR-T therapy has produced durable remissions in patients who had failed every other available treatment.

But the technology comes with two significant constraints. First, the cost: commercial CAR-T therapies typically run three hundred thousand to five hundred thousand dollars per treatment cycle, the result of bespoke, patient-specific manufacturing. Each batch of cells is made for a single patient, using their own cells, at a specialized facility. Second, the timeline: obtaining the cells, shipping them to a manufacturing site, engineering and expanding them, performing quality release testing, and shipping back typically takes four to six weeks. In oncology, where patients may be deteriorating rapidly, that lag is itself a clinical problem.

For autoimmune disease, these constraints matter even more. Conditions like systemic lupus erythematosus — lupus, for short — are not immediately life-threatening in the way that a relapsed aggressive lymphoma is, and the patient population is vastly larger, measured in the hundreds of thousands in the US alone. The economics of a half-million-dollar, one-time cell therapy are simply not viable at the scale that autoimmune disease requires.

This week, Moderna disclosed a program they internally call mRNA-6007 — nicknamed 007, for its license to kill pathogenic cells — which takes a fundamentally different approach to the engineering problem. Rather than removing and re-engineering cells outside the body, the strategy is in vivo CAR-T: delivering the CAR-encoding instructions directly into the patient using Moderna's mRNA lipid nanoparticle platform.

Here is the mechanism. Lipid nanoparticles — the tiny fat-based particles used to deliver mRNA in the SARS cov two vaccines — encapsulate mRNA and ferry it into cells. By modifying the lipids and targeting ligands on the nanoparticle surface, the particles can be directed to specific cell types; which receptors a particle binds determines which cells take up the mRNA. For mRNA-6007, the payload is mRNA encoding a chimeric antigen receptor designed to target CD19, a protein displayed on the surface of B cells. CD19 is already the target of multiple approved CAR-T therapies for B cell cancers, so its biology in the CAR-T context is well-characterized.

In autoimmune diseases like lupus, a subset of B cells are producing antibodies that recognize and attack the patient's own tissues — in lupus, this includes the kidneys, joints, and skin. The CAR-encoded in the mRNA-6007 program directs the patient's own T cells to find and eliminate CD19-positive B cells. Because the mRNA payload degrades within days rather than integrating into the genome, the CAR expression is transient; the T cells express the receptor for a limited window, deplete the B cell population, and then return to baseline as the mRNA is cleared. That transience is actually an advantage: conventional ex vivo CAR-T cells can cause prolonged B cell aplasia — a complete absence of B cells — with attendant infection risk. A transient mRNA approach could allow the immune system to reconstitute normally afterward and might be re-dosed when needed.

Moderna's program is in early development; human trials are not yet underway. The company plans to move into clinical testing within the next year, with initial focus on systemic lupus erythematosus and other B cell-mediated autoimmune diseases. The significance here is less about this specific molecule and more about the direction it represents: the mRNA delivery platform proven by the COVID vaccine rollout is now being adapted for cell programming in ways that could collapse the cost and complexity of what has been one of medicine's most powerful but least accessible therapeutic categories.

---

On AI in the biomedical sciences.

Tuberculosis remains one of the world's most serious infectious disease problems. The bacterium Mycobacterium tuberculosis — the pathogen behind TB — kills more than one million people per year and infects roughly a quarter of the global population in a latent form. The rise of drug-resistant TB strains has made treatment substantially harder: drug-resistant TB requires longer regimens, often with more toxic second-line drugs, for eighteen months to two years or more. Getting drug selection right early matters enormously — months on an ineffective regimen while the bacterial population grows is not just a treatment failure, it is a selection pressure that can generate further resistance.

Whole genome sequencing of M. tuberculosis has become an increasingly practical clinical tool. The genome of each bacterial isolate from a patient contains mutations that confer resistance to specific drugs. The World Health Organization has published and regularly updates a curated catalog of those mutations — a structured map of the relationship between specific genetic changes and specific drug resistance phenotypes. The catalog is not complete; there are mutations of uncertain significance, and the underlying biology of resistance for some drugs is not fully understood. But it represents the accumulated knowledge of a large international research community.

Machine-learning models trained on genomic resistance data have reached impressive accuracy for predicting whether a given isolate is susceptible or resistant to a given drug. The problem is interpretability. Most of these models are black boxes: they assign a probability of resistance without any indication of which mutations drove the prediction or how confident the model is about that prediction. For clinical adoption, that opacity is a barrier. A clinician needs to know not just what the model thinks, but whether the model's basis for its conclusion is solid or speculative.

A paper posted to arXiv this week introduces KG-TRACE, a framework that addresses this. The name stands for knowledge graph-grounded trace. The key idea is neuro-symbolic AI — a class of approach that combines a neural network, which learns statistical patterns from training data, with a symbolic knowledge representation, which encodes structured, human-interpretable biological relationships.

In KG-TRACE, the neural component processes genomic features from whole-genome sequences and learns from a large dataset of TB isolates with known resistance phenotypes. The symbolic component is the WHO mutation knowledge graph, which represents the established, experimentally validated relationships between specific mutations and specific drugs as a structured network. The framework integrates the two through what the authors call an epistemic trust gate. Epistemic refers to knowledge and its limits. The trust gate is a learned mechanism that, for each prediction, evaluates how well the mutations in the query genome correspond to known entries in the WHO knowledge graph. When a mutation driving a prediction is well-documented — for example, a canonical isoniazid-resistance mutation in the katG gene — the system weights the prediction through that biological knowledge and produces a high-confidence output. When the mutations involved are novel or absent from the database, the gate reduces confidence and flags the output as uncertain.

The model was evaluated on the CRyPTIC cohort — short for Comprehensive Resistance Prediction for Tuberculosis, an international consortium that assembled one of the largest curated datasets of M. tuberculosis whole genomes with matched drug susceptibility testing results. For isoniazid, a first-line TB drug, KG-TRACE achieved an AUROC of 0.9760. AUROC stands for area under the receiver operating characteristic curve — it measures how well a model distinguishes between two classes, in this case susceptible and resistant isolates, across all possible decision thresholds. A value of one is perfect; random guessing gives you point five. An AUROC above point nine five is considered excellent for drug resistance prediction.

What makes this system potentially useful in practice is the uncertainty signaling as much as the raw accuracy. A tool that gives a clinician a high-confidence isoniazid resistance flag tied to a catalogued mutation is a different clinical object than one that gives the same flag for an unusual mutation not in the WHO database. The trust gate makes that distinction explicit, giving the clinician a basis for deciding whether to follow the recommendation or pursue additional testing. As whole-genome sequencing of TB becomes routine in more clinical settings, interpretable AI systems of this kind will matter.

---

And finally, animals.

Great white sharks should not, by most conventional biological reasoning, be living in the Mediterranean Sea. The species evolved in cold, temperate waters, preys primarily on marine mammals like seals and sea lions, and depends on a prey base that the Mediterranean — a nearly enclosed sea with a relatively limited pinniped population and warmer temperatures than the eastern North Atlantic — does not obviously support. Yet historical records extending back to the 1860s consistently document great whites appearing in Mediterranean waters, particularly around the Iberian Peninsula, Sicily, and the Adriatic.

For more than a hundred and sixty years, marine biologists debated whether these were isolated strays that had wandered in from the Atlantic through the Strait of Gibraltar, or evidence of a small resident population somehow persisting in an inhospitable habitat. The question matters because the two possibilities have very different conservation implications. Strays from the Atlantic population have one set of management needs; a separate Mediterranean breeding population in critical decline has a different and more urgent set.

Recent reporting has focused on the accidental capture of a juvenile great white shark by Spanish fishermen in the Mediterranean. The animal was approximately two meters long and weighed between eighty and ninety kilograms. The detail that matters most is the word juvenile. Adult great white sharks are documented ocean travelers — individuals in the Atlantic have been tracked crossing entire ocean basins. A juvenile, still developing and not yet established in long-distance movements, is far more likely to be locally born than to be a stray from a distant Atlantic population.

Researchers who reviewed the full 160-year record of Mediterranean great white observations describe a pattern consistent with a small but real breeding population: recurring presence over too long a timespan, too consistent a geographic distribution, and too many juvenile individuals to explain as coincidental strays. The Mediterranean population is assessed as critically endangered — possibly numbering in the very low hundreds at most — and may be declining. But the persistence of juveniles in the record suggests that reproduction has been occurring somewhere in the basin, even if the exact nursery grounds have never been identified.

There is something striking about the fact that an apex predator — one of the ocean's most iconic animals — may have maintained a breeding population, largely undetected, for over a century and a half in waters surrounded by some of the most densely populated and heavily fished coastlines on Earth. It says something about how little we still understand about what is living in the marine environments just off the coast.

---

That's it for today. A point-of-care device that can sniff viruses out of the air. Moderna's bet that an mRNA injection can do what cell factories do. An AI that reasons transparently about tuberculosis drug resistance. And a ghost shark that has been there all along.

See you tomorrow morning.
