# Episode 21: Why TB hits men harder

Story link (TB sex-biased immunity, Bishai/Klein labs, bioRxiv): https://www.biorxiv.org/content/10.64898/2026.07.07.737119v1
Story link (eplontersen CARDIO-TTRansform failure, BioPharma Dive): https://www.biopharmadive.com/news/astrazeneca-ionis-eplontersen-ttr-cardiomyopathy-study-results-failure/824799/
Story link (Evo Variant Effect Explorer, Goodfire, bioRxiv): https://www.biorxiv.org/content/10.64898/2026.04.10.717844v1
Story link (Neil the Seal returns to Tasmania, phys.org): https://phys.org/news/2026-07-neil-viral-animal-global-folk.html

## Script

Good morning. Welcome to The Genome Brief. It's Monday, July thirteenth, twenty twenty-six. Three stories today, plus a seal.

On the pathogen front: a new paper out of Johns Hopkins takes on a long-standing epidemiological puzzle — why tuberculosis is roughly twice as deadly in men as in women. The answer, they argue, is not hormones and not chromosomes on their own. It is a specific programming of female T cells combined with the way immune tissue organizes itself in the lung. It is one of the more mechanistically satisfying pieces of TB immunology to appear in a while.

On the business side: an antisense drug for a serious heart condition has failed its main Phase 3 trial. The drug is eplontersen, from AstraZeneca and Ionis. The condition is transthyretin cardiac amyloidosis. The failure reshapes a rapidly moving competitive landscape, and we'll walk through what happened, why it might have failed, and who benefits.

On the AI front: a paper posted this weekend from Goodfire and collaborators shows that a large DNA foundation model can classify roughly four million genetic variants for pathogenicity — and, more interestingly, it can explain why. Variants of uncertain significance are the single largest bottleneck in clinical genomics, and this is a real step toward closing that gap.

And to close: Neil the Seal is back in Tasmania. He is one ton, he is molting, and he has one point three million TikTok followers. The biology of what is happening to him is genuinely bizarre.

Let's start with tuberculosis.

---

Tuberculosis kills more people than any other single infectious disease on the planet. It has for most of human history. And for as long as anyone has been looking, the disease has hit men harder than women. Male-to-female ratios of active TB run about two to one in most populations. The men-are-worse pattern holds after correcting for occupation, smoking, alcohol, HIV, and access to care. Something biological is driving it.

The paper posted to bioRxiv on Friday, from the Bishai and Klein labs at Johns Hopkins, works through the mechanism in unusual detail — and the result is that the answer has almost nothing to do with sex hormones and almost everything to do with how the immune system is wired and how it organizes itself in tissue.

The tool they used to get there is worth understanding, because it is what makes this study different. It is called the Four Core Genotype mouse model. Ordinary mice come in two flavors: XX females and XY males. What the Four Core Genotype mice let you do is uncouple two things that are normally glued together — the sex chromosomes an animal carries, and the gonads it develops. Through a specific genetic trick, you can produce mice that are XX but develop male gonads, and mice that are XY but develop female gonads. So instead of two groups, you have four: XX female, XX male, XY female, XY male. If you see a difference between groups, you can now tell whether it is being driven by the sex chromosomes themselves, or by the gonadal hormones, or by some combination.

The Hopkins group infected these mice with Mycobacterium tuberculosis, then dissected the immune response. And here is the first surprise. The protection was not tracking with hormones. It was not tracking with chromosomes on their own either. It was tracking with a specific programming that gets stamped into T cells in female animals during development.

To show this, they took CD4 T cells — a class of immune cells whose entire job is to coordinate the response against intracellular infections like TB — out of gonadal-female mice, and transferred them into susceptible XY-male mice. The recipients got protected. The male recipients now controlled the infection better. Female CD4 T cells, on their own, transferred protection. When they did the same transfer from XX-male donors — same chromosomes as XX females, but male gonads — the protection did not transfer. So the effect was not just about the XX chromosome complement. It was about the T-cell programming that develops under female biology.

What are those T cells actually doing that is different? Two things. First, they set up a particular kind of helper response in the lung — the researchers picked it up as an expansion of Bcl6-expressing CD4 T cells, which are the T cells that go into lymphoid follicles and help B cells. Second, they suppress the neutrophil part of the response. Neutrophils are fast-moving innate immune cells that are excellent at killing many pathogens but that, when they overreact in the lung, are actually a major driver of TB tissue damage. The female T cells kept a lid on the neutrophils. The male T cells didn't.

Two molecular signals turned out to be doing this work. One is a chemokine receptor called CXCR3, which is essentially a molecular GPS that homing T cells use to find sites of inflammation. The other is CD40 ligand, which is the handshake T cells use to license B cells and dendritic cells. When they blocked either of those two signals, the female protection disappeared. Female CD4 T cells were using CXCR3 to get to the right place in the lung, and CD40 ligand to organize the tissue once they got there.

