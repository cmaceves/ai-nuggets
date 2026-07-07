## Script

Paper link: https://www.biorxiv.org/content/10.64898/2026.07.05.736580v1
Paper link: https://cdn.who.int/media/docs/default-source/_sage-2026/multi-country-outbreak-of-mpox--external-situation-report_66.pdf
Paper link: https://ir.veratx.com/news-releases/news-release-details/vera-therapeutics-announces-us-fda-granted-priority-review
Paper link: https://www.biorxiv.org/content/10.64898/2026.07.03.736267v1
Paper link: https://www.sciencedaily.com/releases/2026/06/260625060216.htm

Good morning, and welcome to The Genome Brief for Tuesday, July seventh. Today: a preprint from Glasgow settles a three-year debate about what gives Omicron its upper-airway preference — and the mechanism is not the one most scientists assumed. Mpox clade Ib has established itself in Madagascar, now the most active mpox outbreak country in Africa, with exportations already reaching the Indian Ocean islands. Today is the FDA's decision deadline for atacicept in IgA nephropathy, the first drug candidate to block both cytokines driving this autoimmune kidney disease. A City University of Hong Kong AI tool annotates the dark matter of viral genomes using the scientific literature itself as its evidence base. And finally: twenty thousand years ago in a Caribbean cave, solitary bees made their nurseries inside the empty tooth sockets of bones left behind by owls — and we have the fossils.

Let's start with SARS cov two, and a paper that rewrites the standard explanation for how Omicron came to prefer the upper airway.

Omicron lineages infect predominantly the nose and throat rather than the deep lungs. That shift lowered the severity of infections dramatically compared to Delta and earlier variants, because it means less pneumonia. For the past three years, the leading explanation for this tissue preference focused on a specific spike protein mutation called H655Y — a swap from the amino acid histidine to tyrosine at position 655 of the spike.

H655Y was thought to explain the upper-airway preference through a chain of logic about how the virus enters cells. SARS cov two's spike protein, after binding to the ACE2 receptor on a host cell, needs to be cleaved by a host enzyme to trigger cell entry. Two proteases can do this. TMPRSS2, sitting on the outer surface of cells and abundant in the lower lung, enables rapid entry right at the cell membrane. Cathepsin L, found inside the cell's acidic recycling compartments, enables entry only after the virus is taken up by the cell first. Pre-Omicron variants preferred TMPRSS2 and thrived in the lower lung. Omicron variants became more dependent on cathepsins, which are more available in upper-airway tissues. And H655Y was credited as the driver of that switch — reduce TMPRSS2-mediated entry, lose the lower-lung advantage.

A preprint from the MRC-University of Glasgow Centre for Virus Research, posted this week, puts that story to a systematic test with thirteen spike proteins spanning the full variant timeline. Their finding: protease preference and tissue tropism are mechanistically uncoupled. H655Y does shift the virus toward cathepsin-dependent entry — that part of the old story is confirmed. But H655Y does not determine where in the body the virus replicates. The decisive factor turns out to be the receptor-binding domain — the part of the spike that directly contacts ACE2. Mutations in that domain from the BA.2.86 variant override the H655Y effect entirely: a virus with BA.2.86's receptor-binding domain adopts Omicron-like upper-airway tropism regardless of whether H655Y is present.

The two features evolved along separate tracks. For surveillance, this means tracking H655Y tells you about protease usage but won't predict tissue tropism. The receptor-binding domain mutations are the relevant axis to watch for understanding where a new variant will replicate.

On the pathogen watch front, an update on mpox that the show hasn't yet covered: the Indian Ocean expansion of clade Ib.

Mpox comes in two major clades. Clade II drove the global outbreak that peaked in 2022. Clade Ib — the fast-spreading subgroup that emerged in eastern DRC around 2024 — has been moving across East and Central Africa via sexual and household transmission.

What's striking is the new geography. Madagascar — an island nation of roughly thirty million people with historically no endemic mpox — first confirmed clade Ib cases in January 2026 in people with no recent travel history, meaning the virus had already seeded local transmission before it was detected.

According to the most recent WHO situation report, covering data through mid-May 2026, Madagascar reported 780 confirmed mpox cases in a six-week window spanning early April through mid-May. That is more than any other country in Africa during that period — including the DRC, which is almost certainly undercounting because its surveillance capacity is stretched thin by the concurrent Bundibugyo Ebola outbreak. Madagascar also seeded exportations: Mauritius confirmed two clade Ib cases in April linked to travel from Madagascar; Réunion has also reported cases. On the African mainland, South Sudan has seen a sudden jump in clade Ib with ongoing geographic expansion outside Juba.

