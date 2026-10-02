# Sophistry and fallacy scan: Gishiri cutting

- **Article:** Gishiri cutting
- **URL:** https://grokipedia.com/page/Gishiri_cutting
- **Snapshot file:** `articles/gishiri-cutting/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (7 sentences) read in full, plus 45 of 140 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This is a clinically focused article. Traditional rationales are reported as beliefs (54-68), set against hospital fistula data, and the limits of that data are acknowledged: hospital-based records, limited longitudinal studies, and insufficient prevalence data (97, 131, 138). The harm evidence is presented with appropriate hedges, so no anti-cutting overreach was flagged. One structural flag was found: the article credits 'reductions in the practice' to awareness of complications, although it says elsewhere that there is no Gishiri-specific prevalence data from which a reduction could be measured. Lean: 0 pro, 0 anti, 1 neutral/structural. This is a judgment call.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug gishiri-cutting` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 4972 |
| Sentences (prose + list items; headings and tables excluded) | 147 |
| Sentences with no citation marker of their own | 10 (7%) |
| Paragraphs/list items with no citation marker at all | 0 of 55 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 58 |
| Distinct citation numbers used in text | 58 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 1 | 0.2 | notable (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 3 | 0.6 | purported (2), supposed (1) |
| MOS:WTW editorializing | 1 | 0.2 | notably (1) |
| MOS:WTW connectives (but/despite/however...) | 29 | 5.8 | though (12), but (8), despite (5), while (3), however (1) |
| MOS:WTW synonyms for 'said' | 4 | 0.8 | assert (1), claim (1), expose (1), reveal (1) |
| Hyland 2005 hedges | 71 | 14.3 | often (20), rather (13), typically (9), approximately (4), claims (4) |
| Hyland 2005 boosters | 12 | 2.4 | known (4), believed (3), certain (1), demonstrate (1), demonstrated (1) |

## Flags

Side labels: the task's three labels are kept. In this article, which is mainly about female genital cutting, 'pro-circumcision' marks a flag whose reasoning makes genital cutting (or male circumcision, where it is compared) look more acceptable or benign, or makes its critics look less credible. 'anti-circumcision' marks a flag whose reasoning makes genital cutting look worse or its defenders less credible. 'neutral/structural' marks flags that favor neither.

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "Conversely, reductions in the practice are driven by heightened awareness of its complications, particularly vesicovaginal fistulas (VVF), with data from northern Nigerian hospitals indicating that Gishiri cuts account for up to 15% of pediatric VVF cases among girls under 13, often resulting from hemorrhage, infection, or tissue necrosis post-procedure. [4] [9]" | F034 False Cause | neutral/structural | Asserts that 'reductions in the practice are driven by heightened awareness of its complications'. Sentence 131 says there is 'insufficient data on Gishiri-specific prevalence', and sentence 138 says rates are 'insufficient for population-level quantification'. Both the reduction and its cause are asserted without data. Sentence 146 makes a similar campaign-effect claim. (sentence 144) |

Flag tally by side (simple count of the table above): neutral/structural 1.

## Both-sides balance note

Same-standard check: traditional efficacy claims are held to a controlled-evidence standard (85, 99, 112), and the harm evidence is also caveated as hospital-based and limited (97, 138). Both sides' evidence is described by its quality. Sentence 112 offers alternative explanations for reported benefits (misattribution, transient widening) rather than dismissing them by label. There is no male-circumcision comparison.

## What wasn't checked

- Sentences outside the reading set (95 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- Fistula attribution share: 5-18% (sentence 4) vs 1-18% (sentence 14) is an internal inconsistency and was not resolved.
