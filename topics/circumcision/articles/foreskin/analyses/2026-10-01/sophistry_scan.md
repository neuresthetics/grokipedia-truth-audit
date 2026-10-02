# Sophistry and fallacy scan: Foreskin

- **Article:** Foreskin
- **URL:** https://grokipedia.com/page/Foreskin
- **Snapshot file:** `topics/circumcision/articles/foreskin/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9 fallacy scan, run 2 (full read, blind rerun). Both-sides by default; no outside fact-checking.
- **Reading coverage:** 231/231 units read in full (226 paragraphs, 5 table rows).

## Verdict

Run 2 found 5 flags: 5 pro, 0 anti, and 0 neutral. The lean is pro. Main patterns were F036 Suppressed Evidence (3); F032 Cum Hoc (1); F040 Loaded Language (1). Flags are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug foreskin` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 7231 |
| Sentences (prose + list items; headings and tables excluded) | 225 |
| Sentences with no citation marker of their own | 25 (11%) |
| Paragraphs/list items with no citation marker at all | 3 of 73 |
| Table rows (not counted as sentences) | 5 |
| Sources listed in sources CSV | 165 |
| Distinct citation numbers used in text | 165 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 4 | 0.6 | prominent (2), great (1), unique (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 1 | 0.1 | purported (1) |
| MOS:WTW editorializing | 2 | 0.3 | only (2) |
| MOS:WTW connectives (but/despite/however...) | 63 | 8.7 | though (32), while (13), but (12), however (5), despite (1) |
| MOS:WTW synonyms for 'said' | 8 | 1.1 | confirm (2), expose (2), assert (1), find (1), note (1) |
| Hyland 2005 hedges | 104 | 14.4 | approximately (12), often (12), may (11), typically (11), around (7) |
| Hyland 2005 boosters | 16 | 2.2 | certain (3), known (3), show (3), demonstrated (2), shows (2) |

## Flags

Every flag below is a **judgment call** based on the run 2 reading, not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false.

| n | quote | Fxxx Name | side | note |
|---:|---|---|---|---|
| 1 | "The glans penis itself contains thousands of specialized nerve endings (around 4,000–8,000 axons/receptors), forming the primary site for erogenous sensation, which remains unaffected by circumcision." | F036 Suppressed Evidence | pro | States flatly that glans sensation is unaffected, leaving out the article's own account that exposure after circumcision keratinizes and coarsens the glans surface. |
| 2 | "The condition is nearly absent in circumcised populations, underscoring the foreskin's role in harboring oncogenic factors like high-risk HPV strains, which are 32-43% less prevalent post-circumcision per systematic reviews." | F032 Cum Hoc | pro | Takes an association (OR about 0.33, so not 'nearly absent') as showing the foreskin's causal role. |
| 3 | "Intactivist narratives promoting the foreskin as possessing uniquely dense nerve endings for erotogenic purposes are contradicted by histological studies revealing lower specialized nerve density compared to the glans, with no empirical link to superior pleasure." | F036 Suppressed Evidence | pro | Calls the claim contradicted while leaving out the article's own anatomy section, which says preputial corpuscular endings are up to 10 times denser than in the glans. |
| 4 | "These evaluations, drawn from peer-reviewed analyses, underscore a pattern where advocacy prioritizes absolutist positions over causal evidence from prospective trials." | F040 Loaded Language | pro | The article's own summary labels opponents 'absolutist'. Loaded framing caps a section that presents only one side. |
| 5 | "Systematic reviews confirm no adverse impacts on sexual function, sensitivity, or satisfaction from circumcision, countering claims of foreskin-specific erogenous loss, as glans keratinization does not demonstrably impair overall penile sensation in controlled studies." | F036 Suppressed Evidence | pro | Presents the evidence as settled ('confirm no adverse impacts'), though the lead says empirical studies on sensitivity are conflicting. |

## Both-sides balance note

Run 2 flag counts by side: pro 5, anti 0, neutral 0. These are judgment-based labels, not measurements.

## What wasn't checked

- No outside fact-checking or source verification was performed.
- Labels are judgment-based flags, not computed findings.
- Reproducibility comparison: [COMPARISON.md](../../../../runs/2026-10-01_run2_full/COMPARISON.md).
