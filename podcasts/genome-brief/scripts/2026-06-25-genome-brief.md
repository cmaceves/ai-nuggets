# Episode 3: Reading COVID's escape map

Paper link: https://doi.org/10.1080/22221751.2026.2686472
Paper link: https://doi.org/10.1007/s11033-026-12220-z
News link: https://finance.yahoo.com/healthcare/articles/ollin-biosciences-announces-oversubscribed-330-110000599.html
Paper link: https://www.nature.com/articles/s41437-026-00822-z

## Script

Welcome to The Genome Brief. Today is Thursday, June twenty-fifth, twenty twenty-six, and this is Episode three.

Here's what's on the table today. In pathogen watch, researchers have just mapped every possible mutation in the receptor-binding domain of the dominant circulating SARS cov two variants — and the results tell us precisely which positions the virus is most likely to mutate next under immune pressure, and why evolution there comes at a cost. Second, a new wastewater surveillance workflow from Argentina that catches genomic diversity that clinical sequencing misses — and does it affordably enough to actually scale. On the business side, a Texas biotech called Ollin Biosciences just closed a three-hundred-and-thirty-million-dollar Series B for a retinal disease drug that beat the current standard in a head-to-head trial. And to close, a whole-genome study finally explains why South Africa's Cape leopards are half the size of other African leopards — and it turns out to be one of the cleanest examples of local adaptation you'll find anywhere in modern genomics.

Let's get into it.

---

Pathogen watch.

SARS cov two keeps evolving. Each new wave of variants accumulates mutations in the part of the spike protein that the immune system has learned to target. The question that drives a lot of surveillance and lab work right now is: which specific mutations can today's variants use to slip past current antibody defenses — and which ones would cost the virus too much in terms of its ability to actually infect cells?

A team across several universities in China published a paper this week in the journal Emerging Microbes and Infections that tries to answer that question for JN.1 and XEC — the two lineages dominating global circulation right now. The method they used is called deep mutational scanning, and I want to explain how it actually works before getting into the results, because the method is the key to understanding why these findings carry real predictive weight.

The receptor-binding domain — the part of the spike protein that physically latches onto the ACE2 receptor on your cells to initiate infection — is made up of about a hundred and eighty amino acids. Each one of those amino acids can, in principle, be swapped out for any of the other nineteen standard amino acids. Deep mutational scanning creates a comprehensive library containing every one of those possible single-position swaps — thousands of variants all at once — and tests them all in parallel in the lab.

For each variant in the library, you ask two questions simultaneously. First, can it still infect cells effectively? And second, does it escape a given antibody? The team used a pseudovirus system to do this safely. A pseudovirus is an engineered particle that displays the SARS cov two spike protein on its surface but carries a harmless reporter gene inside instead of a real viral genome, so you can measure infection without working with live virus. You run your library of spike variants through, add your antibody of interest, and any variant that manages to infect despite the antibody being present is flagged as an escape mutant.

The researchers first screened six monoclonal antibodies — lab-produced single-specificity antibodies — against both JN.1 and XEC pseudoviruses to see which ones still neutralized the current variants. Only two retained meaningful activity. That's striking in itself: four out of six antibodies tested were already largely ineffective against JN.1 and XEC. The two survivors were a conventional immunoglobulin G antibody and a mucosal antibody of the class found in saliva and respiratory secretions — that type is called secretory immunoglobulin A. Those are the two they mapped.

Here's what the escape analysis revealed. For the conventional IgG antibody, escape mutations clustered at specific positions in what the paper calls the receptor-binding motif and receptor-binding ridge — two surface regions on the receptor-binding domain that directly contact ACE2. For the mucosal antibody, the biggest escape hotspot sat at position three-forty-six on the receptor-binding domain, with a secondary hotspot at position four-ninety-three. These are different positions from the IgG escape sites, which makes sense: each antibody targets a different face of the protein, and mutations in different places are required to dislodge it.

What gives the paper its teeth is the next step. The researchers compared their identified escape positions against real-world sequencing data and found that positions three-forty-six, four-fifty-six, and four-ninety-three are precisely the sites where mutations have been accumulating in the most recent JN.1 descendants circulating globally right now — including the sub-lineages KP.2 and KP.3. The experiment and the surveillance data are telling the same story. These are the evolutionary pressure points, and natural selection has already found them.

