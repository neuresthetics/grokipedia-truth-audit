# Sophistry and fallacy scan: Circumcision of Jesus

- **Article:** Circumcision of Jesus
- **URL:** https://grokipedia.com/page/Circumcision_of_Jesus
- **Snapshot file:** `articles/circumcision-of-jesus/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (6 sentences) read in full, plus 45 of 139 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This is a religious-history and art-history article. The relic sections are skeptical and give reasons, and the historicity section correctly says the event lacks extra-biblical corroboration. The reasoning problems are structural. The article contradicts itself on historicity: it says 'universally accepted via Gospel attestation' in one place and 'a matter of faith tradition rather than empirically corroborated history' in another. It also states theological conclusions in its own voice, once backed by the absence of evidence for the opposite. All 3 flags are neutral/structural; nothing in the sentences read bears on the modern circumcision debate. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug circumcision-of-jesus` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 5218 |
| Sentences (prose + list items; headings and tables excluded) | 145 |
| Sentences with no citation marker of their own | 22 (15%) |
| Paragraphs/list items with no citation marker at all | 0 of 47 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 80 |
| Distinct citation numbers used in text | 80 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 9 | 1.7 | great (3), extraordinary (2), unique (2), legendary (1), prominent (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 3 | 0.6 | purported (2), alleged (1) |
| MOS:WTW editorializing | 3 | 0.6 | only (3) |
| MOS:WTW connectives (but/despite/however...) | 29 | 5.6 | though (10), while (8), but (7), despite (2), however (2) |
| MOS:WTW synonyms for 'said' | 7 | 1.3 | confirm (2), assert (1), claim (1), expose (1), note (1) |
| Hyland 2005 hedges | 55 | 10.5 | rather (14), claims (8), often (8), around (3), claimed (3) |
| Hyland 2005 boosters | 6 | 1.1 | true (3), established (1), realized (1), shows (1) |

## Flags

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "Interdenominational debates focus less on the event's historicity—universally accepted via Gospel attestation—and more on its soteriological and ecclesial implications, particularly whether it analogizes infant baptism or obligates covenant continuity." | F005 Appeal to Popularity | neutral/structural | Uncited (code count). Historicity is said to be 'universally accepted via Gospel attestation', an appeal to general acceptance. It contradicts sentence 29 ('a matter of faith tradition rather than empirically corroborated history') and sentence 28 on critical analyses. (sentence 58) |
| 2 | "This framework underscores causal realism in redemption: the physical rite's pain and blood directly anticipate the efficacious atonement, not as symbolic abstraction but as historical pre-enactment ordained by God, ensuring the antitype's reality validates the type's prophetic intent. [29]" | F004 Appeal to Authority | neutral/structural | States in the article's voice that the rite is a 'historical pre-enactment ordained by God' and calls this 'causal realism'. The theological tradition is the only warrant, and its claim is given as fact rather than attributed. (sentence 46) |
| 3 | "Theological contention persists on typology—whether it strictly prefigures spiritual excision of sin or risks conflating shadows with substance—but consensus holds that Christ's circumcision uniquely qualified him to atone, obviating repetition for justification, as no empirical evidence supports salvific efficacy in the rite absent faith. [37] [19]" | F010 Appeal to Ignorance | neutral/structural | A theological 'consensus' is supported by 'no empirical evidence supports salvific efficacy in the rite absent faith'. Absence of empirical evidence for a non-empirical claim is offered as support for a doctrinal position. (sentence 60) |

Flag tally by side (simple count of the table above): neutral/structural 3.

## Both-sides balance note

Same-standard check: skeptical treatment is applied firmly to relic claims (sentences 118-145), with stated reasons (multiplicity, provenance gaps, decomposition). Comparable scrutiny is applied to the nativity account in sentences 28-29, but sentence 58 then undercuts it. Denominational views are attributed by tradition (Catholic, Orthodox, Reformed). Not applicable to the pro/anti-circumcision lean.

## What wasn't checked

- Sentences outside the reading set (94 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- Art-historical attributions and dates were not checked.