And that word — organize — is the second half of the story. When you look at the lungs of TB-infected animals, in the ones controlling the infection well, you see something structured. You see B-cell follicles: little balls of B cells with T cells around them, embedded in the lung parenchyma. These are called tertiary lymphoid structures. They are the immune system building a lymph node on the fly, at the site of infection. In animals that fail to control TB, the B cells are still there, but they are scattered — no follicles, no organization.

To test whether that organization matters, the group depleted B cells in their mice. The result is the interesting part. When they knocked out the B cells, the total bacterial load did not change much — which was surprising in its own right. But the pattern of failure was completely different between the sexes. In females losing their B-cell follicles, what changed was the T-cell response: it collapsed and reorganized in ways that suggested the B-cell scaffolding had been holding the adaptive immune response together. In males, when you took the B cells out, everything went the other direction — the neutrophils came roaring in, and the lungs filled with what are called neutrophil extracellular traps, or NETs. These are webs of DNA and toxic enzymes that neutrophils extrude when they die. Useful in some infections. Terrible in TB, where they damage lung tissue and don't help clear the bacteria.

So the picture that emerges is layered. Female mice have CD4 T cells that are intrinsically wired to run a coordinated, follicle-based response, and to hold down destructive inflammation. Male mice don't. When you remove the female-style scaffolding — for example by knocking out the B cells — the male immune system defaults to a pattern that looks a lot like the pathology you see in severe human TB.

Why does this matter for humans? A few reasons. The first is basic understanding. It reframes the sex disparity in TB not as a hormonal question but as a developmental-programming question — something being set into female T cells during their maturation. That is a testable, druggable target class in the long run. The second is TB vaccine design. The only widely used TB vaccine, BCG, is a hundred years old and is known to protect children better than adults and to work variably across populations. Modern TB vaccine candidates are struggling in trials. If the difference between a productive and a destructive lung response comes down to whether you build organized B-cell follicles or not, that is something a vaccine could try to induce on purpose. The third is a caution. Almost all TB drug and vaccine trials use pooled male-and-female data. If the underlying immune architecture is meaningfully different, some interventions may work better in one sex than the other, and we are currently blind to that.

The paper is a preprint — not peer reviewed — but it is a careful piece of work from a serious lab. It reframes a puzzle that has been sitting in TB epidemiology for a century.

---

On the business side, one of the biggest cardiology stories of the year landed on Friday: AstraZeneca and Ionis announced that their Phase 3 trial of eplontersen in transthyretin cardiac amyloidosis had failed its primary endpoint. Ionis shares fell twenty-one percent. AstraZeneca fell eight. And the shape of the market for this disease has been redrawn.

Let me back up and explain what any of that means, because this is a story that hinges on a small piece of protein biology.

Transthyretin, or TTR, is a protein your liver makes. Its normal job is to shuttle thyroid hormone and vitamin A around your bloodstream. It floats around as a stable tetramer — four copies of the protein stuck together. And in most people, that is the end of the story.

But in some people — either because they carry a mutation in the transthyretin gene, or simply because they are old — the tetramer becomes unstable. It falls apart into individual protein monomers. Those monomers misfold. They stick to each other. They deposit as amyloid fibrils in tissues, especially in the heart and in nerves. That deposition is what causes disease. When the deposits are in the heart, they stiffen the heart muscle, and the result is a progressive, disabling, ultimately fatal heart failure syndrome called transthyretin cardiac amyloidosis. This condition, until about seven years ago, had no approved treatment.

Since then the treatment landscape has exploded. Four drugs are relevant. First, tafamidis — brand name Vyndamax, from Pfizer — approved in 2019, sales over six billion dollars a year. It is a stabilizer. It binds the transthyretin tetramer and physically holds it together so it can't fall apart into misfolding monomers. Second, acoramidis — brand name Attruby, from BridgeBio — approved in 2024. Also a stabilizer, same category, more potent by some measures. Third, vutrisiran — brand name Amvuttra, from Alnylam — approved for cardiomyopathy last year. That one works completely differently: it is an RNA interference drug, or siRNA, which silences the messenger RNA for transthyretin inside liver cells so the protein is never made in the first place. And fourth, eplontersen, from AstraZeneca and Ionis, which is the drug that failed on Friday.

Eplontersen is what's called an antisense oligonucleotide, or ASO. That is a short piece of synthetic single-stranded nucleic acid designed to bind, by base pairing, to a specific messenger RNA — in this case, the transthyretin messenger RNA. When the ASO binds, a cellular enzyme called RNase H recognizes the RNA-DNA hybrid and chops the RNA up, so the protein never gets translated. Vutrisiran and eplontersen are doing roughly the same thing — knocking down the transthyretin protein at the source — through different molecular machinery. Vutrisiran uses the RNAi pathway; eplontersen uses the ASO pathway. In principle, both should work.