There's one constraint that I think is underappreciated in how this kind of work usually gets reported. The escape hotspots are concentrated at the ACE2-binding interface — the same surface that the virus needs to physically contact in order to enter a cell. That creates a fundamental fitness tradeoff. A mutation that helps the virus dodge an antibody by altering that interface may simultaneously weaken the virus's grip on ACE2. Escape and infection are competing objectives, and they're competing over the same patch of protein. The data show this directly as an inverse relationship: mutations that strongly escape a given antibody tend to also reduce cellular infection efficiency, and vice versa.

What this means practically: the virus is not free to escape in arbitrary directions. It's constrained to escape paths that don't break its ability to infect. That's actually somewhat reassuring from a pandemic-preparedness standpoint, because it narrows the search space for variants likely to cause real problems. For vaccine strain selection, knowing which escape positions carry the least fitness cost is exactly the input you need to decide whether to update the target sequence in the next vaccine formulation.

---

Still in pathogen watch, but shifting from evolution to surveillance.

A group at the National University of Patagonia in Argentina published a paper this week in Molecular Biology Reports that addresses a surveillance gap that doesn't get enough attention. Clinical sequencing of SARS cov two has been declining in many parts of the world. Budget pressure, falling case counts, changed public-health priorities — whatever the cause, the stream of sequence data that powered real-time variant tracking during the pandemic is narrowing in a lot of regions. If the next significant variant emerges somewhere with limited clinical sequencing capacity, we may not notice it for weeks.

Wastewater surveillance is the natural complement, because the genetic diversity of virus in wastewater reflects what's circulating in an entire city's population — regardless of whether anyone infected ever gets tested. But existing workflows for turning wastewater samples into useful genomic data are often complex and costly, and tools for actually characterizing the full diversity present in a sample, rather than just identifying the dominant variant, have lagged behind.

The paper presents a new end-to-end workflow combining an improved lab procedure for concentrating high-purity viral RNA from wastewater with a custom R package for diversity analysis built on information theory. Information theory, in this context, provides mathematical tools — originally developed for telecommunications — that quantify how much variation or uncertainty exists at each position across a population of sequences. Applying that to a wastewater sample gives you a position-by-position diversity map across the entire receptor-binding domain, showing where the population of circulating viruses is uniform and where it's actively diversifying.

The team validated the workflow on samples from a single urban wastewater treatment node, collected at two very different points in the pandemic: an early phase when ancestral lineages were circulating regionally, and a later Omicron phase when subvariants had spread globally. In the early samples, the diversity patterns showed geographic fingerprints — mutations characteristic of specific regional lineages that matched local clinical sequencing data from the same period. In the Omicron samples, the patterns shifted to reflect global spread. In both cases, the workflow also found variants and diversity signals that clinical surveillance had not captured: location-specific mutation frequency differences revealing biogeographical trends that only wastewater could see.

The case for tools like this is straightforward. Wherever clinical sequencing is limited or declining, wastewater gives a complementary view of what's circulating at the community level. That's especially important given that the most consequential variants are statistically more likely to emerge in precisely the settings with the least genomic surveillance capacity.

---

On the business side.

A biotech based in Houston called Ollin Biosciences raised three hundred and thirty million dollars in an oversubscribed Series B round yesterday, June twenty-fourth, to fund global Phase Three clinical trials for its lead drug OLN three twenty-four. The round was co-led by T-C-G-X and A-R-C-H Venture Partners, with participation from Andreessen Horowitz Bio and a number of major institutional funds.

The drug targets two of the most common causes of serious vision loss in adults: diabetic macular edema — DME — and wet age-related macular degeneration, known as wet AMD.

Both conditions involve pathological changes in the blood vessels of the retina, the light-sensing layer at the back of the eye. In DME, which develops as a complication of diabetes, fluid leaks from damaged retinal capillaries into the macula — the small central zone of the retina responsible for sharp reading and facial recognition. In wet AMD, abnormal new blood vessels grow beneath the retina and leak, also damaging the macula. Both conditions can cause rapid, severe, and sometimes irreversible vision loss if untreated.

