# Sophistry and fallacy scan: Foreskin restoration

- **Article:** Foreskin restoration
- **URL:** https://grokipedia.com/page/Foreskin_restoration
- **Snapshot file:** `articles/foreskin-restoration/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (6 sentences) read in full, plus 45 of 204 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This article is generally careful about evidence. It repeatedly notes that restoration benefits rest on self-selected, self-reported data with no RCTs (70, 71, 107, 126, 131, 134), and it attributes the ethical debate to named sides. Two flags were found. The lead's final sentence leaves restoration evidence to assert 'robust evidence' that circumcision 'imposes negligible long-term detriments', a pro-circumcision claim that is off-topic and held to a looser standard than the restoration claims nearby. And the opponents' argument is reported with the article's 'purported' inserted into their own position. Lean: 1 pro, 1 anti, 0 neutral/structural. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug foreskin-restoration` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 6327 |
| Sentences (prose + list items; headings and tables excluded) | 210 |
| Sentences with no citation marker of their own | 51 (24%) |
| Paragraphs/list items with no citation marker at all | 8 of 74 |
| Table rows (not counted as sentences) | 16 |
| Sources listed in sources CSV | 55 |
| Distinct citation numbers used in text | 55 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 2 | 0.3 | leading (1), unique (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 1 | 0.2 | purported (1) |
| MOS:WTW editorializing | 1 | 0.2 | only (1) |
| MOS:WTW connectives (but/despite/however...) | 57 | 9.0 | but (20), though (20), while (7), however (6), despite (4) |
| MOS:WTW synonyms for 'said' | 6 | 0.9 | note (3), assert (2), confirm (1) |
| Hyland 2005 hedges | 89 | 14.1 | often (19), rather (13), typically (13), may (8), indicate (6) |
| Hyland 2005 boosters | 8 | 1.3 | established (2), found (2), demonstrates (1), establish (1), known (1) |

## Flags

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "Empirical data on objective benefits like sensitivity gains or sexual performance improvements remain sparse and inconclusive, contrasting with robust evidence that circumcision itself imposes negligible long-term detriments to erectile or orgasmic function. [6] [2]" | F003 Red Herring | pro-circumcision | In the lead, after saying that evidence on restoration benefits is 'sparse and inconclusive', it adds 'contrasting with robust evidence that circumcision itself imposes negligible long-term detriments'. That shifts the subject from restoration to a defense of circumcision. Sexual-function evidence is described as 'mixed' elsewhere in this set (for example, foreskin-man 70), and the claim needs a source check. (sentence 6) |
| 2 | "They argue that ethical focus should prioritize IMC's purported health advantages over autonomy concerns, dismissing restoration as speculative and psychologically driven rather than medically substantiated. [49]" | F040 Loaded Language | anti-circumcision | Reporting opponents' view: 'They argue that ethical focus should prioritize IMC's purported health advantages'. Opponents of restoration would not describe the advantages as 'purported', so the article's skeptical word is inserted into their own argument. This is the article-voice 'purported' convention flagged elsewhere in this audit. (sentence 191) |

Flag tally by side (simple count of the table above): anti-circumcision 1; pro-circumcision 1.

## Both-sides balance note

Same-standard check: restoration benefits are consistently held to an RCT standard and marked as self-reported. The lead holds circumcision's lack of detriments to no stated standard ('robust'), which is an asymmetry in favor of the pro side. On the anti side, ethicists' rebuttal (192) includes 'circumcision's failure to eradicate infections entirely', a nirvana-style standard, but it is attributed and was not counted as the article's reasoning. Sentence 183 ('inflicts irreversible harm') reads as a continuation of proponents' contention in sentence 182; it was not flagged, but it is close to article voice.

## What wasn't checked

- Sentences outside the reading set (159 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- The historical claims (epispasm in antiquity, 2) and survey figures (1,192 respondents, 85%) were not checked against sources.
