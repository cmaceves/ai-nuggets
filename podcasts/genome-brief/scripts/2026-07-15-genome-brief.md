# Episode 23: The noise that saves malaria parasites

Story link (Kelch13 stochastics determine drug survival in resistant malaria parasites, Spielmann lab, bioRxiv): https://www.biorxiv.org/content/10.64898/2026.07.13.738300v1
Story link (Biogen/Ionis diranersen Phase 2 CELIA data at AAIC 2026): https://investingnews.com/biogen-presents-phase-2-celia-data-at-aaic-demonstrating-meaningful-clinical-outcomes-and-robust-tau-reduction-with-diranersen-in-early-alzheimer-s-disease/
Story link (Dizal / AstraZeneca licensing deal for Zegfrovy, PRNewswire): https://www.prnewswire.com/news-releases/dizal-announces-global-exclusive-license-agreement-with-astrazeneca-for-zegfrovy-302824624.html
Story link (Midwife toads survive chytrid via early-developing antimicrobial peptides, Nature Chemical Biology, UCL press): https://www.sciencedaily.com/releases/2026/07/260714225523.htm

## Script

Good morning. Welcome to The Genome Brief. It's Wednesday, July fifteenth, twenty twenty-six. Four items today, and we'll finish with toads.

On the pathogen front, a really nice piece of malaria parasitology out of the Bernhard Nocht Institute in Hamburg. It's about why, even when a malaria population is fully genetically resistant to artemisinin — the frontline drug — some parasites still die. The answer, they argue, is not something written in the genome. It's noise. Random cell-to-cell fluctuations in how much of one specific protein each individual parasite happens to be making.

On the business side, two big items. First, Biogen and Ionis presented Phase 2 data at the Alzheimer's conference on an anti-tau drug called diranersen. This is arguably the first anti-tau therapy in Alzheimer's history to show a signal on cognitive endpoints alongside dramatic biomarker reductions — but it got there in a strange way, missing its primary endpoint while hitting essentially every secondary. Second, AstraZeneca is paying up to one and a half billion dollars to license a Chinese lung cancer drug called Zegfrovy for markets outside China.

And to close: how some frogs, and specifically the Pyrenean midwife toads, are surviving the fungus that has been running amphibians toward extinction worldwide.

Let's start with the parasites.

---

Malaria. The mosquito-borne parasite Plasmodium falciparum kills about six hundred thousand people a year, mostly African children. The frontline drug against P. falciparum for the last two decades has been a compound called artemisinin, given as part of a combination therapy. Artemisinin is fast, potent, and cheap, and it saved millions of lives after it displaced chloroquine.

But artemisinin resistance is now well established. It started in Southeast Asia in the mid twenty-tens and has been spreading into East Africa. And the interesting thing about artemisinin resistance is that it doesn't look like the classical drug-resistance story you might be used to.

Here's what a classical resistance story looks like. You give the drug. Wild-type parasites die. The parasites that carry a specific resistance mutation survive. That mutation gets selected for, spreads through the population, and eventually the drug stops working because everyone has the mutation.

Artemisinin resistance is weirder. The resistance-causing mutations are in a gene called K13, which encodes a protein called Kelch13. In parasites with resistance mutations in K13, artemisinin still kills — a lot. Not everyone survives. In fact, only a portion of the parasites in a genetically identical resistant population survive the drug. The rest die.

That is a puzzle. If the parasites are all genetically identical, and they all carry the same K13 resistance mutation, and they're all sitting in the same test tube seeing the same drug at the same concentration, why do some live and others die? Something else has to be at work.

The new paper, posted this weekend to bioRxiv from Tobias Spielmann's group at the Bernhard Nocht Institute for Tropical Medicine in Hamburg, is one of the cleanest answers we have to that question. And the answer is beautifully simple. It's noise.

Here's what they mean by noise. Every cell in a population, even in a genetically identical clonal population, actually has a slightly different amount of any given protein at any given moment. Some cells happen to be making a little more of a given protein than others, by pure biochemical chance — because gene expression is bursty, because the timing of transcription is stochastic, because degradation happens in fits. When biologists say a protein "shows expression noise," this is what they mean. The average across the population is fine. But the individuals within it vary.

