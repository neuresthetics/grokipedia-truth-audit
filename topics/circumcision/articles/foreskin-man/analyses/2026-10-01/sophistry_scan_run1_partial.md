> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: Foreskin Man

- **Article:** Foreskin Man
- **URL:** https://grokipedia.com/page/Foreskin_Man
- **Snapshot file:** `articles/foreskin-man/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (5 sentences) read in full, plus 36 of 110 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This article is about an advocacy comic, so most of the circumcision-related claims are the comic's or its critics' and are attributed. The health-evidence section is balanced: it gives the RCT findings with low-prevalence caveats, says sensitivity evidence is 'mixed', and covers AAP/CDC positions (62-74). The article also cautions against causal claims about the comic's influence (103, 114). One flag was found: the lead says in the article's voice that the comic contributed to 'the measure's defeat'. The body's own caution about causal links is not applied to this claim, and the ballot history needs a source check. Lean: 0 pro, 0 anti, 1 neutral/structural. This is a judgment call.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug foreskin-man` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 4069 |
| Sentences (prose + list items; headings and tables excluded) | 115 |
| Sentences with no citation marker of their own | 15 (13%) |
| Paragraphs/list items with no citation marker at all | 0 of 44 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 82 |
| Distinct citation numbers used in text | 82 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 1 | 0.2 | leading (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 2 | 0.5 | purported (2) |
| MOS:WTW editorializing | 1 | 0.2 | arguably (1) |
| MOS:WTW connectives (but/despite/however...) | 36 | 8.8 | but (11), while (11), though (7), however (4), despite (3) |
| MOS:WTW synonyms for 'said' | 2 | 0.5 | find (1), note (1) |
| Hyland 2005 hedges | 43 | 10.6 | rather (12), approximately (6), around (5), claims (5), argued (3) |
| Hyland 2005 boosters | 7 | 1.7 | certain (2), known (2), demonstrated (1), established (1), find (1) |

## Flags

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "The comics, available in print and digital formats, have sparked significant controversy, particularly for caricatures perceived as invoking anti-Semitic tropes through blond, Aryan-like heroism clashing with hook-nosed mohels, leading even fellow activists to distance themselves and contributing to the measure's defeat amid broader backlash. [1] [6]" | F031 Post Hoc | neutral/structural | Lead, article voice: the controversy led activists to distance themselves 'and contribut[ed] to the measure's defeat amid broader backlash'. The defeat follows the controversy in time, but no evidence of contribution is given in the sentence. Sentences 103 and 114 decline to assert causal links for the comic's other effects, so the lead is held to a looser standard. The ballot-measure history (90, 105) needs a source check; no verdict is given here. (sentence 4) |

Flag tally by side (simple count of the table above): neutral/structural 1.

## Both-sides balance note

Same-standard check: 'purported' is used in the article's voice for both sides, 'purported ethical violations' (37) and 'Purported benefits' (57), so the loaded-term use is symmetric here and was not flagged. Critics' charge of 'fear-mongering' (88) and 'sensationalism' (102) and supporters' claims of 'amplifying awareness' (92) are both reported. The article notes that the comic sidelines RCT data (91), and it also notes the small absolute benefits in low-risk settings (64, 67), so the evidence context cuts both ways.

## What wasn't checked

- Sentences outside the reading set (74 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- The San Francisco ballot history (23.7% support figure in sentence 90; 'defeat' in sentences 4 and 105) was not checked against sources.
