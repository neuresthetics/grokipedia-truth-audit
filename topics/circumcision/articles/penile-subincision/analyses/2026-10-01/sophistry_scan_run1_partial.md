> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: Penile subincision

- **Article:** Penile subincision
- **URL:** https://grokipedia.com/page/Penile_subincision
- **Snapshot file:** `topics/circumcision/articles/penile-subincision/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (8 sentences) read in full, plus 35 of 107 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This is an ethnographic and medical article. Consent and cultural-preservation positions are attributed to their holders (83-98). Three flags were found, all leaning against the practice (anti-cutting). One is an uncited article-voice label, 'ritual mutilation'. One borrows harm evidence from 'similar ritual cuttings' and 'analogous penile splitting procedures' because the article admits subincision-specific data is limited. One answers claims of cultural benefit with health-harm evidence. The harm claims themselves are plausible and partly cited, and the flags concern how they are argued, not a verdict on them. Lean: 0 pro, 3 anti, 0 neutral/structural. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug penile-subincision` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 4001 |
| Sentences (prose + list items; headings and tables excluded) | 115 |
| Sentences with no citation marker of their own | 14 (12%) |
| Paragraphs/list items with no citation marker at all | 1 of 40 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 45 |
| Distinct citation numbers used in text | 45 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 2 | 0.5 | unique (2) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 1 | 0.2 | purported (1) |
| MOS:WTW editorializing | 0 | 0.0 | none |
| MOS:WTW connectives (but/despite/however...) | 35 | 8.7 | but (11), though (10), while (6), despite (5), however (3) |
| MOS:WTW synonyms for 'said' | 2 | 0.5 | expose (1), note (1) |
| Hyland 2005 hedges | 46 | 11.5 | often (12), typically (12), rather (7), may (4), claims (3) |
| Hyland 2005 boosters | 9 | 2.2 | certain (6), demonstrated (2), believed (1) |

## Flags

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "Penile subincision, a form of urethrotomy involving a longitudinal incision along the ventral surface of the penis, was practiced exclusively by certain Indigenous Australian tribes as a ritual mutilation during male initiation ceremonies prior to European colonization." | F040 Loaded Language | anti-circumcision | Uncited (code count). The article's voice calls the practice 'a ritual mutilation' (and 'the mutilation' in sentence 28), while the lead uses 'genital modification'. The evaluative label is in the article's voice; sentence 115 attributes the 'mutilation' framing to 'peer-reviewed analyses'. (sentence 23) |
| 2 | "Despite this, the procedure inflicts demonstrable bodily harm, involving a deep longitudinal incision along the ventral penis into the urethra without anesthesia in traditional settings, leading to risks of hemorrhage, urinary fistulas, strictures, chronic infections, and impaired erectile function, as documented in case reports of complications from similar ritual cuttings. [35]" | F042 False Analogy | anti-circumcision | Specific harms (fistulas, strictures, impaired erectile function) are said to be 'documented in case reports of complications from similar ritual cuttings'. Evidence from other procedures is carried over by analogy without showing that the procedures are comparable. Sentence 95 says data is limited and 'modern secrecy complicates quantification'. (sentence 93) |
| 3 | "This tension reflects broader global contentions in multicultural contexts, where empirical harm evidence from peer-reviewed cases challenges unsubstantiated claims of net cultural benefit, urging evidence-based policies over deference to tradition alone. [41]" | F003 Red Herring | anti-circumcision | 'Empirical harm evidence ... challenges unsubstantiated claims of net cultural benefit'. Cultural-benefit claims (kinship, cosmology, identity: 92) are not health claims, so harm evidence answers a different question. It may outweigh them, but it does not show they are unsubstantiated. (sentence 99) |

Flag tally by side (simple count of the table above): anti-circumcision 3.

## Both-sides balance note

Same-standard check: the cultural-preservation side (86, 92, 96) is described by anthropologists and attributed, while the critiques are attributed to genital-autonomy organizations, bioethicists and legal scholars (84, 88, 97). The article-voice tilt is in the closing synthesis sentences (93-95, 99, 115), all on the harm side. No pro-modification reasoning faults were found in the article's voice. Comparisons to circumcision and FGC appear only in attributed positions (84, 97).

## What wasn't checked

- Sentences outside the reading set (72 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- The legal claims in 111 (FGM-equivalent statutes 'extended to males' in the UK and Canada) and 96 ('state-level prohibitions ... since the 1990s') need source checks; no verdict is given here.