Eplontersen has actually been on the market since 2023 for the polyneuropathy form of transthyretin disease — where the amyloid deposits are in nerves rather than heart. It was already generating over two hundred million dollars in quarterly sales in that indication. The heart trial, called CARDIO-TTRansform, was the big-ticket expansion. It enrolled fourteen hundred patients. The primary endpoint was a composite of all-cause mortality and recurrent cardiovascular events over roughly three years.

It missed. Eplontersen did not significantly reduce that composite endpoint compared to placebo.

There is one clue about why. Cardiac amyloidosis patients in this trial were often already on a stabilizer drug — tafamidis or acoramidis. At baseline, fifty-seven percent of patients were on one. During the trial, another twenty-four percent started one. That means over eighty percent of the trial population ended up on a stabilizer at some point. And when the trial was analyzed by whether patients were on a stabilizer or not, the story split. In patients not on a stabilizer, eplontersen showed a twenty-nine percent reduction in the primary endpoint — a meaningful effect. In patients on a stabilizer, there was no effect at all.

The likely interpretation is not that eplontersen doesn't work. It is that stabilizers work so well now that in patients already on one, there is very little residual disease progression left to prevent. In other words, the standard of care changed under the trial. When the trial was designed, few patients were on a stabilizer. By the time it read out, most were. And the drug was competing against a background where the disease had already been meaningfully slowed.

That leaves AstraZeneca and Ionis in a hard spot. They can push for approval in stabilizer-naive patients only — but that is a shrinking population, because more patients are being started on stabilizers earlier. And it hands the knockdown-drug space in cardiac amyloidosis to Alnylam's vutrisiran, which won a comparable Phase 3 trial in this indication in 2024. Alnylam stock, unsurprisingly, jumped on Friday. BridgeBio's stock jumped too, on the theory that stabilizers just proved themselves indirectly.

The broader takeaway for the field is that this is what a maturing disease area looks like. Trials that would have won ten years ago are getting harder because there is already something on the market that works well. Trial designers are going to have to think carefully about how to show benefit on top of a strong background regimen.

---

On the AI front — an interesting paper from a group called Goodfire, in collaboration with Mayo Clinic researchers, on using a genomic foundation model to interpret genetic variants.

Some context first, because this is one of those problems where the size of the pile matters more than any single item on it. When a patient gets a genome sequenced today, the analysis pipeline compares their DNA against a reference and identifies places where the two disagree. A typical genome yields hundreds of thousands of variants. Most of them are benign. A small number cause disease. For any given variant, the clinical question is: does this thing hurt the patient?

ClinVar is the public database where clinical labs deposit their answers. ClinVar today holds about four million variants. Most of them are classified as "variant of uncertain significance," or VUS — meaning nobody yet knows whether they are benign or pathogenic. That uncertainty is a real clinical problem. It shows up on reports. It gets communicated to patients. It affects screening decisions and family testing.

For decades, computational tools have tried to help. They fall into a few categories. Some use protein-structure predictions to guess whether a missense mutation — a variant that changes one amino acid — will break the protein. Some look at how conserved the position is across evolution. Some combine dozens of hand-selected features into a composite score. The best of these tools do reasonably well on missense variants. They do worse or nothing at all on other variant types: silent mutations, splice variants, deep intronic variants, and everything non-coding. And most of them produce a number without a why — a pathogenicity score with no interpretable reasoning behind it.

The Goodfire paper takes a different approach. They start from a large genomic foundation model — a model called Evo 2, seven billion parameters, pretrained on a huge sweep of biological sequence data from across the tree of life. That model has, in the process of training, absorbed statistical structure about what DNA sequences look like and how they behave. What the Goodfire group does is not train a new model from scratch. It uses Evo 2's internal representations — the numerical vectors that the model produces when it reads a sequence — and trains a small classifier on top of them.

The trick they introduce is called a covariance probe. Ordinarily, when you want to use a foundation model's internal representation of a sequence, you take the average of all the position-wise numbers. That averaging throws away a lot of information. What the covariance probe does instead is compute the outer product — the pairwise correlations between different dimensions of the representation. Think of it as capturing not just what features are present, but what features co-occur. It preserves second-order structure that mean-pooling flattens.

Trained this way on ClinVar labels, the classifier achieves an area under the ROC curve of point nine nine seven across eight hundred and thirty thousand variants. To translate: for essentially every variant type — missense, silent, nonsense, splice, UTR, deep intronic — it matches or exceeds the best specialized predictors. It also generalizes zero-shot to insertions and deletions, meaning it was never trained on those and still classifies them accurately. That single-framework performance is genuinely new. Most tools work for one variant class and fail on the others. This one is unified.

