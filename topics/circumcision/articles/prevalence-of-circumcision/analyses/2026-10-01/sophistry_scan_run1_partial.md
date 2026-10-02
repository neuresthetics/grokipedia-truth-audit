> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: Prevalence of circumcision

- **Article:** Prevalence of circumcision
- **URL:** https://grokipedia.com/page/Prevalence_of_circumcision
- **Snapshot file:** `topics/circumcision/articles/prevalence-of-circumcision/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (7 sentences) read in full, plus 45 of 178 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This statistical article is mostly descriptive and organized by region, and many sentences carry no citation of their own (see code counts). Three flags were found. Two are pro-circumcision: the trials are credited with 'causal evidence' for a specific anatomical mechanism (viral entry, target cells, micro-tears), when what they measured was the effect of circumcision; and the US decline is framed as 'parental skepticism toward medical recommendations despite AAP and CDC endorsements', although the AAP does not recommend routine circumcision. One is structural: advocacy groups are credited with 'accelerating the drop' in Australia beyond policy changes, without evidence that separates the two. Also noted: China is given at 14% here (104, uncited), against 2-5% in another article in this set, and extraction artifacts appear in sentence 63. Lean: 2 pro, 0 anti, 1 neutral/structural. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug prevalence-of-circumcision` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 5906 |
| Sentences (prose + list items; headings and tables excluded) | 185 |
| Sentences with no citation marker of their own | 58 (31%) |
| Paragraphs/list items with no citation marker at all | 4 of 60 |
| Table rows (not counted as sentences) | 7 |
| Sources listed in sources CSV | 105 |
| Distinct citation numbers used in text | 105 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 3 | 0.5 | celebrated (1), leading (1), notable (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 2 | 0.3 | purported (1), supposed (1) |
| MOS:WTW editorializing | 0 | 0.0 | none |
| MOS:WTW connectives (but/despite/however...) | 51 | 8.6 | though (21), but (11), despite (10), while (6), however (3) |
| MOS:WTW synonyms for 'said' | 3 | 0.5 | confirm (1), observe (1), reveal (1) |
| Hyland 2005 hedges | 115 | 19.5 | rather (20), around (17), approximately (15), often (14), typically (10) |
| Hyland 2005 boosters | 17 | 2.9 | show (7), showed (3), shown (2), shows (2), certain (1) |

## Flags

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "Causal evidence from the trials attributes the protective effect to reduced viral entry via the foreskin, which harbors more target cells for HIV and is prone to micro-tears during intercourse, rather than behavioral changes, as circumcised participants reported similar sexual practices. [32]" | F034 False Cause | pro-circumcision | 'Causal evidence from the trials attributes the protective effect to reduced viral entry via the foreskin, which harbors more target cells ... and is prone to micro-tears'. The RCTs established the effect of circumcision. The mechanism is a hypothesis, and here it is presented as trial-established. This is the same issue as foreskin 126 and mohel 94. (sentence 44) |
| 2 | "Factors contributing to the decline include state-level policy shifts (Medicaid ending coverage in some states), increasing parental skepticism toward medical recommendations despite AAP and CDC endorsements of benefits (e.g., reduced UTI and STI risks), cultural/ethical debates, and demographic changes like growing Hispanic populations with lower rates." | F036 Suppressed Evidence | pro-circumcision | Uncited (code count). Frames the decline as 'increasing parental skepticism toward medical recommendations despite AAP and CDC endorsements of benefits'. The omitted point, reported in other articles in this set, is that the AAP stops short of recommending routine circumcision, so there is no recommendation for parents to be skeptical of. (sentence 127) |
| 3 | "Anti-circumcision advocacy groups have further influenced public opinion by highlighting ethical concerns over infant consent and potential complications, accelerating the drop beyond medical policy changes alone. [11]" | F031 Post Hoc | neutral/structural | Credits advocacy groups with 'accelerating the drop beyond medical policy changes alone'. The decline follows both influences in time, and no evidence separates the advocacy effect from the medical-policy effect described in 167. (sentence 168) |

Flag tally by side (simple count of the table above): neutral/structural 1; pro-circumcision 2.

## Both-sides balance note

Same-standard check: low-prevalence regions' medical positions (Royal Australasian College of Physicians, 167; Europe, 142-152) are reported fairly, and the US benefits are stated with absolute figures (48: '0.1-0.2% absolute'). Mechanism and benefit framing lean pro (44, 127). Anti-side influence is credited causally (168), but neutrally rather than pejoratively.

## What wasn't checked

- Sentences outside the reading set (133 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- China 14% (104) vs 2-5% in circumcision-in-china, a cross-article inconsistency, was not resolved.
- Sentence 3 says circumcision is 'obligatory shortly after birth' for both Islam and Judaism, which conflicts with khitan-circumcision 3 and 94 (no fixed age; obligatory in some schools only). This was not resolved.
- Extraction artifacts in sentence 63 ('00515-0/fulltext)').
