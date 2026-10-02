> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: Circumcision surgical procedure

- **Article:** Circumcision surgical procedure
- **URL:** https://grokipedia.com/page/Circumcision_surgical_procedure
- **Snapshot file:** `topics/circumcision/articles/circumcision-surgical-procedure/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (6 sentences) read in full, plus 45 of 254 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This is mostly a technical how-it-is-done article: techniques, devices, anesthesia, aftercare. The ethics and public-health disputes are reported with attribution on both sides, and AAP and CDC caveats are included. Four reasoning flags were found in the sentences read. Two favor circumcision: a mechanism stated as causal on the basis of cohort data, and a 100:1-200:1 benefit-to-risk ratio presented as 'risk-benefit analyses' generally. One is structural: brit milah is grouped with tribal initiations under 'non-sterile conditions and untrained performers'. One favors the critical side: an uncited generalization about low and tight circumcisions. On the sentences read: 2 pro, 1 anti, 1 neutral/structural. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug circumcision-surgical-procedure` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 8510 |
| Sentences (prose + list items; headings and tables excluded) | 260 |
| Sentences with no citation marker of their own | 72 (28%) |
| Paragraphs/list items with no citation marker at all | 2 of 80 |
| Table rows (not counted as sentences) | 5 |
| Sources listed in sources CSV | 154 |
| Distinct citation numbers used in text | 158 |
| Dangling citation numbers (used, no source row) | 4: 2014, 2021, 2024–2025 |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 0 | 0.0 | none |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 2 | 0.2 | only (2) |
| MOS:WTW connectives (but/despite/however...) | 83 | 9.8 | though (31), but (27), while (18), despite (4), however (3) |
| MOS:WTW synonyms for 'said' | 7 | 0.8 | confirm (4), assert (1), expose (1), find (1) |
| Hyland 2005 hedges | 129 | 15.2 | often (20), typically (20), may (16), approximately (11), generally (9) |
| Hyland 2005 boosters | 20 | 2.4 | show (6), must (3), found (2), certain (1), clear (1) |

## Flags

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "This protective effect stems from the removal of the foreskin, which can harbor bacteria under suboptimal hygiene conditions, as evidenced by cohort studies showing a 10-fold lower incidence in circumcised versus uncircumcised infants. [16]" | F032 Cum Hoc | pro-circumcision | 'This protective effect stems from the removal of the foreskin ... as evidenced by cohort studies': a causal mechanism is asserted with observational cohort data as the evidence named. (sentence 29) |
| 2 | "Risk-benefit analyses estimate benefits outweighing risks by ratios of 100:1 to 200:1 when aggregating lifetime protections against infections and cancers. [151]" | F004 Appeal to Authority | pro-circumcision | A 100:1-200:1 benefit-to-risk ratio is stated in the article's voice as what 'risk-benefit analyses estimate', with no named author or method, though it sits in a section on disputes. The aggregation method ('aggregating lifetime protections') decides the result and is not shown. Claim needs source check. (sentence 255) |
| 3 | "Ritual or traditional settings, including Jewish brit milah by mohels or tribal initiations, often forgo anesthesia and modern clamps in favor of sharp instruments like ritual knives, resulting in substantially higher risks—up to 14% severe complications like excessive bleeding or sepsis—due to non-sterile conditions and untrained performers. [10]" | F020 Division | neutral/structural | Assigns the properties of the broad class 'ritual or traditional settings' ('non-sterile conditions and untrained performers', up to 14% severe complications) to each member, including brit milah by mohels, with no member-specific evidence. (sentence 25) |
| 4 | "In low and tight circumcisions, which remove significant inner foreskin and shaft skin resulting in minimal loose skin and reduced gliding action, masturbation techniques often shift from foreskin rolling or gliding to direct glans and shaft stimulation, frequently requiring lubricant due to increased friction and lack of natural skin movement." | F011 Hasty Generalization | anti-circumcision | Uncited (code count). A general claim about how men with low and tight circumcisions 'often' and 'frequently' masturbate and need lubricant, with no source or sample shown. (sentence 212) |

Flag tally by side (simple count of the table above): anti-circumcision 1; neutral/structural 1; pro-circumcision 2.

## Both-sides balance note

Same-standard check: the 'Ethical Perspectives' and 'Medical and Public Health Disputes' sections pair each proponent claim with a critic reply (239/240, 243, 248/250, 251/253), and attribution verbs are fairly even ('argue', 'contend', 'highlight'). Sentence 210 says earlier observational findings of reduced sensitivity 'have been contradicted' by prospective studies. That is a one-way summary, but it is cited and was not flagged. The article includes Reddit-sourced aftercare tips (185) and labels them anecdotal (187), which is disclosed, not a reasoning fault.

## What wasn't checked

- Sentences outside the reading set (209 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- The '[2014]', '[2021]', '[2024]', '[2025]' brackets counted as dangling citation numbers are years rendered as citation links on the page (see INDEX).
- Practical medical advice in the aftercare sections was not evaluated.
