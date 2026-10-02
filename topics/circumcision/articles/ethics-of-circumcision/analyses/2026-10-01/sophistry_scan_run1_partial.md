> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: Ethics of circumcision

- **Article:** Ethics of circumcision
- **URL:** https://grokipedia.com/page/Ethics_of_circumcision
- **Snapshot file:** `topics/circumcision/articles/ethics-of-circumcision/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (8 sentences) read in full, plus 77 of 234 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 80). Other sentences were not read closely.

## Verdict

The lead is balanced, and its closing sentence even calls the benefits 'context-specific and often marginal'. But much of the body argues the pro-circumcision case in the article's own voice, often under neutral-sounding headings ('Application of Harm Principle', 'Human Rights Frameworks'). Many of those sentences are uncited. The pattern of moves: analogies to heel-stick screening and vaccines without matching the relevant features; the FGM comparison relabelled as a 'slippery slope' argument; harm, trauma and regret evidence discounted as 'unsubstantiated', 'advocacy-driven' or 'hypothetical'; observational UTI and cancer data described as 'high-quality RCTs'; continuity 'validated' because no harm has been demonstrated; and European practice linked to ancient anti-Jewish bans. Critical positions (KNMG, BMA, AMA Journal of Ethics) are reported but each is followed by a rebuttal. On the sentences read, all 11 flags favor pro-circumcision; no article-voice anti-circumcision reasoning fault was found. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug ethics-of-circumcision` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 8954 |
| Sentences (prose + list items; headings and tables excluded) | 242 |
| Sentences with no citation marker of their own | 43 (18%) |
| Paragraphs/list items with no citation marker at all | 0 of 92 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 187 |
| Distinct citation numbers used in text | 187 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 2 | 0.2 | celebrated (1), notable (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 6 | 0.7 | only (6) |
| MOS:WTW connectives (but/despite/however...) | 65 | 7.3 | while (20), but (19), though (15), despite (7), however (4) |
| MOS:WTW synonyms for 'said' | 9 | 1.0 | find (4), confirm (2), reveal (2), note (1) |
| Hyland 2005 hedges | 99 | 11.1 | approximately (12), often (12), rather (11), indicate (8), typically (7) |
| Hyland 2005 boosters | 47 | 5.2 | certain (8), found (5), show (5), demonstrate (4), established (4) |

## Flags

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "These findings counter unsubstantiated assertions of harm, as lower-quality self-report studies showing differences often suffer from recall bias or confounding factors like cultural attitudes, whereas objective measures (e.g., histological sensitivity assessments) indicate preserved or enhanced penile nerve density in circumcised men. [46]" | F026 Poisoning the Well | pro-circumcision | Pre-labels contrary findings as 'unsubstantiated assertions of harm' and the studies behind them as 'lower-quality self-report studies', so they are discounted by category. The counter-claim ('preserved or enhanced penile nerve density') needs a source check. (sentence 56) |
| 2 | "This framework privileges verifiable causal benefits—such as infection risk mitigation—over hypothetical future regrets, which surveys indicate affect a minority of parents regardless of choice. [63]" | F073 McNamara Fallacy | pro-circumcision | 'Privileges verifiable causal benefits ... over hypothetical future regrets' means what is measured counts and the unmeasured personal outcome is discounted as 'hypothetical'. (sentence 73) |
| 3 | "These causal data from high-quality RCTs and meta-analyses establish an empirical threshold where harms—primarily acute pain and rare complications—do not predominate, precluding classification as net harm absent context-specific override (e.g., negligible HIV risk environments still yield marginal gains from non-HIV outcomes)." | F036 Suppressed Evidence | pro-circumcision | Uncited. Calls the UTI and penile cancer data 'high-quality RCTs and meta-analyses', but sentence 108 says the UTI figure comes from 'meta-analyses of observational studies'. The evidence base is overstated in the sentence that draws the conclusion. (sentence 77) |
| 4 | "Critiques framing infant circumcision as inherently non-therapeutic, thus presumptively harmful, falter against precedents in preventive pediatric medicine, where procedures like heel-stick blood sampling for newborn metabolic screening inflict comparable or greater procedural pain yet are standard due to utility in averting conditions like phenylketonuria, which untreated causes intellectual disability in 1:10,000-15,000 births. [67]" | F042 False Analogy | pro-circumcision | Heel-stick screening is offered as precedent: it is painful, yet standard. But screening is diagnostic, removes no tissue, and targets conditions that cause harm in infancy. The features that make it acceptable are not shown to carry over to circumcision. (sentence 78) |
| 5 | "Slippery slope arguments equating male circumcision to female genital mutilation (FGM) lack evidential parity, as FGM confers no documented health benefits and correlates with increased risks of urinary issues, sexual dysfunction, and obstetric complications (e.g., postpartum hemorrhage odds ratio 1.3-1.55), per WHO classifications of Types I-III. [70] [71]" | F002 Straw Man | pro-circumcision | Relabels the FGM comparison (sentence 62: a consent/bodily-integrity parity argument) as 'slippery slope arguments' and then rebuts it on health outcomes. The opposing argument is misdescribed before it is answered. (sentence 81) |
| 6 | "This environmental causality underscores how cultural persistence can embody practical responses to historical exigencies, validating continuity where no overriding harm is empirically demonstrated. [108]" | F010 Appeal to Ignorance | pro-circumcision | 'Validating continuity where no overriding harm is empirically demonstrated': the absence of demonstrated harm is treated as positive validation of the practice. (sentence 123) |
| 7 | "However, this framing overlooks its preventive classification in contexts analogous to vaccines, where interventions target rare but severe outcomes with net benefits; for instance, systematic reviews affirm circumcision reduces UTI risk by 90% in infancy and heterosexual HIV acquisition by 50-60% based on randomized controlled trials (RCTs) in high-prevalence settings, benefits that scale population-wide despite low baseline risks. [1] [125] [8]" | F042 False Analogy | pro-circumcision | 'Contexts analogous to vaccines': vaccines protect against communicable disease during childhood. The main benefit cited (adult heterosexual HIV in high-prevalence settings) arises after the age of consent, which is the feature critics point to. (sentence 145) |
| 8 | "Lower circumcision prevalence in Europe (typically under 20%, except among immigrant Muslim populations) is often cited as evidence of non-necessity, yet this reflects historical and cultural norms—such as post-World War II abandonment in the UK and bans linked to anti-Jewish sentiments in antiquity—rather than superior medical outcomes; European nations exhibit comparable disease rates to high-circumcision regions when adjusted for hygiene and behavior, and some analyses urge reconsideration given universal benefits like reduced human papillomavirus (HPV) persistence. [128] [129] [32]" | F025 Guilt by Association | pro-circumcision | Explains lower European prevalence partly by 'bans linked to anti-Jewish sentiments in antiquity', associating the non-circumcising side with antisemitism without connecting that history to current European medical positions. Also asserts 'universal benefits', which conflicts with the lead's 'context-specific'. (sentence 147) |
| 9 | "Claims of delayed trauma, often from advocacy-driven surveys or small non-randomized cohorts, fail replication in rigorous designs and overlook confounders like cultural context or self-selection bias. [138]" | F026 Poisoning the Well | pro-circumcision | Trauma claims are introduced as 'often from advocacy-driven surveys', which discounts them by origin before their methods are discussed. (sentence 154) |
| 10 | "This evidence prioritizes causal efficacy over deferred choice, as adult uptake failures undermine preventive efficacy." | F061 Is-Ought Jump | pro-circumcision | Uncited. From 'adult uptake failures' to 'prioritizes causal efficacy over deferred choice'. That informed adults often decline is treated as a failure to be prevented by deciding in infancy, with no normative premise for overriding the choice adults would make. (sentence 180) |
| 11 | "Absolutist claims equating male circumcision to mutilation overlook data showing complication rates below 0.5% in hospital settings versus higher non-medical ritual risks, and fail to account for evolutionary and physiological roles of the foreskin that, while sensitive, do not preclude overall utility in disease prevention." | F040 Loaded Language | pro-circumcision | Uncited. Opposing views are labelled 'absolutist claims' (and in sentence 228, also uncited, 'ideological purity'). The answer given (low hospital complication rates) does not meet the consent and equivalence argument it labels. (sentence 229) |

Flag tally by side (simple count of the table above): pro-circumcision 11.

## Both-sides balance note

Same-standard check: the anti-circumcision positions are attributed ('opponents contend', 'intactivist perspectives', named bodies) and are generally followed by rebuttals, while pro-circumcision positions are often stated in the article's own voice without a following rebuttal (73-82, 123, 145-147, 175-180, 222-229). Evidence standards differ: self-report and survey evidence of harm is discounted (56, 154), while 'surveys indicate' is used to minimize regret (73). The lead's sentence 6 mentions 'institutional biases' on the pro side as a controversy; that is the anti side's comparable framing, and it is presented as a topic of debate rather than asserted, so it was not flagged. Shortfall: the 'Critiques and Contextual Limitations' section (202-210) is the only place where pro-side claims are scrutinized, and it is shorter than the pro-side sections in the sentences read.

## What wasn't checked

- Sentences outside the reading set (157 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- Sentence 52 ('phimosis (affecting up to 1 in 2 uncircumcised males lifetime)') and sentence 80 (16% US lifetime HIV reduction modeling) need source checks.
