> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: Female genital mutilation

- **Article:** Female genital mutilation
- **URL:** https://grokipedia.com/page/female_genital_mutilation
- **Snapshot file:** `articles/female-genital-mutilation/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (8 sentences) read in full, plus 45 of 283 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This is a long overview, and structurally its sourcing is broken: the page lists 3 sources but cites up to [76], leaving 73 dangling citation numbers (code count), so almost nothing in it can be traced. On reasoning, the treatment of FGM's harms is mostly evidence-based, with some causal overstatement. The comparison sections defend the male/female distinction by replying with Type III severity and with severity in general to arguments about milder types and about consent. Elsewhere, the article discounts trauma data as coming from 'advocacy-influenced surveys'. Lean: 3 pro-circumcision (pro-cutting or pro-distinction), 3 anti, 1 neutral/structural. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug female-genital-mutilation` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 9833 |
| Sentences (prose + list items; headings and tables excluded) | 291 |
| Sentences with no citation marker of their own | 134 (46%) |
| Paragraphs/list items with no citation marker at all | 31 of 88 |
| Table rows (not counted as sentences) | 10 |
| Sources listed in sources CSV | 3 |
| Distinct citation numbers used in text | 76 |
| Dangling citation numbers (used, no source row) | 73: 4–76 |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 3 | 0.3 | honorable (3) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 1 | 0.1 | officially (1) |
| MOS:WTW expressions of doubt | 6 | 0.6 | purported (4), accused (1), alleged (1) |
| MOS:WTW editorializing | 5 | 0.5 | only (5) |
| MOS:WTW connectives (but/despite/however...) | 91 | 9.3 | but (29), though (22), while (22), despite (15), however (3) |
| MOS:WTW synonyms for 'said' | 11 | 1.1 | note (4), reveal (4), find (2), assert (1) |
| Hyland 2005 hedges | 119 | 12.1 | often (34), rather (19), indicate (8), around (6), claims (6) |
| Hyland 2005 boosters | 33 | 3.4 | certain (8), found (7), known (4), show (3), find (2) |

## Flags

Side labels: the task's three labels are kept. In this article, which is mainly about female genital cutting, 'pro-circumcision' marks a flag whose reasoning makes genital cutting (or male circumcision, where it is compared) look more acceptable or benign, or makes its critics look less credible. 'anti-circumcision' marks a flag whose reasoning makes genital cutting look worse or its defenders less credible. 'neutral/structural' marks flags that favor neither.

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "Critics, often anthropologists or community representatives from practicing regions, argue "mutilation" imposes cultural bias, equating varied practices (from pricking to excision) under a condemnatory label that impedes eradication efforts by alienating locals; they favor FGC for its descriptive neutrality, as endorsed by some UNICEF campaigns since 2008 to promote intra-community dialogue. [11] [12]" | F056 Exception Fallacy | pro-circumcision | The ethicists' critique concerns how 'all forms' of FGM are labelled compared with male circumcision. The reply cites 'up to 80%' tissue loss 'in Type III', the most extensive form, to justify the distinction for the whole category, including pricking and prepuce-only cuts. (sentence 14) |
| 2 | "However, empirical evidence highlights fundamental differences in procedure, health outcomes, and functional impacts, rendering the practices non-equivalent in severity." | F003 Red Herring | pro-circumcision | Uncited (code count). The claim answered (sentence 268) is that both are 'non-consensual genital cutting of minors', a consent-parity argument. The reply ('non-equivalent in severity') addresses severity, which the parity argument does not rest on. (sentence 269) |
| 3 | "Psychological trauma, manifesting as PTSD symptoms, has been observed in longitudinal studies of survivors, though data quality varies due to underreporting in biased self-reports from advocacy-influenced surveys." | F026 Poisoning the Well | pro-circumcision | Uncited. Discounts PTSD evidence because of 'biased self-reports from advocacy-influenced surveys'. Survivors' reports are pre-labelled by their supposed origin, which minimizes the harm evidence. (sentence 63) |
| 4 | "These outcomes correlate with anatomical damage—such as clitoral excision and infibulation scarring—causally impairing nerve function and vaginal elasticity, though self-reported data may confound cultural stigma with physiological limits." | F032 Cum Hoc | anti-circumcision | Uncited. 'Correlate with anatomical damage ... causally impairing nerve function': correlation and causation in the same breath. Sentence 180 itself urges 'cautious inference' because of confounding. (sentence 177) |
| 5 | "Variations include sunna circumcision, which targets only the prepuce, and more extensive forms removing the entire glans; the former is sometimes defended as a minor ritual akin to male circumcision, but empirical evidence shows it impairs clitoral function regardless." | F011 Hasty Generalization | anti-circumcision | Uncited. 'Empirical evidence shows it impairs clitoral function regardless' applies a sweeping claim to prepuce-only 'sunna' cutting with no study named. The cited review in sentence 40 concerns 'partial clitoridectomy', not prepuce-only procedures. (sentence 38) |
| 6 | "While not prescribed by any major religion's doctrines, FGM persists across Muslim, Christian, and animist communities in practicing regions, often justified through misinterpreted religious or customary norms rather than explicit scriptural mandates. [5] [6]" | F040 Loaded Language | anti-circumcision | The article's own voice calls practitioners' religious justifications 'misinterpreted' norms. That is an evaluative verdict on religious interpretation, presented as description. (sentence 5) |
| 7 | "Overall, early colonial and missionary interventions prioritized symbolic condemnation over sustained eradication, often exacerbating local resistance without significantly reducing incidence, as evidenced by post-colonial surveys indicating persistence in 90% of Sudanese women by the 1960s." | F034 False Cause | neutral/structural | Uncited. Concludes that colonial interventions were 'exacerbating local resistance', with continued 90% prevalence as the evidence. Persistence shows the practice did not decline; it does not show the interventions made resistance worse. (sentence 213) |

Flag tally by side (simple count of the table above): anti-circumcision 3; neutral/structural 1; pro-circumcision 3.

## Both-sides balance note

Same-standard check: within this article, FGM harms are stated causally (160, 177), while pro-practice 'purported benefits' are held to a strict standard (185-190). That asymmetry is partly warranted by the evidence the article describes, and it is noted rather than counted except where a sentence itself conflicts (177 vs 180). On the male-circumcision comparison, the anti-distinction side ('hypocrisy', 279-288) and the pro-distinction side (14, 269-278) both get space. The pro-distinction replies tend to compare FGM's severe forms with male circumcision as a whole. The anti-distinction sentences use 'analogous' and the 'often without ... anesthetic' claim (280), which need source checks. Shortfall: with 73 of 76 citation numbers dangling, neither side's claims can be traced from this page.

## What wasn't checked

- Sentences outside the reading set (238 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- With 73 dangling citation numbers, no citation in this article could be matched to a source row; the 'sentences without own citation' count understates the sourcing problem.
