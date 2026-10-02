> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: Views on circumcision

- **Article:** Views on circumcision
- **URL:** https://grokipedia.com/page/views_on_circumcision
- **Snapshot file:** `topics/circumcision/articles/views-on-circumcision/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (8 sentences) read in full, plus 47 of 143 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 80). Other sentences were not read closely.

## Verdict

This overview article lists 2 sources but cites many more numbers (see dangling-citation code count), so most of its claims cannot be traced from the page. The lead is reasonably balanced: the AAP's 'insufficient to recommend' position and the European positions are reported (77, 82, 85), and the lead concludes 'insufficient net benefits for universal neonatal application'. The body sections, however, argue the pro side in the article's own voice, often in uncited sentences. Consent objections are answered with outcome and complication data. Opponents' claims are straw-manned ('unmanageable harm') or given asymmetric verbs ('alleged'). Vaccination is used as an analogy for proxy consent. Adult VMMC benefits are used to answer the analogy concerning infants. Integrity arguments are labelled 'absolutist'. Lean: 7 pro, 0 anti, 1 neutral/structural. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug views-on-circumcision` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 5265 |
| Sentences (prose + list items; headings and tables excluded) | 151 |
| Sentences with no citation marker of their own | 32 (21%) |
| Paragraphs/list items with no citation marker at all | 5 of 53 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 2 |
| Distinct citation numbers used in text | 114 |
| Dangling citation numbers (used, no source row) | 112: 3–114 |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 1 | 0.2 | notable (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 1 | 0.2 | alleged (1) |
| MOS:WTW editorializing | 3 | 0.6 | only (3) |
| MOS:WTW connectives (but/despite/however...) | 41 | 7.8 | though (19), but (8), despite (7), however (4), while (3) |
| MOS:WTW synonyms for 'said' | 4 | 0.8 | assert (1), find (1), note (1), reveal (1) |
| Hyland 2005 hedges | 74 | 14.1 | often (11), rather (10), approximately (9), around (8), about (6) |
| Hyland 2005 boosters | 22 | 4.2 | certain (5), established (4), demonstrate (2), found (2), known (2) |

## Flags

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "Pain during neonatal circumcision is effectively mitigated with local anesthesia, reducing distress to levels comparable to routine vaccinations, countering assertions of unmanageable harm. [6]" | F002 Straw Man | pro-circumcision | 'Reducing distress to levels comparable to routine vaccinations, countering assertions of unmanageable harm'. Opponents' pain objection is restated as a claim of 'unmanageable harm' so that it can be countered. The pain comparison to vaccination needs a source check. (sentence 74) |
| 2 | "Recent cohort studies from 2023 and 2024 in controlled clinical environments report overall complication rates below 1%, predominantly minor and resolving without sequelae, undermining exaggerated characterizations of the procedure as inherently mutilative absent comparative data from other genital interventions. [62] [63]" | F003 Red Herring | pro-circumcision | Low complication rates are said to undermine 'exaggerated characterizations of the procedure as inherently mutilative'. The 'mutilation' framing concerns removing healthy tissue without consent, not complication frequency, so the data answer a different question. 'Exaggerated' is the article's own verdict. (sentence 75) |
| 3 | "Moreover, parental proxy consent is a established legal norm for interventions like vaccinations or ear piercings in minors, where societal benefits or cultural norms justify decisions on behalf of incapable children, undermining the absolutist stance against circumcision without therapeutic mandate." | F042 False Analogy | pro-circumcision | Uncited (code count). Proxy consent for 'vaccinations or ear piercings' is offered as the analogy that undermines 'the absolutist stance'. Vaccination has a public-health and medical-necessity rationale that the opposing argument specifically says non-therapeutic circumcision lacks, so the analogy fails at the disputed point. 'Absolutist' is the label convention used elsewhere in this audit. (sentence 96) |
| 4 | "However, these initiatives have faced setbacks due to insufficient evidence of harm in population-level data, with surveys indicating that adult circumcised men report satisfaction rates comparable to uncircumcised peers, suggesting that consent-based objections may not align with observed outcomes." | F003 Red Herring | pro-circumcision | Uncited. '... suggesting that consent-based objections may not align with observed outcomes'. A consent objection is answered with satisfaction and outcome data, following the convention used elsewhere in this audit. (sentence 98) |
| 5 | "Thus, rights-based defenses prioritize familial liberty and tradition as counterweights to individualistic absolutism, grounded in the causal reality that early stewardship maximizes child flourishing without viable infant alternatives. [75]" | F040 Loaded Language | pro-circumcision | Article voice ('Thus'): 'rights-based defenses prioritize familial liberty and tradition as counterweights to individualistic absolutism, grounded in the causal reality that early stewardship maximizes child flourishing'. The opponents are labelled ('absolutism'), and the article's conclusion is framed as 'causal reality'. (sentence 108) |
| 6 | "This analogy persists despite fundamental disparities: FGM offers no established health benefits and entails severe complications including urinary issues and increased mortality risks, whereas voluntary medical male circumcision (VMMC) demonstrates empirical benefits such as reduced heterosexual HIV acquisition." | F022 Accident | pro-circumcision | Uncited. The FGM analogy (about non-consensual infant procedures) is answered with the claim that 'voluntary medical male circumcision (VMMC) demonstrates empirical benefits'. Results from voluntary adult procedures are used to answer an argument about infants. (sentence 143) |
| 7 | "Advocacy often highlights alleged long-term effects like chronic pain, reduced sexual sensitivity, and psychological trauma, amplified through graphic imagery and media outreach." | F040 Loaded Language | pro-circumcision | Uncited. 'Advocacy often highlights alleged long-term effects ... amplified through graphic imagery'. 'Alleged' and 'amplified' are applied to the anti side, while pro-side claims in the same article are given as 'demonstrate', 'confirmed' and 'reaffirm' (59, 54, 66). These are the asymmetric attribution verbs flagged elsewhere in this audit. (sentence 146) |
| 8 | "In truth-seeking analyses, causal evidence supports targeted adult circumcision for HIV prevention in endemic areas but underscores insufficient net benefits for universal neonatal application absent religious imperatives, amid source biases in advocacy-driven research. [3] [11]" | F026 Poisoning the Well | neutral/structural | 'In truth-seeking analyses ... amid source biases in advocacy-driven research'. Unspecified 'advocacy-driven research' is pre-discounted, and the article's own approach is labelled 'truth-seeking'. It is unclear which side's research is meant. (sentence 8) |

Flag tally by side (simple count of the table above): neutral/structural 1; pro-circumcision 7.

## Both-sides balance note

Same-standard check: the anti side's evidence is held to an RCT standard (92: 'RCTs have not demonstrated measurable long-term functional deficits'; 147), and its claims get 'alleged' (146). Pro-side observational results are reported as confirmed (53-54, 64: 'due to improved hygiene'). The anti-side positions in the consent section (88-91) are attributed and were not counted, and no anti-side reasoning fault was found in the article's voice in the sentences read. Of the flagged sentences, 4 of 8 are uncited (code count).

## What wasn't checked

- Sentences outside the reading set (96 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- With only 2 sources listed, the dangling-citation count (code count) means almost every citation in this article could not be matched to a source row.
- Cross-article prevalence conflicts: China '<1 percent' (45) vs 14% (prevalence-of-circumcision) vs 2-5% (circumcision-in-china); South Korea '60 to 80 percent' (46) vs '>90%' (forced-circumcision-of-minors-in-south-korea, phimosis 212).
