# Sophistry and fallacy scan: Female genital mutilation in the United Kingdom

- **Article:** Female genital mutilation in the United Kingdom
- **URL:** https://grokipedia.com/page/female_genital_mutilation_in_the_united_kingdom
- **Snapshot file:** `articles/female-genital-mutilation-in-the-united-kingdom/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9 fallacy scan, run 2 (full read, blind rerun). Both-sides by default; no outside fact-checking.
- **Reading coverage:** 173/173 units read in full (173 paragraphs, 0 table rows).

## Verdict

Run 2 found 3 flags: 0 pro, 3 anti, and 0 neutral. The lean is anti. Main patterns were F040 Loaded Language (1); F002 Straw Man (1); F010 Appeal to Ignorance (1). Flags are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug female-genital-mutilation-in-the-united-kingdom` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 5906 |
| Sentences (prose + list items; headings and tables excluded) | 168 |
| Sentences with no citation marker of their own | 51 (30%) |
| Paragraphs/list items with no citation marker at all | 10 of 59 |
| Table rows (not counted as sentences) | 4 |
| Sources listed in sources CSV | 54 |
| Distinct citation numbers used in text | 54 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 5 | 0.8 | notable (3), landmark (1), prominent (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 1 | 0.2 | accused (1) |
| MOS:WTW editorializing | 10 | 1.7 | only (10) |
| MOS:WTW connectives (but/despite/however...) | 44 | 7.5 | though (15), despite (13), but (10), while (5), however (1) |
| MOS:WTW synonyms for 'said' | 2 | 0.3 | confirm (1), reveal (1) |
| Hyland 2005 hedges | 73 | 12.4 | often (13), rather (13), estimated (11), indicate (7), may (6) |
| Hyland 2005 boosters | 15 | 2.5 | known (5), found (3), showed (3), demonstrates (1), must (1) |

## Flags

Every flag below is a **judgment call** based on the run 2 reading, not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false.

| n | quote | Fxxx Name | side | note |
|---:|---|---|---|---|
| 1 | "These changes reflected causal links between lax prior enforcement—zero convictions from 1985 to 2014—and persistent cultural practices, prioritizing empirical deterrence over multicultural relativism." | F040 Loaded Language | anti | Loaded framing that labels the alternative 'multicultural relativism' and asserts 'causal links' that are not shown. |
| 2 | "The evolution demonstrates a shift from narrow prohibition to comprehensive risk-based criminalization, grounded in verifiable prevalence data rather than unsubstantiated claims of rarity." | F002 Straw Man | anti | Sets the law against an unnamed 'claims of rarity' position. It also calls the prevalence data 'verifiable', though the article earlier says the figures are extrapolations resting on assumptions. |
| 3 | "Earlier modeling estimated around 137,000 women and girls born in FGM-practicing countries residing in England and Wales, with approximately 103,000 aged 15–49 estimated to have undergone FGM (as of 2011 data), a figure likely conservative given subsequent immigration and the absence of eradication evidence." | F010 Appeal to Ignorance | anti | Uses the absence of evidence of eradication as support for higher prevalence. |

## Both-sides balance note

Run 2 flag counts by side: pro 0, anti 3, neutral 0. These are judgment-based labels, not measurements.

## What wasn't checked

- No outside fact-checking or source verification was performed.
- Labels are judgment-based flags, not computed findings.
- Reproducibility comparison: [COMPARISON.md](../../../SOPHISTRY_RERUN_2026-10-01/COMPARISON.md).