The paper measures this noise for the Kelch13 protein — the same one whose gene carries the resistance mutations. They generated pairs of isogenic parasite lines: one with wild-type K13, one with the classic C580Y resistance mutation. Then they measured Kelch13 protein levels in individual parasites within each population, one cell at a time. And they found a striking pattern.

First, the C580Y mutation lowers the average level of Kelch13 protein across the population. That much was already known. What's new here is that individual parasites within the resistant population still show a huge range of Kelch13 protein levels. Some have almost as much as the wild-type parasites. Some have almost none. It is a distribution, not a fixed number.

Then they asked which parasites survive drug exposure. And the answer was clean: the low-Kelch13 parasites survive, the high-Kelch13 parasites die. In a genetically identical population. Same DNA, different fate, and the difference is just where in the natural expression range the individual parasite happened to fall on the day the drug arrived.

The mechanism, they argue, is that artemisinin has to be activated inside the parasite to kill it. The activation depends on hemoglobin — the parasite feeds on hemoglobin from the red blood cell it lives in, and the iron in hemoglobin cracks open the artemisinin molecule and releases the toxic species that damages the parasite. Kelch13 is part of the machinery that pulls hemoglobin into the parasite in the first place. So less Kelch13 means less hemoglobin uptake means less drug activation means survival. More Kelch13 means the opposite. And critically, less Kelch13 also comes with a fitness cost — parasites with less of the protein grow more slowly. So there is a natural tension between drug survival and reproductive fitness, playing out at the level of individual cells.

Then the mutations do something clever. Different K13 resistance mutations don't just shift the average protein level. They shift the shape of the distribution — how much of the population sits in the low-Kelch13 survival zone, and how much sits in the high-Kelch13 killing zone. As the mutations get stronger — more clinically resistant — the fraction of parasites in the survival zone grows. But it never becomes one hundred percent. There is always some Kelch13-high tail that dies. Which explains, at the individual-parasite level, why treatment failure with artemisinin looks like partial rather than complete drug loss.

Why this matters. First, it changes how you think about the endgame of artemisinin resistance. If drug survival is fundamentally a stochastic outcome — a lottery, running inside every parasite in real time — then resistance is not going to jump to one hundred percent even in fully mutated populations. There will always be a killing fraction. That is both good news, in the sense that partial artemisinin efficacy will persist, and bad news, in the sense that the resistant parasites who survive get to reproduce and drive the next wave.

Second, and more importantly, it points to a completely different kind of intervention. If you can find a way to push Kelch13 levels up in the parasite — force more of the population into the high-Kelch13 killing zone — you might be able to re-sensitize resistant parasites to artemisinin without needing a new drug. That is a genuinely new therapeutic idea, and it comes directly from thinking of drug resistance as a distribution rather than a switch.

And third, this is the kind of finding that generalizes. There are drug-resistance stories in cancer, in bacteria, in viruses, where a genetically identical population still gives you a spectrum of drug response. Non-genetic expression noise as the actual determinant of individual survival — with the mutation reshaping the distribution rather than dictating a fixed phenotype — is a way to think about all of those cases. The Kelch13 paper is one of the first really clean demonstrations of that principle for a frontline antimalarial in the wild.

---

On the business side. Yesterday I mentioned that Eisai presented biomarker data at the big Alzheimer's conference in London on an anti-tau antibody called etalanetug, and I said the field is waiting for the first anti-tau drug to actually improve cognition, not just clear biomarkers. Later at the same conference, Biogen and their partner Ionis presented Phase 2 clinical data on their anti-tau drug diranersen — and the answer to that waiting question turns out to be, for the first time, yes. Sort of. With caveats. Let's walk through the caveats.

The background. Diranersen — formerly known as B I I B zero eighty — is not an antibody like etalanetug. It's an antisense oligonucleotide, or ASO. An ASO is a short synthetic strand of nucleic acid that binds to a specific messenger RNA and marks it for destruction. In this case, the target is the messenger RNA that encodes the tau protein itself. So diranersen doesn't try to clean up misfolded tau after the fact; it tries to reduce how much tau the neuron makes in the first place. Less production, less pathology, in theory. It is dosed by intrathecal injection — meaning a lumbar puncture — because ASOs don't cross the blood-brain barrier on their own.

