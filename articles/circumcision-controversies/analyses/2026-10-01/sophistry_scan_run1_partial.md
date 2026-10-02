> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: Circumcision controversies

- **Article:** Circumcision controversies
- **URL:** https://grokipedia.com/page/Circumcision_controversies
- **Snapshot file:** `articles/circumcision-controversies/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (4 sentences) read in full, plus 58 of 176 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 80). Other sentences were not read closely.

## Verdict

The lead is reasonably balanced. The body is not: a section headed 'Proven Health Benefits' and a 'Causal Reasoning from First Principles' section argue the pro-circumcision case in the article's own voice, and many of those sentences are uncited. That case leans on several weak moves. Proxy consent for circumcision is compared to vaccinations and orthodontics. Public-health gains are turned into a justification without a stated value premise. The deferral argument is restated as 'absolute deferral' and called 'incoherent'. Deontological objections are discounted openly ('when discounting deontological objections'). Self-report evidence is rejected when it shows harm but accepted when it shows equivalence. The anti side's main article-voice problem is one unattributed sentence asserting FGM parallels without the differences. On the sentences read, the flags lean pro-circumcision (13 of 15). These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug circumcision-controversies` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 6156 |
| Sentences (prose + list items; headings and tables excluded) | 180 |
| Sentences with no citation marker of their own | 42 (23%) |
| Paragraphs/list items with no citation marker at all | 5 of 62 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 153 |
| Distinct citation numbers used in text | 153 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 3 | 0.5 | prominent (1), unique (1), visionary (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 2 | 0.3 | alleged (1), purported (1) |
| MOS:WTW editorializing | 5 | 0.8 | only (3), notably (2) |
| MOS:WTW connectives (but/despite/however...) | 44 | 7.1 | but (17), though (11), while (10), despite (4), however (2) |
| MOS:WTW synonyms for 'said' | 3 | 0.5 | confirm (2), find (1) |
| Hyland 2005 hedges | 85 | 13.8 | often (14), claims (13), rather (11), approximately (10), indicate (8) |
| Hyland 2005 boosters | 25 | 4.1 | show (4), certain (3), demonstrate (3), established (3), found (3) |

## Flags

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "Neonatal circumcision nearly eliminates the risk in high-prevalence settings, as supported by epidemiological data linking uncircumcised status to higher incidence via phimosis and poor hygiene. [35]" | F032 Cum Hoc | pro-circumcision | 'Nearly eliminates the risk' is a causal claim drawn from 'epidemiological data linking' status to incidence: an association turned into a near-total causal effect. (sentence 34) |
| 2 | "Claims of sensitivity loss often stem from lower-quality retrospective surveys prone to recall bias, lacking empirical support from randomized or controlled designs. [43]" | F026 Poisoning the Well | pro-circumcision | Contrary evidence is characterized by its weakest form ('lower-quality retrospective surveys') and dismissed as a class. Sentence 46 reports a mapping study (Sorrells) in the same section that does not fit that description. (sentence 47) |
| 3 | "In high-risk African settings, VMMC interventions have demonstrated epidemiological causality through time-series declines in incidence post-uptake, exceeding expectations from behavioral interventions alone, whereas low-prevalence contexts like Europe show minimal marginal gains due to already subdued transmission dynamics. [56] [57]" | F031 Post Hoc | pro-circumcision | 'Demonstrated epidemiological causality through time-series declines in incidence post-uptake': declines after uptake are treated as proof of cause, and other concurrent interventions (ART scale-up, PrEP) are not addressed in the sentence. (sentence 57) |
| 4 | "High-quality evidence, including quantitative sensory testing, finds no significant overall difference in penile sensitivity between circumcised and uncircumcised men for stimuli relevant to sex, and no adverse effect on erectile function, orgasm ease, or sexual satisfaction for most men." | F004 Appeal to Authority | pro-circumcision | Uncited (code count). 'High-quality evidence ... finds no significant overall difference' rests on unnamed authority with no citation attached. (sentence 72) |
| 5 | "These claims, while highlighting procedural similarities, apply to infant contexts where long-term sensory or psychological harms are alleged but lack uniform empirical validation across cohorts. [62] [63]" | F003 Red Herring | pro-circumcision | The FGM-analogy argument (sentences 76-77) is about consent and consistency. The reply shifts to whether sensory harms have 'uniform empirical validation', which the consent argument does not depend on. 'Alleged' is also an MOS:WTW doubt term. (sentence 78) |
| 6 | "Parents exercise proxy consent for their minor children in medical decisions, including irreversible procedures such as vaccinations—which carry risks of rare but permanent neurological effects—and orthodontics, which permanently alter dental structure, based on a fiduciary duty to promote the child's long-term welfare amid incomplete information. [64] [65]" | F042 False Analogy | pro-circumcision | Article-voice analogy between proxy consent for circumcision and for vaccinations and orthodontics. Vaccination protects against communicable disease in childhood, and orthodontics is usually done with the adolescent's involvement. The analogy has no step showing those features carry over. (sentence 79) |
| 7 | "These effects extend to broader public health gains, including decreased healthcare burdens from preventable infections, justifying proxy interventions where net benefits accrue to dependents and society despite the child's inability to consent. [70]" | F061 Is-Ought Jump | pro-circumcision | Moves from public-health gains (sentence 83, largely from adult RCTs) to 'justifying proxy interventions ... despite the child's inability to consent' with no stated normative premise for overriding consent for societal benefit. (sentence 84) |
| 8 | "Infant claims to bodily autonomy falter on grounds of incompetence, as neonates lack capacity for rational deliberation or foresight, rendering absolute deferral to adulthood philosophically incoherent and practically suboptimal." | F002 Straw Man | pro-circumcision | Uncited. Restates the opposing view as 'absolute deferral to adulthood' and calls it 'philosophically incoherent'. Opponents (sentences 58-59) argue for deferring elective surgery, not all decisions. The infant's incompetence is their premise for deferral, not a refutation of it. (sentence 85) |
| 9 | "In low-prevalence contexts, these benefits accrue cumulatively over lifetime exposure, outweighing surgical risks when discounting deontological objections and focusing on empirical causality." | F073 McNamara Fallacy | pro-circumcision | Uncited. The conclusion that benefits outweigh risks is reached explicitly 'when discounting deontological objections and focusing on empirical causality': the unmeasured considerations are removed by assumption, not by argument. (sentence 95) |
| 10 | "Removal aligns the anatomy with contemporary sanitary realities, reducing these mismatches without invoking adaptive foresight, as natural selection operates on reproductive fitness, not post-hoc hygiene optimality. [78]" | F061 Is-Ought Jump | pro-circumcision | From a speculative evolutionary story (sentence 96, uncited; claim needs source check) to the evaluative conclusion that removal 'aligns the anatomy with contemporary sanitary realities'. This is an is-ought step, and a natural-mismatch narrative is used as warrant for surgery. (sentence 99) |
| 11 | "One study suggesting reduced penile sensitivity in circumcised groups relied on retrospective self-reports prone to recall bias and did not isolate causation from confounding factors like age or partner dynamics, failing to demonstrate downstream impacts on pleasure or function. [79]" | F036 Suppressed Evidence | pro-circumcision | Rejects a study for relying on 'retrospective self-reports', while sentence 101 accepts 'self-reported equivalence persisting across large cohorts' as evidence for the other side. The same evidence type is judged by different standards. (sentence 102) |
| 12 | "Prioritizing observable utilities over subjective proxies, the procedure's net causal effect favors reduced disease transmission over unsubstantiated pleasure deficits." | F073 McNamara Fallacy | pro-circumcision | Uncited. 'Prioritizing observable utilities over subjective proxies' decides that pleasure and sensation count less because they are harder to measure, then concludes 'net causal effect favors' the procedure. (sentence 104) |
| 13 | "U.S. studies also link higher circumcision rates to parents with greater education levels, who cite familiarity with evidence on preventive health outcomes like reduced urinary tract infections and certain STIs, countering narratives of inverse correlations in less informed populations. [127]" | F032 Cum Hoc | pro-circumcision | The correlation between parental education and circumcision rate is read as evidence-informed choice ('who cite familiarity with evidence') and used to counter other narratives. Confounders such as income, insurance and region are not addressed. (sentence 151) |
| 14 | "Circumcision controversies involve debates over the routine surgical removal of the foreskin from the penis of male infants and children, primarily for non-therapeutic reasons including religious, cultural, or purported preventive health benefits, which pit claims of modest medical advantages against concerns regarding procedural risks, ethical violations of bodily autonomy, and lack of informed consent from the minor. [1] [2]" | F040 Loaded Language | anti-circumcision | The lead's own 'purported preventive health benefits' (MOS:WTW expression of doubt) pre-judges the benefit claims that sentence 2 reports from AAP. (sentence 1) |
| 15 | "Analogies to female genital mutilation (FGM) underscore non-consensual parallels: both entail cultural or parental imposition of genital excision on minors, altering healthy anatomy without therapeutic imperative, yet FGM faces universal condemnation while male circumcision evades equivalent scrutiny." | F041 False Equivalence | anti-circumcision | Uncited and in the article's voice (unlike sentence 77, which attributes it). It asserts that FGM analogies 'underscore' parallels and that male circumcision 'evades equivalent scrutiny' without stating the differences in severity and type that the comparison would have to address. (sentence 76) |

Flag tally by side (simple count of the table above): anti-circumcision 2; pro-circumcision 13.

## Both-sides balance note

Same-standard check: the anti-circumcision case (sentences 58-62, 77, 160-161) is mostly attributed ('opponents contend', 'advocates argue', 'they contend'). The pro case in the 'Parental Rights' and 'Causal Reasoning from First Principles' sections is mostly unattributed article voice (79-85, 89-104), and many of those sentences are uncited. Evidence standards differ by side: anecdote and retrospective self-report are discounted when they suggest harm (47, 102, 164) but self-report is accepted when it suggests no harm (101). Section headings are not counted as sentences by the script, but the heading 'Proven Health Benefits' itself states a contested conclusion. Shortfall: the anti side has no section arguing its case in the article's own voice to match the 'First Principles' section; whether that is a reasoning fault or an editorial choice is a judgment call.

## What wasn't checked

- Sentences outside the reading set (118 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- Sentence 66 (uncited; Meissner's corpuscle density falling 'by up to 90% by middle age') and sentence 83 ('protecting uncircumcised partners') need source checks.
