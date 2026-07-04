## Script

Paper link: https://www.biorxiv.org/content/10.1101/2025.07.30.667738
Paper link: https://www.biorxiv.org/content/10.64898/2026.07.03.736283
Paper link: https://www.biorxiv.org/content/10.64898/2026.07.03.736369
Paper link: https://ir.veratx.com/news-releases/news-release-details/vera-therapeutics-announces-us-fda-granted-priority-review
Paper link: https://www.science.org/doi/10.1126/science.ady1618

Good morning, and welcome to The Genome Brief for Friday, July fourth. Today: a new malaria resistance gene is quietly sweeping across Uganda; we check how H five N one has fared in the cats of Philadelphia; a big-picture AI benchmark shows what machine learning can and cannot do for tuberculosis drug resistance; and bumble bees pull off something genuinely impressive.

Let's start in Uganda, with a pathogen genomics story that deserves more attention than it is currently getting.

The backbone of modern malaria treatment is artemisinin-based combination therapy — ACTs. You pair artemisinin, which kills parasites fast in the first day or two, with a longer-acting partner drug like lumefantrine that mops up survivors. That two-drug combination is what keeps treatment from failing when one component starts to slip.

For years, the known threat has been Kelch 13 mutations — K13 — which arise in the malaria parasite Plasmodium falciparum and allow it to tolerate artemisinin. K13 mutations originally came out of Southeast Asia and are now spreading in East Africa. We covered a critical causal validation of one of those mutations two days ago.

But a preprint updated on bioRxiv this week from researchers at UC San Francisco, UC San Diego, and Ugandan collaborators reveals a second threat, at a completely different gene — one that nobody was watching. When the team performed whole-genome sequencing on 158 Ugandan Plasmodium falciparum samples and scanned for signs of positive selection across the entire genome, the strongest signal was not at K13. It was at a gene called px1, which encodes a protein involved in how the parasite handles certain fats in its membrane. The team identified a set of three mutations and two small deletions in px1 — they call this the PIN haplotype — and found that PIN-carrying parasites showed significantly decreased susceptibility to lumefantrine, to mefloquine, and to dihydroartemisinin. That last one is the active form of artemisinin itself. In other words, PIN parasites have decreased susceptibility to the two main components of front-line combination therapy simultaneously.

To track how far this has spread, the team genotyped nearly fifteen hundred samples from Uganda collected between 2004 and 2024. In 2004, before artemisinin combination therapies were deployed in Uganda, the PIN haplotype did not exist. It appeared in 2008, two years after artemether-lumefantrine became first-line treatment. By 2024, it had reached over fifty percent prevalence in eastern Uganda and over eighty percent in northern Uganda. Those are majority-prevalence numbers for a previously unknown resistance locus. And critically, PIN spreads independently of K13 — it is found in parasites with and without K13 mutations.

The alarming scenario is a parasite that carries both K13 and PIN. K13 blunts artemisinin. PIN blunts lumefantrine, mefloquine, and to some degree dihydroartemisinin. That leaves a combination therapy with no functional arm. Whether we are already seeing clinical treatment failures driven by this is not yet established — that requires prospective outcome data — but the genomic sweep is unmistakable, and Uganda is already the epicenter of African K13 resistance. The global malaria surveillance community needs to start tracking px1.

On the pathogen watch, a quick note from a University of Pennsylvania study published this week: surveillance of 417 feral and 228 owned cats in the greater Philadelphia area found just one cat — less than a fifth of one percent — with antibodies against clade 2.3.4.4b H five N one. So urban cats in a major American city are not quietly accumulating avian influenza exposure at meaningful rates. SARS cov two was a different story: three percent of the cats tested positive in both binding and neutralization assays, meaning COVID-19 has spread into the urban feral cat population despite no owner contact. Cats appear to be useful sentinels here, and the H five N one signal is reassuring.

On the business side, the FDA has a decision due this Monday, July seventh, on atacicept, from Vera Therapeutics, for IgA nephropathy — the most common cause of autoimmune kidney disease worldwide. In IgAN, the immune system produces a structurally defective version of the antibody immunoglobulin A. This abnormal IgA is recognized as foreign, which triggers the immune system to form complexes that deposit in the kidney's filtering units, causing inflammation and, over years, scarring and kidney failure in a significant fraction of patients.

Atacicept works by blocking two proteins called BAFF and APRIL — B-cell activating factor and a proliferation-inducing ligand. These signals keep the B cells alive that produce the defective IgA. By blocking both simultaneously, atacicept cuts off the upstream driver of the disease-causing antibody. It is the first drug designed to hit both targets at once. The supporting Phase Three trial showed a forty-six percent reduction in proteinuria — the excess protein in urine that marks ongoing kidney damage. Monday's PDUFA date is a meaningful moment for IgAN patients.

Now for AI in biomedicine. A preprint posted this week delivers the largest benchmark yet for using machine learning to predict tuberculosis drug resistance from whole-genome sequencing of the bacteria. The team curated over fifty-four thousand paired genome-and-drug-susceptibility records and tested seven different models across eighteen drugs. The headline finding: XGBoost, a gradient boosting algorithm and workhorse of applied machine learning, outperformed deep learning architectures on most drugs by the metrics that matter clinically. For well-characterized drugs with lots of resistance data, like isoniazid and rifampicin, prediction is already quite good. For newer reserve drugs like bedaquiline and delamanid, all models struggled — because resistant isolates are rare, the genetic mechanisms of resistance are incompletely understood, and training data is sparse. XDR-TB, where even the reserve drugs fail, was the hardest to classify correctly.

The lesson is clear: the bottleneck is not model architecture. It is the data gap and incomplete biology for newer drugs. No machine learning advance closes that gap — it requires more clinical sequencing and more basic research into resistance mechanisms.

And finally, animals.

A paper just published in Science offers a striking result from the world of insect cognition. Bumble bees, which have a brain smaller than a sesame seed, can spontaneously solve a novel problem by combining two pieces of previously learned information they had never been asked to connect before.

Here is the experiment. Researchers first taught bees separately that a blue flower held a reward, and that a ball in the arena could be physically moved. Then they suspended the blue flower from the ceiling, out of reach. Without any further training, some bees solved the problem by rolling the ball underneath the flower and climbing onto it to access the reward. They combined two isolated memories — flower means food, ball can move — into a single novel action plan they had never been shown.

This kind of spontaneous cross-domain problem solving has historically been attributed to large-brained animals: primates, corvids, elephants. The fact that it shows up in a brain smaller than a sesame seed is a direct challenge to the assumption that flexible reasoning requires substantial neural architecture.

That's The Genome Brief for July fourth. The px1 malaria story is one to bookmark. More tomorrow, and happy Independence Day to those celebrating.