The Phase 2 trial is called CELIA. Four hundred and sixteen participants with early Alzheimer's disease — sixty percent with mild cognitive impairment, forty percent with mild dementia — randomized across three dose regimens and a placebo, treated for eighteen months. Notably, none of them had received the amyloid antibodies. So this is a clean look at anti-tau alone.

Now here is the paradoxical result. The primary endpoint was a dose-response on the standard cognitive scale in Alzheimer's trials, called the Clinical Dementia Rating Sum of Boxes, or CDR-SB. That endpoint asks: as you go from low dose to high dose, does the drug work more? And the answer was no. There was no clean dose-response. In fact, the best clinical effect was seen at the lowest dose — sixty milligrams every six months. The middle dose was weaker. The highest dose was weakest of all. That means the trial technically missed its primary endpoint.

But at that low dose, the effect on cognition was, by anti-tau standards, striking. Compared to placebo at eighteen months, the low-dose arm slowed decline by twenty-six percent on CDR-SB, by forty-two percent on a memory-and-language scale called ADAS-Cog13, by fifty percent on the Mini-Mental State Examination, and by thirty percent on a composite score called the integrated Alzheimer's Disease Rating Scale. Those numbers are in the same neighborhood as what the amyloid antibodies do — for a drug that works through a completely different mechanism, in patients who had never received an amyloid drug.

The biomarker side was even more definitive. Total tau in cerebrospinal fluid dropped by fifty to sixty-five percent across all three doses. Tau on PET imaging, which is a direct measurement of pathological tau in the brain, declined across every brain region and every dose group. So the drug is clearly, unambiguously reducing tau burden. It is just that more reduction did not equal more clinical benefit.

Why the paradox? Nobody knows for sure. The Biogen line is that this is dose-plateau behavior — the low dose is already saturating the therapeutic window and the higher doses are just adding tau reduction without added cognitive translation. There are also mechanistic questions about whether extremely aggressive tau reduction might interfere with normal tau function in ways that offset the benefit. Both are guesses. The honest answer is that this needs Phase 3 to sort out, and Biogen has said they're moving to Phase 3 based on the CELIA data.

Why it matters. Every anti-tau program up to now — passive antibodies, active vaccines, small-molecule inhibitors of tau aggregation — has failed to show a cognitive signal in a Phase 2 or Phase 3 Alzheimer's trial. This is, arguably, the first credible anti-tau positive signal from a randomized clinical trial. It doesn't mean the drug is going to be approved next year — a Phase 3 confirmatory trial is a real risk given the primary-endpoint miss, and dose-selection for that trial is going to be a genuinely hard call. But it does mean the tau hypothesis is, for the first time, showing signs of translating from biomarker to bedside. Combined with yesterday's Eisai etalanetug biomarker data on a completely different anti-tau mechanism, and the ongoing combination-therapy trials with the amyloid drugs, this is the most action anti-tau has ever had in the Alzheimer's clinic. Long overdue, but here.

---

Also on the business side, and briefly. AstraZeneca yesterday agreed to pay Dizal Pharmaceuticals up to one and a half billion U.S. dollars in a licensing deal — six hundred million upfront, up to nine hundred million in milestones, plus tiered royalties — for the ex-China global rights to a small-molecule lung cancer drug called Zegfrovy. The generic name is sunvozertinib. Dizal is a Shanghai-based biotech; this deal moves the drug's global commercial rights outside of China to AstraZeneca.

The context. Zegfrovy is what oncologists call an EGFR TKI — an epidermal growth factor receptor tyrosine kinase inhibitor. EGFR is a receptor on the surface of cells that, when it binds to a growth factor, tells the cell to divide. In many lung adenocarcinomas — the largest subtype of non-small cell lung cancer — the EGFR gene is mutated in a way that makes the receptor constitutively active, so the cell divides even without a signal. TKIs are small-molecule pills that block the kinase activity of that receptor from the inside.

