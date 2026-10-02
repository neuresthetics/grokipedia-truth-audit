> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: Religious views on female genital mutilation

- **Article:** Religious views on female genital mutilation
- **URL:** https://grokipedia.com/page/Religious_views_on_female_genital_mutilation
- **Snapshot file:** `articles/religious-views-on-female-genital-mutilation/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (7 sentences) read in full, plus 45 of 149 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This article surveys Islamic, Christian, Jewish and traditional-religion positions with attribution to named bodies and scholars (Dar al-Ifta, Al-Azhar, the Fiqh Council of North America, al-Qaradawi, Pope Francis). Three flags were found. An uncited sentence denies any intrinsic link to Islam by citing 'certain' regions, while the lead reports the opposite pattern in Burkina Faso. A speculative causal origin (paternity uncertainty) is presented as 'observable' although the article admits the traces are sparse. The closing sentence generalizes harm 'across procedure types', which takes in the minimal forms the same section discusses. The article also gives Dar al-Ifta two incompatible positions (57: 'permissible and recommended' in 2007; 60: 'prohibited (haram)'), which is noted rather than flagged. Lean: 0 pro, 1 anti, 2 neutral/structural. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug religious-views-on-female-genital-mutilation` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 5222 |
| Sentences (prose + list items; headings and tables excluded) | 156 |
| Sentences with no citation marker of their own | 40 (26%) |
| Paragraphs/list items with no citation marker at all | 1 of 55 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 108 |
| Distinct citation numbers used in text | 107 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 1: 108 |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 4 | 0.8 | honorable (3), leading (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 1 | 0.2 | officially (1) |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 1 | 0.2 | only (1) |
| MOS:WTW connectives (but/despite/however...) | 36 | 6.9 | though (11), while (10), but (7), despite (5), however (3) |
| MOS:WTW synonyms for 'said' | 8 | 1.5 | reveal (5), confirm (3) |
| Hyland 2005 hedges | 53 | 10.1 | rather (21), often (7), indicate (4), typically (4), approximately (3) |
| Hyland 2005 boosters | 14 | 2.7 | certain (3), must (3), known (2), show (2), shows (2) |

## Flags

Side labels: the task's three labels are kept. In this article, which is mainly about female genital cutting, 'pro-circumcision' marks a flag whose reasoning makes genital cutting (or male circumcision, where it is compared) look more acceptable or benign, or makes its critics look less credible. 'anti-circumcision' marks a flag whose reasoning makes genital cutting look worse or its defenders less credible. 'neutral/structural' marks flags that favor neither.

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "The notion that FGM is intrinsically linked to Islam lacks empirical support, as the practice shows higher rates among animist and Christian populations in certain African regions compared to many Muslim-majority areas." | F036 Suppressed Evidence | neutral/structural | Uncited (code count). 'The notion that FGM is intrinsically linked to Islam lacks empirical support, as the practice shows higher rates among animist and Christian populations in certain African regions'. Sentence 4 reports 'higher prevalence among Muslims compared to Christians or adherents of traditional religions in countries like Burkina Faso', and that evidence is not addressed here. The comparison selects 'certain' regions against 'many' Muslim-majority areas. (sentence 27) |
| 2 | "Empirical patterns link the rite to agrarian and nomadic economies where ensuring female fidelity reduced paternity uncertainty, a causal driver observable in non-religious contexts across prehistoric Eurasian and African analogs, though direct paleontological traces remain sparse. [30]" | F033 Causal Oversimplification | neutral/structural | Attributes the rite's origin to paternity-uncertainty reduction as 'a causal driver observable ... across prehistoric Eurasian and African analogs', while conceding that 'direct paleontological traces remain sparse'. A single speculative cause is presented as observed. (sentence 35) |
| 3 | "These perspectives highlight tensions between universal human rights framing and contextual relativism, though longitudinal studies confirm sustained harm profiles across procedure types. [7]" | F011 Hasty Generalization | anti-circumcision | 'Longitudinal studies confirm sustained harm profiles across procedure types', a blanket generalization that includes the minimal forms discussed in 155 (and Type IV pricking elsewhere in the set), without the studies being named. (sentence 156) |

Flag tally by side (simple count of the table above): anti-circumcision 1; neutral/structural 2.

## Both-sides balance note

Same-standard check: both pro-practice Islamic opinions (56-57, 66-67) and opposing fatwas (60, 63, 65) are reported with attribution. The anthropologists' critique of campaigns (155) is attributed and answered with WHO data. The male-circumcision comparisons here (47, 51, 53, 75) concern differences in textual basis, are attributed to scriptural sources, and were not flagged.

## What wasn't checked

- Sentences outside the reading set (104 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- Dar al-Ifta's position: 'permissible and recommended' (57) vs 'prohibited (haram)' (60) was not resolved against sources.
- The mission-exposure effect estimate (88: '10-20%') was not checked.
