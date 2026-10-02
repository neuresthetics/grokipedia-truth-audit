# Sophistry and fallacy scan: Lipodermos

- **Article:** Lipodermos
- **URL:** https://grokipedia.com/page/Lipodermos
- **Snapshot file:** `articles/lipodermos/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (2 sentences) read in full, plus 35 of 105 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This is a classical-medicine and history article. Its Greek and Roman sources (Celsus, Soranus, Galen, the pseudo-Galenic Definitiones) are described as ancient views, and the attitude toward circumcision ('barbarism', 'primitive') is attributed to Greek society. One neutral/structural flag was found: an uncited lead sentence describes ancient prepuce restoration with the modern term 'bodily integrity', which reads a contemporary ethical frame into Greco-Roman aesthetics. The short 'contemporary relevance' section (102-104) connects to modern circumcision ethics only lightly and was not flagged. Lean: 0 pro, 0 anti, 1 neutral/structural. This is a judgment call.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug lipodermos` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 3367 |
| Sentences (prose + list items; headings and tables excluded) | 107 |
| Sentences with no citation marker of their own | 36 (34%) |
| Paragraphs/list items with no citation marker at all | 2 of 37 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 18 |
| Distinct citation numbers used in text | 16 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 2: 17–18 |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 4 | 1.2 | celebrated (1), great (1), notable (1), prominent (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 3 | 0.9 | notably (2), only (1) |
| MOS:WTW connectives (but/despite/however...) | 18 | 5.3 | while (7), though (6), but (5) |
| MOS:WTW synonyms for 'said' | 0 | 0.0 | none |
| Hyland 2005 hedges | 38 | 11.3 | around (8), rather (8), often (7), could (4), may (2) |
| Hyland 2005 boosters | 5 | 1.5 | thought (2), finds (1), found (1), known (1) |

## Flags

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "This condition highlighted the intersection of medicine, aesthetics, and cultural identity in antiquity, where restoring the prepuce aligned with Greco-Roman ideals of bodily integrity, as explored in subsequent sections." | F058 Presentism | neutral/structural | Uncited (code count). 'Restoring the prepuce aligned with Greco-Roman ideals of bodily integrity'. The body describes ideals of proportion, modesty and sophrosyne (43-58); 'bodily integrity' is a modern rights term, so a present-day concept is applied to antiquity. (sentence 2) |

Flag tally by side (simple count of the table above): neutral/structural 1.

## Both-sides balance note

Same-standard check: Greek disdain for circumcision (54) and Philo's defense of it (58) are both reported as historical positions. Neither pro- nor anti-circumcision reasoning was found in the article's voice in the sentences read.

## What wasn't checked

- Sentences outside the reading set (70 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- The classical source passages (Celsus, De Medicina 7.25; Soranus; Galen) were not checked against editions.