The problem is that not all EGFR-mutant lung cancer is the same. The classical mutations, in exons nineteen and twenty-one, respond well to the standard-of-care TKI osimertinib, which happens to be AstraZeneca's biggest oncology drug. But there's a smaller subset — around ten percent of EGFR-mutant non-small cell lung cancer — whose tumors carry a mutation called an exon twenty insertion. Those tumors do not respond to osimertinib. And until recently, no oral drug worked well against them. Patients were left with chemotherapy and, later, an intravenous biologic called amivantamab.

Zegfrovy is the first oral drug approved specifically for exon twenty insertion mutations. It has full approval in China and accelerated approval in the U.S. as of two years ago. Both agencies have granted it Breakthrough Therapy Designation for the more lucrative first-line setting — meaning use before chemotherapy — and that expansion is pending. The commercial argument for AstraZeneca is clean. They already own most of the EGFR-mutant lung cancer market with osimertinib; Zegfrovy plugs the exon twenty gap. That gives them essentially the full oral EGFR field in one portfolio.

The larger point about this deal is that it's part of a broader pattern of Chinese biotech assets moving to Western majors. Chinese drug development has caught up to the point where its Phase 2 and Phase 3 data are increasingly credible; Chinese companies often don't have the global commercial infrastructure to launch their own drugs in the U.S. and Europe; so what you see, in ever larger numbers, are deals like this. AstraZeneca, Merck, GSK, and others have all done big in-licensing deals with Chinese biotechs in the last eighteen months. Six hundred million dollars upfront for a de-risked, Phase 3-ready oncology drug is roughly the going rate.

---

And finally, animals.

A study out yesterday in Nature Chemical Biology, from a group at University College London working with the Institute of Zoology and Imperial College London, tells us how some frogs are surviving what should have been an extinction event.

The context. Since about the nineteen nineties, amphibians around the world — frogs, toads, salamanders — have been dying in staggering numbers from a fungal disease called chytridiomycosis. The fungus is called Batrachochytrium dendrobatidis, or Bd for short. Bd infects amphibian skin. Amphibians breathe partly through their skin and regulate their salt and water balance through it, so when the fungus takes over the skin, they lose electrolyte balance and eventually go into cardiac failure. Bd has driven around ninety species of amphibians to extinction and pushed hundreds more to the brink. It is the worst infectious wildlife disease event ever recorded.

But something odd has been happening in the last decade or so. In many hard-hit places — including in the Pyrenees — some populations have been recovering. Not because Bd is gone. Bd is still there. But because the animals in those populations have found some way to survive it.

The UCL group, led by Phillip Jervis with senior author Alethea Tabor, studied common midwife toads at four lakes in the Pyrenees along the French–Spanish border. One lake population is still crashing. The other three have recovered. All four lakes have Bd. So they asked: what is different about the toads?

The answer is what happens on the skin, and specifically when. Frog and toad skin, like human skin, is home to a set of naturally produced antimicrobial peptides — short protein-like molecules that punch holes in bacterial and fungal cell membranes. Different amphibian species and populations make different peptides. And it turns out that toads at the surviving lakes make a very different, and much richer, set of antimicrobial peptides than the toads at the crashing lake.

The interesting part is timing. In amphibians, the skin changes fundamentally at metamorphosis — the moment a tadpole becomes a small toad. Tadpoles have soft, non-keratinized skin that Bd can't infect. Adult toads have hard, keratin-rich skin that Bd loves. The moment of metamorphosis is when the toads become vulnerable. And what the UCL group showed is that the surviving toads have already built up their antimicrobial peptide arsenal in the tadpole stage — before Bd can grab them. So by the time metamorphosis happens and the vulnerable skin appears, the immune shield is already deployed and running. The toads at the crashing lake, in contrast, don't build that shield until much later, and by then, Bd is already established on their skin.

There's a bonus finding. They catalogued one thousand one hundred fifty-two distinct antimicrobial peptides in these toad populations. Only seven had ever been described before. In other words, an entire hidden library of previously unknown antimicrobial molecules, evolved by natural selection to survive one of the most aggressive fungal pathogens known. Some of those peptides might be useful starting points for human antifungal drugs, at a moment when we don't have many. So a story about which frogs get to live has become, incidentally, a lead on where the next generation of antimicrobial drugs might come from.

That's the show for Wednesday, July fifteenth. Thanks for listening.
