# Sophistry and fallacy scan: Infibulation

- **Article:** Infibulation
- **URL:** https://grokipedia.com/page/Infibulation
- **Snapshot file:** `articles/infibulation/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9 fallacy scan, run 2 (full read, blind rerun). Both-sides by default; no outside fact-checking.
- **Reading coverage:** 187/187 units read in full (187 paragraphs, 0 table rows).

## Verdict

Run 2 found 3 flags: 2 pro, 0 anti, and 1 neutral. The lean is pro. Main patterns were F033 Causal Oversimplification (1); F036 Suppressed Evidence (1); F032 Cum Hoc (1). Flags are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug infibulation` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 6294 |
| Sentences (prose + list items; headings and tables excluded) | 187 |
| Sentences with no citation marker of their own | 25 (13%) |
| Paragraphs/list items with no citation marker at all | 0 of 69 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 126 |
| Distinct citation numbers used in text | 126 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 1 | 0.2 | landmark (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 4 | 0.6 | only (3), notably (1) |
| MOS:WTW connectives (but/despite/however...) | 53 | 8.4 | but (15), though (14), while (11), despite (10), however (2) |
| MOS:WTW synonyms for 'said' | 7 | 1.1 | reveal (3), confirm (2), claim (1), insist (1) |
| Hyland 2005 hedges | 72 | 11.4 | rather (15), often (14), typically (8), indicate (5), could (4) |
| Hyland 2005 boosters | 19 | 3.0 | certain (4), show (3), shows (3), believe (1), believed (1) |

## Flags

Every flag below is a **judgment call** based on the run 2 reading, not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false.

| n | quote | Fxxx Name | side | note |
|---:|---|---|---|---|
| 1 | "The practice exhibits marked gender asymmetry, with female infibulation imposing irreversible narrowing of the birth canal to constrain sexual access and reproduction—far exceeding male circumcision's scope—due to the evolutionary and economic imperatives of paternal investment in high-dependency offspring within resource-scarce, agrarian contexts." | F033 Causal Oversimplification | pro | Explains the female/male asymmetry with one speculative evolutionary-economic cause, presented as fact, to support the male/female distinction. |
| 2 | "Anatomically, male circumcision removes a fold of skin (the foreskin) that protects the glans but does not fundamentally alter penile erectile, urinary, or sensory functions, whereas infibulation excises the clitoris—the primary site of female sexual pleasure and orgasm—and constructs a barrier that impedes natural vaginal function, often requiring repeated cutting for intercourse or childbirth." | F036 Suppressed Evidence | pro | Asserts that sensory function is unaltered while leaving out contrary evidence, to sharpen the male/female contrast. |
| 3 | "This reaction underscores causal limitations of top-down approaches, where coercion correlates with evasion rather than abandonment in low-capacity contexts." | F032 Cum Hoc | neutral | Moves from a correlation (coercion correlates with evasion) to a 'causal' limitation of top-down approaches. |

## Both-sides balance note

Run 2 flag counts by side: pro 2, anti 0, neutral 1. These are judgment-based labels, not measurements.

## What wasn't checked

- No outside fact-checking or source verification was performed.
- Labels are judgment-based flags, not computed findings.
- Reproducibility comparison: [COMPARISON.md](../../../SOPHISTRY_RERUN_2026-10-01/COMPARISON.md).
