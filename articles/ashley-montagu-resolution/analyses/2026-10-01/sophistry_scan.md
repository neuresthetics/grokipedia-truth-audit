# Sophistry and fallacy scan: Ashley Montagu Resolution

- **Article:** Ashley Montagu Resolution
- **URL:** https://grokipedia.com/page/ashley_montagu_resolution
- **Snapshot file:** `articles/ashley-montagu-resolution/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9 fallacy scan, run 2 (full read, blind rerun). Both-sides by default; no outside fact-checking.
- **Reading coverage:** 194/194 units read in full (194 paragraphs, 0 table rows).

## Verdict

Run 2 found 4 flags: 2 pro, 0 anti, and 2 neutral. The lean is mixed (pro/neutral tie). Main patterns were F026 Poisoning the Well (1); F010 Appeal to Ignorance (1); F011 Hasty Generalization (1); F040 Loaded Language (1). Flags are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug ashley-montagu-resolution` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 6835 |
| Sentences (prose + list items; headings and tables excluded) | 189 |
| Sentences with no citation marker of their own | 40 (21%) |
| Paragraphs/list items with no citation marker at all | 2 of 62 |
| Table rows (not counted as sentences) | 1 |
| Sources listed in sources CSV | 59 |
| Distinct citation numbers used in text | 59 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 1 | 0.1 | notable (1) |
| MOS:WTW contentious labels | 1 | 0.1 | myth (1) |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 3 | 0.4 | purported (3) |
| MOS:WTW editorializing | 3 | 0.4 | only (2), notably (1) |
| MOS:WTW connectives (but/despite/however...) | 55 | 8.0 | while (18), though (16), but (10), despite (7), however (4) |
| MOS:WTW synonyms for 'said' | 2 | 0.3 | confirm (1), expose (1) |
| Hyland 2005 hedges | 52 | 7.6 | rather (16), often (8), claims (7), argue (3), argued (3) |
| Hyland 2005 boosters | 10 | 1.5 | certain (3), show (2), demonstrated (1), established (1), known (1) |

## Flags

Every flag below is a **judgment call** based on the run 2 reading, not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false.

| n | quote | Fxxx Name | side | note |
|---:|---|---|---|---|
| 1 | "These efforts positioned Montagu as a key figure in postwar antiracist science, though institutional biases in mid-20th-century anthropology often amplified environmental explanations at the expense of causal genetic mechanisms." | F026 Poisoning the Well | neutral | Discounts Montagu's anthropology by attributing it to institutional bias rather than engaging its evidence. The topic is race science, not circumcision. |
| 2 | "The absence of robust initial pushback underscores a broader academic tendency to prioritize aggregated health data over absolutist ethical petitions, potentially influenced by systemic alignments with prevailing clinical norms." | F010 Appeal to Ignorance | neutral | Draws a positive conclusion about academic tendencies from an absence of responses. The silence is compatible with many explanations, including simple neglect of a niche petition. |
| 3 | "Key limitations stemmed from evidentiary and framing challenges: the resolution's categorical condemnation overlooked systematic reviews documenting net health benefits for neonatal male circumcision, including 50-60% reductions in heterosexual HIV acquisition and lower urinary tract infection risks in infancy." | F011 Hasty Generalization | pro | The HIV reduction comes from adult trials in high-prevalence settings and is cited as a benefit of neonatal circumcision in general. |
| 4 | "This absolutist equation of all genital modifications ignored procedural severities—female genital mutilation (FGM) Types II-III often entail greater tissue loss and complications like vesicovaginal fistulae—undermining broader acceptance amid cultural entrenchment and medical endorsements." | F040 Loaded Language | pro | Calls the resolution 'absolutist' and says it 'ignored' severity, though the article itself reports the proponents' argument that severity differences do not negate the shared harm. |

## Both-sides balance note

Run 2 flag counts by side: pro 2, anti 0, neutral 2. These are judgment-based labels, not measurements.

## What wasn't checked

- No outside fact-checking or source verification was performed.
- Labels are judgment-based flags, not computed findings.
- Reproducibility comparison: [COMPARISON.md](../../../SOPHISTRY_RERUN_2026-10-01/COMPARISON.md).