The current standard of care for both is a drug called faricimab, sold as Vabysmo by Roche. Faricimab was itself a significant advance when it launched, because it was the first approved drug for these conditions to block two molecular targets simultaneously: VEGF, or vascular endothelial growth factor — the protein primarily responsible for driving abnormal vessel growth — and angiopoietin-two, often shortened to Ang-two, a protein that destabilizes blood vessel walls, promotes leakage, and fuels inflammation in the retina.

That dual approach turned out to be meaningfully better than blocking VEGF alone, because the two proteins drive the same disease through overlapping but distinct mechanisms. Blocking only VEGF often leaves angiopoietin-two still active and still contributing to the problem.

OLN three twenty-four targets the same two proteins, but is engineered differently — it's what's called a bispecific antibody, meaning a single engineered molecule with two binding arms, one for each target. In a head-to-head Phase 1b clinical trial called JADE that compared it directly against faricimab in patients with both DME and wet AMD, OLN three twenty-four showed faster and greater improvement in retinal anatomy — the objective measure of whether fluid is clearing from the macula — and numerically better vision gains.

Head-to-head trials against an approved standard are expensive and logistically demanding, and companies don't attempt them unless early data gives them real reason to think they can show superiority. The three-hundred-thirty-million-dollar raise now funds Phase Three global trials, due to start in the second half of this year.

---

And finally, animals.

Let me tell you about the Cape leopards of South Africa.

Leopards are found across a huge range — most of sub-Saharan Africa and into South and Southeast Asia. Adult male African leopards typically weigh somewhere between forty and ninety kilograms. The leopards that live in South Africa's Cape Floristic Region — the dense, rugged shrublands and mountain ranges of the Western Cape province — weigh almost half that. Their males rarely exceed forty kilograms. They are obviously, visibly smaller than leopards you'd encounter anywhere else on the continent.

For a long time, the dominant explanation was essentially: they're small because they're inbred and isolated. The Cape Floristic Region is geographically fragmented, and the assumption was that this population had gone through genetic bottlenecks — sharp reductions in population size that had shrunk the gene pool and left these animals diminished. Some population ecologists worried they might be on a slow trajectory toward extinction.

A paper published this week in the journal Heredity, based on whole-genome resequencing of forty-three leopards including ten from the Western Cape, dismantles that story comprehensively.

The genetic distinctiveness is real. The Cape leopards have been isolated from other African leopard populations for roughly twenty thousand years. That isolation began during the Last Glacial Maximum — the most recent ice age peak, when global temperatures dropped, southern Africa became cooler and drier, grassland gave way to more fragmented habitat, and leopard populations became separated. The Cape population has been on its own ever since, forming a genetic cluster clearly separate from savanna or eastern African lineages.

But the size difference is not an artifact of inbreeding. It's adaptation. The researchers identified about ninety genes showing signatures of positive selection in the Cape population — meaning they're unusually common in these leopards, in a pattern that's hard to explain by chance and points to natural selection actively promoting them. Those genes are predominantly involved in body size, muscle development, bone structure, and energy metabolism. The smaller body plan wasn't imposed on these animals by genetic poverty; it was refined over thousands of generations because smaller worked better in their particular environment.

The reason for that selection is prey. The Cape Floristic Region doesn't have the large antelope and buffalo that sustain savanna leopards. Its dominant small mammals are rock hyrax — small, rotund relatives of elephants that weigh about two to four kilograms — and klipspringer, a nimble antelope adapted to rocky terrain that tops out around twelve kilograms. Hunting ten-kilogram prey in mountainous shrubland favors a different body architecture than hunting a hundred-kilogram kudu on open savanna. The leopards evolved to fit the landscape they had.

The genetic diversity finding was the second surprise. Despite twenty thousand years of isolation and a severe population collapse driven by hunting and habitat loss in the nineteenth and twentieth centuries, the Cape leopards have only slightly lower genetic diversity than other African leopard populations. That's a meaningful positive signal for conservation. The paper calls for these animals to be recognized as evolutionarily significant units — a formal designation meaning they represent a distinct genetic heritage that warrants targeted protection, not just a subpopulation to be swept into a generic management plan.

It's a story about what genomics can do that decades of observations couldn't: separate adaptation from deterioration, and reveal that an animal thought to be weakened is actually precisely fitted to its place.

That's it for today. Thanks for listening to The Genome Brief.
