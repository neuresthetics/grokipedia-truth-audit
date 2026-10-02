# Sophistry and fallacy scan: Female genital mutilation in the Gambia

- **Article:** Female genital mutilation in the Gambia
- **URL:** https://grokipedia.com/page/female_genital_mutilation_in_the_gambia
- **Snapshot file:** `articles/female-genital-mutilation-in-the-gambia/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (8 sentences) read in full, plus 38 of 114 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This is a mostly descriptive, survey-based article. It sets out defenders' arguments (rite of passage, religious obligation, likeness to male circumcision, sovereignty) in their own terms and attributes them, alongside the legal and campaign history. Two flags were found in the sentences read. One is in the lead: '77% of adverse neonatal outcomes' are linked to cut mothers in a population where about 73% of women are cut, so the figure means little without the base rate. The other is an uncited closing sentence that warns of 'Islamist influences' and cites a '2022 parliamentary push ... narrowly defeated'; elsewhere the article describes the repeal vote as a 2024 bill rejected 31-18. Lean: 0 pro, 1 anti, 1 neutral/structural. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug female-genital-mutilation-in-the-gambia` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 4226 |
| Sentences (prose + list items; headings and tables excluded) | 122 |
| Sentences with no citation marker of their own | 22 (18%) |
| Paragraphs/list items with no citation marker at all | 3 of 41 |
| Table rows (not counted as sentences) | 18 |
| Sources listed in sources CSV | 38 |
| Distinct citation numbers used in text | 38 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 3 | 0.7 | landmark (2), respected (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 1 | 0.2 | purported (1) |
| MOS:WTW editorializing | 7 | 1.7 | only (7) |
| MOS:WTW connectives (but/despite/however...) | 40 | 9.5 | despite (12), but (10), though (8), while (8), however (2) |
| MOS:WTW synonyms for 'said' | 1 | 0.2 | note (1) |
| Hyland 2005 hedges | 34 | 8.0 | often (10), approximately (3), rather (3), argue (2), could (2) |
| Hyland 2005 boosters | 13 | 3.1 | known (3), certain (2), show (2), shows (2), believed (1) |

## Flags

Side labels: the task's three labels are kept. In this article, which is mainly about female genital cutting, 'pro-circumcision' marks a flag whose reasoning makes genital cutting (or male circumcision, where it is compared) look more acceptable or benign, or makes its critics look less credible. 'anti-circumcision' marks a flag whose reasoning makes genital cutting look worse or its defenders less credible. 'neutral/structural' marks flags that favor neither.

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "Predominantly Type I (clitoridectomy) or Type II (excision), with 16.6% involving infibulation (Type III), the practice correlates with elevated health risks including hemorrhage, urinary issues, and obstetric complications—studies indicate 77% of adverse neonatal outcomes link to FGM-affected mothers—compounded by a reported 34.3% lifetime health problems among cut women. [2] [1]" | F071 Base Rate Neglect | anti-circumcision | '77% of adverse neonatal outcomes link to FGM-affected mothers' is presented as evidence of risk. With 72.6-73% of women aged 15-49 cut (sentences 3, 28), roughly that share of all outcomes would come from cut mothers even with no added risk. The rate comparison in sentence 46 is the informative figure; this one ignores the base rate. (sentence 6) |
| 2 | "However, political shifts, including potential Islamist influences, could undermine progress, as evidenced by a 2022 parliamentary push to repeal the ban that was narrowly defeated." | F040 Loaded Language | neutral/structural | Uncited (code count). The label 'potential Islamist influences' is offered as the threat, supported by a '2022 parliamentary push ... narrowly defeated'. Sentences 5, 89 and 111 describe a 2024 bill rejected 31-18. The date and margin conflict internally, and the claim needs a source check. (sentence 122) |

Flag tally by side (simple count of the table above): anti-circumcision 1; neutral/structural 1.

## Both-sides balance note

Same-standard check: defenders' claims (54-60, 96-100) and the anti-FGM campaign's own claims ('contributed to a slight decline', 91; 'monumental achievement', 111) are both attributed, and neither side's claims are endorsed in the article's voice in the sentences read. Sentence 50, reporting that the cohort's PTSD attributions cut against simple trauma framing, is an example of the article including evidence that complicates the anti-FGM narrative. The male-circumcision analogy (60, 98) is attributed to defenders and not evaluated.

## What wasn't checked

- Sentences outside the reading set (76 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- The '2022 parliamentary push' (sentence 122) vs the 2024 vote was not resolved against sources.
