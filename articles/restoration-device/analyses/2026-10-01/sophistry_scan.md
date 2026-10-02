# Sophistry and fallacy scan: Restoration device

- **Article:** Restoration device
- **URL:** https://grokipedia.com/page/Restoration_device
- **Snapshot file:** `articles/restoration-device/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (7 sentences) read in full, plus 45 of 198 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This device-focused article is generally careful to say that restoration outcomes rest on self-selected surveys and small cohorts without RCTs (5-6, 114, 119, 128, 137, 147, 191, 204). Three flags were found. In the lead, the article's voice explains the research gap as 'institutional hesitancy toward patient-driven interventions countering routine circumcision', which attributes a motive without evidence. The conservative-methods section says 'persistence yields functional benefits' directly after acknowledging that validation is limited. On the other side, restoration claims are dismissed by attributing 'motivated reasoning' to the field. Lean: 1 pro, 2 anti, 0 neutral/structural. Here pro-restoration overreach is counted as anti-circumcision. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug restoration-device` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 6226 |
| Sentences (prose + list items; headings and tables excluded) | 205 |
| Sentences with no citation marker of their own | 66 (32%) |
| Paragraphs/list items with no citation marker at all | 0 of 69 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 63 |
| Distinct citation numbers used in text | 63 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 3 | 0.5 | leading (1), notable (1), prominent (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 0 | 0.0 | none |
| MOS:WTW connectives (but/despite/however...) | 64 | 10.3 | but (21), though (20), while (16), however (5), despite (2) |
| MOS:WTW synonyms for 'said' | 4 | 0.6 | confirm (2), assert (1), note (1) |
| Hyland 2005 hedges | 86 | 13.8 | often (21), typically (16), rather (14), may (10), around (6) |
| Hyland 2005 boosters | 11 | 1.8 | must (4), established (2), found (2), demonstrated (1), known (1) |

## Flags

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "This gap reflects broader institutional hesitancy toward patient-driven interventions countering routine circumcision, where formal studies remain scarce. [2]" | F033 Causal Oversimplification | anti-circumcision | Explains the evidence gap as 'broader institutional hesitancy toward patient-driven interventions countering routine circumcision'. A single, motive-based cause is asserted in the article's voice. Other explanations (small user base, non-medical context, noted in 72 and 112) are not weighed. (sentence 7) |
| 2 | "Psychological commitment is integral, as motivations often stem from bodily autonomy rather than medical necessity, yet persistence yields functional benefits without the permanence of surgery. [4]" | F011 Hasty Generalization | anti-circumcision | 'Persistence yields functional benefits without the permanence of surgery' asserts functional benefit as established. Sentence 191, immediately before it, says 'empirical validation remains limited to qualitative studies and practitioner anecdotes'. (sentence 193) |
| 3 | "These claims persist in non-scientific forums but lack falsifiable metrics, highlighting the predominance of motivated reasoning over empirical validation in the field. [2]" | F001 Ad Hominem | pro-circumcision | Says the claims 'lack falsifiable metrics, highlighting the predominance of motivated reasoning over empirical validation in the field'. The first half is a fair evidence point, but the conclusion moves from the evidence gap to the proponents' motives. (sentence 140) |

Flag tally by side (simple count of the table above): anti-circumcision 2; pro-circumcision 1.

## Both-sides balance note

Same-standard check: the article holds restoration benefit claims to an RCT standard consistently (128, 137-138, 166) and also applies it to surgical restoration (172, 182). The anti-side overreaches are framing in the lead (7) and an unsupported benefit claim (193). The pro-side overreach is a motive dismissal (140). Sentence 157's account of provider 'dismissal or ridicule' (25% figure) is uncited in-sentence and needs a source check.

## What wasn't checked

- Sentences outside the reading set (153 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- Extraction artifact in sentence 72 ('00183-8/fulltext)').
- Survey figures (1,790 respondents; 69.1%; 74.8%; 86.7%) were not checked. Note that foreskin-restoration 71 gives a 2023 survey of 1,192 restorers, which may or may not be the same study.