One feature of clade Ib that distinguishes it from the 2022 global outbreak: it doesn't stay confined to sexual networks. Clade Ib also transmits through household contacts including children, much more like the dynamics of the original endemic clade Ia in Central Africa. That broader transmission range, combined with Madagascar's limited healthcare infrastructure, is why this situation is an active WHO response priority.

On the business side, today is the FDA's PDUFA date — the decision deadline — for atacicept, the lead drug from Vera Therapeutics, for adults with IgA nephropathy.

IgA nephropathy is the most common primary glomerulonephritis worldwide — meaning the most common immune-mediated kidney disease that arises on its own without another underlying condition. The glomeruli are the tiny capillary knots in the kidney where blood filtration happens. In IgA nephropathy, B cells produce structurally abnormal IgA1 antibodies — the sugar chains attached to them are incomplete. These malformed molecules form aggregates that deposit in the glomeruli, triggering chronic inflammation that scars the filtering tissue over years to decades. About 20 to 40 percent of patients eventually reach kidney failure.

Two cytokines drive the abnormal B cell behavior: BAFF — B-cell activating factor — and APRIL — A PRoliferation-Inducing Ligand. Both promote B cell survival and the class switching that produces IgA. Both are elevated in IgA nephropathy patients. Atacicept is a fusion protein that simultaneously blocks both, acting as a decoy receptor that mops up both cytokines before they can reach B cells. The dual blockade is the pharmacological key: either cytokine alone can sustain the disease, so blocking only one is not enough.

The pivotal Phase 3 ORIGIN 3 trial showed a 46% reduction from baseline in proteinuria — the protein leakage into urine that marks kidney damage — with a 42% placebo-adjusted reduction, published in the New England Journal of Medicine. Vera Therapeutics applied for accelerated approval using proteinuria as the surrogate endpoint, with full approval based on kidney filtration data expected in 2027. The drug has Breakthrough Therapy Designation and Priority Review status. If approved today, atacicept would be the first drug for IgA nephropathy to target the disease at the B cell cytokine level — mechanistically distinct from all existing therapies.

In AI-in-biomedicine news, a preprint this week from City University of Hong Kong describes VirProtRAG: a system for annotating viral protein functions using retrieval-augmented generation.

The problem is the viral dark matter problem. When you sequence a new virus and look at its protein sequences to understand what the virus does, a large fraction come back labeled "hypothetical protein" or "unknown function." Traditional annotation compares new sequences to known ones and infers function by similarity — it fails when a protein is genuinely novel or only distantly related to anything characterized.

VirProtRAG uses a different approach. Given a viral protein of unknown function, it retrieves the most relevant passages from the scientific literature — combining keyword search and semantic vector search — and generates a functional annotation explicitly grounded in those documents. Each annotation comes with the supporting literature, so a virologist can judge the quality of each call. Applied to all 17,484 reviewed viral proteins in Swiss-Prot, the system added new non-overlapping functional annotations for about a third beyond existing expert curation. For metagenomics surveillance, this means annotating a novel pathogen's proteome now yields not just functional guesses but traceable citations — a meaningful improvement over unlabeled unknowns.

And finally, animals — and a piece of natural history from the Caribbean that I find genuinely delightful.

In a limestone cave in Hispaniola — the island shared by Haiti and the Dominican Republic — researchers have documented what is apparently the first known case of bees using animal bones as nesting sites. Specifically, the empty tooth sockets of mammal jawbones left behind by owls.

Owls have been roosting in this cave for tens of thousands of years, swallowing prey whole and regurgitating the bones and fur as compact pellets that accumulated on the cave floor. The bones of rodents and small sloths that owls consumed were left exposed on the rocky limestone surface.

Solitary bees — which, unlike honeybees, build individual nesting cells for each larva rather than communal hives — discovered that the concave, smooth interiors of empty tooth sockets were a perfect fit for a larval chamber. Researchers examining cave sediments found the fossil nests still intact: tiny cup-shaped structures inside rodent and sloth jawbones, now formally named Osnidum almontei. The findings were published in Royal Society Open Science.

In a limestone landscape with almost no soil for ground nesting, the bees adapted to the available material: a cave floor full of owl-donated jawbones. The ecological relay here — owl hunting, pellet deposition, bone weathering, bee colonization — is the kind of chain that produces a behavior no one would have predicted to look for. Twenty thousand years on, the fossils found it for us.

That's The Genome Brief for July seventh. We'll be back tomorrow.