But the more interesting piece is the interpretability. The authors trained a second set of probes — three hundred and fifty seven of them — on the same Evo 2 embeddings, but each one predicting a specific biological annotation. So one probe learns to predict whether a given base is inside a protein domain, another predicts whether it is at a splice site, another predicts whether it is a phosphorylation site, another predicts secondary structure, and so on across a broad panel of annotations. Then for any variant, they compute the delta: how much does each of these annotations change when you introduce the variant compared to the reference? That gives you a disruption profile — a fingerprint of what specific biology the variant is likely to be breaking.

The example they walk through is a BRCA1 intronic variant sitting three bases upstream of an exon. The disruption profile flags a collapse in splice acceptor prediction: the probability that this position is recognized as an intron-to-exon boundary drops from one point zero to zero. The branchpoint region prediction, upstream of the acceptor, drops from point nine nine to point zero seven. The polypyrimidine tract prediction similarly collapses. That is a mechanistically specific hypothesis: the model is saying, this variant will destroy splice acceptor recognition at exon fifteen. And RNA studies of that variant, done years ago, confirmed exactly that. It produces frameshifting transcripts because the acceptor site is broken.

They then feed those top-ranked disruptions into a large language model to synthesize a natural-language explanation for the clinician. The evaluation of the explanations against expert-annotated ClinVar entries showed the disruption profile was the single biggest contributor to explanation quality — bigger than adding gene name, gene function, or protein-level notation.

The whole thing is available at a public site called EVEE — the Evo Variant Effect Explorer — with pre-computed predictions and on-demand explanations for all four point two million ClinVar variants.

Two things to say about significance. First, most AI-in-biomedicine papers that come across our desks are optimizing a benchmark. This one is targeting an actual clinical bottleneck — the pile of uncertain variants sitting on real patient reports. If a tool of this quality gets integrated into variant-classification workflows, it has direct clinical utility. Second, the interpretability approach is worth watching. The paper argues that interpretability need not be a trade-off against accuracy — that you can get the accuracy and the mechanism from the same set of learned representations, by asking the model different questions. If that generalizes, it points at a different way to build clinical AI: models that don't just predict, but tell you what they think the biology is.

---

And finally, animals. Neil the Seal is back.

Neil is a southern elephant seal, five years old, roughly one ton in weight, and for the past two years he has been an internationally famous animal. He belongs to a species called Mirounga leonina — southern elephant seals — that spend most of their lives in the frigid waters around Antarctica and the sub-Antarctic islands. Every year, though, adult elephant seals haul themselves out onto beaches to do something called the catastrophic molt. And this is the part of the biology that is genuinely strange.

Most animals shed. Dogs shed fur, snakes shed skin, birds molt feathers a few at a time. Elephant seals do not do this in installments. They shed everything — outer skin and fur — all at once, in a single roughly month-long event. During that month, they cannot be in the water: their skin is coming off in sheets, they are metabolically vulnerable, and the cold ocean would be lethal. So they haul themselves onto beaches — or, if the beaches are inconvenient, onto roads — and they wait.

That is why Neil visits Tasmania. Elephant seals from the sub-Antarctic occasionally molt on the Australian mainland. Neil has been doing so since he was a subadult, which is unusual — most animals return to the same colonies. And because Tasmania is not exactly Antarctica, Neil's molt sites have included beaches, driveways, boat ramps, and, most memorably, roads. He knocks over traffic bollards. He resists being moved. He needs a security detail, because he weighs a ton and does not, in his current physiological state, want to walk into the ocean.

He is also now the subject of one point three million TikTok accounts, remixes involving heavy metal soundtracks, and a growing body of thinkpiece essays about why humans project rebel-hero symbolism onto a marine mammal that is simply trying to shed its skin.

The underlying biology, though, is worth pausing on. Elephant seals — the two species combined — are the deepest-diving pinnipeds on the planet. Their dives routinely exceed a thousand meters. They can hold their breath for two hours. They shut down blood flow to most of their tissues during a dive, and they extract oxygen from a specialized store held in their muscle myoglobin. They are, physiologically, closer to a large diving cetacean than to a beach seal.

And once a year, that entire body has to be repaired. The molt reprocesses the skin, the fur, the peripheral tissue supply, and demands enormous metabolic reserves — reserves that elephant seals store as blubber during their at-sea foraging. Which is why, during the molt, they mostly lie still. They cannot afford to move.

That's why Neil sits in Tasmanian driveways. He is not being rebellious. He is being an elephant seal in July. It just happens that in his case, the driveway comes with a fan club.

That is your Genome Brief for Monday, July thirteenth. Thanks for listening.
