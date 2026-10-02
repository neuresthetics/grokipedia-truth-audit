# Sophistry and fallacy scan: Holy Prepuce

- **Article:** Holy Prepuce
- **URL:** https://grokipedia.com/page/Holy_Prepuce
- **Snapshot file:** `articles/holy-prepuce/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (14 sentences) read in full, plus 34 of 103 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This is a relic-history article and has no bearing on the medical or ethical circumcision debate. Most devotional claims are attributed ('purported', 'claimed', 'reportedly'). Two neutral/structural flags were found, both uncited: one says in the article's voice that the relic is 'concrete evidence of the Incarnation', and one reports a chronicle miracle as 'a documented miracle'. Structurally, the article gives inconsistent site counts ('at least 18' in sentences 2 and 80 vs 'at least 31' in sentence 50), and an 'historians attribute' claim about guild-like fabrication is uncited (80). Lean: 0 pro, 0 anti, 2 neutral/structural. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug holy-prepuce` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 3869 |
| Sentences (prose + list items; headings and tables excluded) | 117 |
| Sentences with no citation marker of their own | 45 (38%) |
| Paragraphs/list items with no citation marker at all | 0 of 39 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 21 |
| Distinct citation numbers used in text | 23 |
| Dangling citation numbers (used, no source row) | 2: 22–23 |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 13 | 3.4 | prominent (4), notable (3), unique (2), extraordinary (1), legendary (1) |
| MOS:WTW contentious labels | 2 | 0.5 | cult (1), myth (1) |
| MOS:WTW unsupported attributions | 1 | 0.3 | officially (1) |
| MOS:WTW expressions of doubt | 4 | 1.0 | purported (4) |
| MOS:WTW editorializing | 6 | 1.6 | only (5), notably (1) |
| MOS:WTW connectives (but/despite/however...) | 22 | 5.7 | but (8), while (6), though (4), despite (3), although (1) |
| MOS:WTW synonyms for 'said' | 4 | 1.0 | claim (3), confirm (1) |
| Hyland 2005 hedges | 44 | 11.4 | claims (11), often (9), claimed (5), claim (3), about (2) |
| Hyland 2005 boosters | 10 | 2.6 | never (3), known (2), true (2), established (1), proved (1) |

## Flags

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "The Holy Prepuce holds profound theological significance in Christian doctrine as a tangible remnant of Jesus Christ's humanity, serving as concrete evidence of the Incarnation described in John 1:14, where "the Word became flesh and dwelt among us."" | F004 Appeal to Authority | neutral/structural | Uncited (code count). The article's voice says the relic serves 'as concrete evidence of the Incarnation'. A doctrinal claim is presented as evidential fact rather than as the tradition's view; the article itself calls the relic 'purported' (1). (sentence 24) |
| 2 | "In Charroux, France, the Abbey of Charroux claimed possession from Charlemagne in the 9th century, with a documented miracle involving the relic bleeding in 1082 during a council." | F004 Appeal to Authority | neutral/structural | Uncited. 'A documented miracle involving the relic bleeding in 1082': an abbey or chronicle account is turned into documentation of a miracle, when it documents only that the claim was made. (sentence 54) |

Flag tally by side (simple count of the table above): neutral/structural 2.

## Both-sides balance note

Same-standard check: the skeptics (Guibert of Nogent, 61, 69) and the defenders (Thomas of Chobham, Aquinas, 7, 29) are both attributed. Lean is not applicable to the circumcision debate. Sentence 10's 'anti-Judaism in Christian appropriation of circumcision' is cited and interpretive, and was not flagged.

## What wasn't checked

- Sentences outside the reading set (69 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- Site counts (18 vs 31) and the 'historians attribute ... guild-like operations' claim (80) were not checked against sources.
