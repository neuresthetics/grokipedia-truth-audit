> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: Circumcision in China

- **Article:** Circumcision in China
- **URL:** https://grokipedia.com/page/Circumcision_in_China
- **Snapshot file:** `articles/circumcision-in-china/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (5 sentences) read in full, plus 25 of 50 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This is a short, mostly descriptive article on low circumcision prevalence among the Han majority and religious practice among Muslim minorities. It does not argue the ethics. Much of the history section is uncited (code count). Two reasoning flags were found. An uncited causal explanation attributes low Han adoption to 'traditional views prioritizing bodily integrity'. And 'despite global evidence' implies that Chinese authorities are ignoring evidence whose scope (high-HIV-prevalence settings) the sentence does not state. Lean: 1 pro-circumcision and 1 neutral/structural flag. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug circumcision-in-china` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 1497 |
| Sentences (prose + list items; headings and tables excluded) | 55 |
| Sentences with no citation marker of their own | 18 (33%) |
| Paragraphs/list items with no citation marker at all | 4 of 25 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 36 |
| Distinct citation numbers used in text | 32 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 4: 33–36 |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 0 | 0.0 | none |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 0 | 0.0 | none |
| MOS:WTW connectives (but/despite/however...) | 13 | 8.7 | though (4), while (4), but (2), despite (2), however (1) |
| MOS:WTW synonyms for 'said' | 0 | 0.0 | none |
| Hyland 2005 hedges | 24 | 16.0 | often (5), rather (4), generally (3), typically (3), may (2) |
| Hyland 2005 boosters | 7 | 4.7 | established (2), certain (1), found (1), known (1), never (1) |

## Flags

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "Western medical influences, including those from missionaries and modern public health reformers, introduced surgical options for genital hygiene, yet adoption stayed limited due to entrenched traditional views prioritizing bodily integrity." | F033 Causal Oversimplification | neutral/structural | Uncited (code count). Gives a single cultural cause ('entrenched traditional views prioritizing bodily integrity') for limited adoption. Cost, medical practice and the absence of religious motive (noted elsewhere in the article) are other candidate causes the sentence leaves out. (sentence 13) |
| 2 | "Authorities have refrained from endorsing circumcision for HIV prevention, citing insufficient readiness for policy adoption despite global evidence. [12]" | F022 Accident | pro-circumcision | 'Despite global evidence' frames non-endorsement as going against the evidence. It applies evidence scoped to high-HIV-prevalence heterosexual epidemics to China as a whole without stating that scope condition. (sentence 49) |

Flag tally by side (simple count of the table above): neutral/structural 1; pro-circumcision 1.

## Both-sides balance note

Same-standard check: the article reports both 'high theoretical acceptability' (sentence 4) and cultural reasons for low uptake (16-19), with similar attribution. The Confucian bodily-integrity view (16-18) is attributed to tradition and is not presented as the article's own position, so it was not flagged. Pro-side medical claims are brief and mostly scoped to therapeutic indications. No ethical debate appears in the sentences read.

## What wasn't checked

- Sentences outside the reading set (25 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- Sources 33-36 are listed but never cited (code count).
