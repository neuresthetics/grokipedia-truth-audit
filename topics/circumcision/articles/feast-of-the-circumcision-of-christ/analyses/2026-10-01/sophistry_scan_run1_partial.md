> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: Feast of the Circumcision of Christ

- **Article:** Feast of the Circumcision of Christ
- **URL:** https://grokipedia.com/page/Feast_of_the_Circumcision_of_Christ
- **Snapshot file:** `articles/feast-of-the-circumcision-of-christ/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (13 sentences) read in full, plus 41 of 125 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This is a liturgical-history article. Most theological content is attributed to traditions ('In Orthodox theology', patristic authors, named collects and hymns). One flag was found: an uncited sentence asserts in the article's own voice that Jesus entered Israel 'as the promised Messiah', which is a confessional claim stated as fact. There is also an internal inconsistency on dating (sentence 3, 'since at least the fourth century', vs sentence 36, 'emerged ... during the sixth century'); that is a factual inconsistency rather than a fallacy and is noted, not flagged. The article does not bear on the medical or ethical circumcision debate. The one flag is neutral/structural. This is a judgment call.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug feast-of-the-circumcision-of-christ` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 4605 |
| Sentences (prose + list items; headings and tables excluded) | 138 |
| Sentences with no citation marker of their own | 57 (41%) |
| Paragraphs/list items with no citation marker at all | 0 of 50 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 81 |
| Distinct citation numbers used in text | 76 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 5: 77–81 |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 9 | 2.0 | great (5), celebrated (3), popular (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 1 | 0.2 | only (1) |
| MOS:WTW connectives (but/despite/however...) | 25 | 5.4 | while (16), but (3), though (3), however (2), despite (1) |
| MOS:WTW synonyms for 'said' | 1 | 0.2 | observe (1) |
| Hyland 2005 hedges | 21 | 4.6 | often (11), appears (2), argued (2), rather (2), appear (1) |
| Hyland 2005 boosters | 8 | 1.7 | known (2), true (2), believed (1), established (1), never (1) |

## Flags

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "The circumcision of Jesus, performed on the eighth day after his birth as prescribed by Jewish law, served as a profound affirmation of his submission to the Mosaic covenant, marking his entry into the community of Israel as the promised Messiah." | F004 Appeal to Authority | neutral/structural | Uncited (code count). States in the article's voice that the circumcision marked Jesus' entry 'as the promised Messiah'. Tradition is the only warrant, and its theological claim is presented as historical fact rather than attributed. (sentence 63) |

Flag tally by side (simple count of the table above): neutral/structural 1.

## Both-sides balance note

Same-standard check: Eastern, Catholic, Anglican, Lutheran and Reformed practices are each described in their own terms, including the Reformed rejection of fixed feasts (58, 133). Jewish naming practice (87) is described accurately as far as can be seen without opening sources. The pro/anti-circumcision lean is not applicable.

## What wasn't checked

- Sentences outside the reading set (84 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- Sources 77-81 are listed but never cited (code count).
- The dating inconsistency between sentences 3 and 36 was not resolved against sources.
