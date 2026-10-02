# Sophistry and fallacy scan: Paraphimosis

- **Article:** Paraphimosis
- **URL:** https://grokipedia.com/page/Paraphimosis
- **Snapshot file:** `articles/paraphimosis/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (14 sentences) read in full, plus 45 of 143 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This is a clinical reference article covering definition, anatomy, causes, risk factors, diagnosis, treatment and prevention, and it is mostly descriptive. No sophistry or fallacy flags were raised in the sentences read. The lead is cited throughout, and circumcision appears only as a treatment or preventive option for recurrence, with the statement in sentence 152 that it is 'typically reserved for cases where non-surgical options fail'. Many anatomy and risk-factor sentences carry no citation of their own (see code counts), and the uncited epidemiological comparison of Europe with the United States (82) needs a source check. Lean: none. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug paraphimosis` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 4249 |
| Sentences (prose + list items; headings and tables excluded) | 157 |
| Sentences with no citation marker of their own | 49 (31%) |
| Paragraphs/list items with no citation marker at all | 0 of 56 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 49 |
| Distinct citation numbers used in text | 45 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 4: 46–49 |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 2 | 0.5 | landmark (1), prominent (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 4 | 0.9 | only (3), notably (1) |
| MOS:WTW connectives (but/despite/however...) | 22 | 5.2 | but (11), though (8), while (3) |
| MOS:WTW synonyms for 'said' | 1 | 0.2 | confirm (1) |
| Hyland 2005 hedges | 82 | 19.3 | may (23), typically (10), often (8), should (8), around (6) |
| Hyland 2005 boosters | 5 | 1.2 | must (3), certain (1), clear (1) |

## Flags

No flags. No flags were raised. Sentence 152's mention of 'broader benefits like reduced penile carcinoma incidence' in a prophylaxis context was considered but not flagged: it is relevant to the decision being described and is qualified as reserved for failed non-surgical options.

## Both-sides balance note

Same-standard check: the article states plainly that paraphimosis occurs only in uncircumcised males, as a matter of definition, and gives hygiene education as first-line prevention (136-143) before surgery (148-152). No asymmetric evidence standards were found in the sentences read.

## What wasn't checked

- Sentences outside the reading set (98 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- The uncited epidemiological claim in sentence 82 (Europe vs US prevalence) needs a source check; no verdict is given here.
