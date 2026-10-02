# Sophistry and fallacy scan: Female genital mutilation in India

- **Article:** Female genital mutilation in India
- **URL:** https://grokipedia.com/page/Female_genital_mutilation_in_India
- **Snapshot file:** `articles/female-genital-mutilation-in-india/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9 fallacy scan, run 2 (full read, blind rerun). Both-sides by default; no outside fact-checking.
- **Reading coverage:** 200/200 units read in full (200 paragraphs, 0 table rows).

## Verdict

Run 2 found 3 flags: 3 pro, 0 anti, and 0 neutral. The lean is pro. Main patterns were F011 Hasty Generalization (1); F034 False Cause (1); F002 Straw Man (1). Flags are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug female-genital-mutilation-in-india` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 7243 |
| Sentences (prose + list items; headings and tables excluded) | 201 |
| Sentences with no citation marker of their own | 35 (17%) |
| Paragraphs/list items with no citation marker at all | 0 of 74 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 96 |
| Distinct citation numbers used in text | 97 |
| Dangling citation numbers (used, no source row) | 1: 97 |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 1 | 0.1 | unique (1) |
| MOS:WTW contentious labels | 8 | 1.1 | sect (8) |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 2 | 0.3 | purported (2) |
| MOS:WTW editorializing | 3 | 0.4 | only (3) |
| MOS:WTW connectives (but/despite/however...) | 50 | 6.9 | despite (15), though (12), while (11), but (9), however (3) |
| MOS:WTW synonyms for 'said' | 8 | 1.1 | assert (2), claim (2), confirm (2), deny (1), reveal (1) |
| Hyland 2005 hedges | 103 | 14.2 | rather (19), often (17), may (11), claims (10), indicate (9) |
| Hyland 2005 boosters | 16 | 2.2 | known (8), established (4), certain (2), demonstrated (1), found (1) |

## Flags

Every flag below is a **judgment call** based on the run 2 reading, not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false.

| n | quote | Fxxx Name | side | note |
|---:|---|---|---|---|
| 1 | "Unlike male circumcision, which epidemiological studies link to reduced risks of urinary tract infections, penile cancer, and heterosexual HIV transmission in high-prevalence settings, FGM lacks any verifiable medical justification and consistently correlates with adverse outcomes, including immediate risks of hemorrhage, infection, and shock, as well as long-term issues like chronic pain, urinary problems, sexual dysfunction, and increased maternal mortality from childbirth complications." | F011 Hasty Generalization | pro | In a section on Type Ia (prepuce-only) khatna, outcomes of the severe types (e.g. maternal mortality from childbirth complications) are attributed to FGM generally to draw the male/female contrast. |
| 2 | "These risks stem causally from procedural factors like lack of medical oversight, rather than inherent severity, as khatna aligns with WHO Type Ib cutting." | F034 False Cause | pro | Asserts without support that the harms come from setting rather than the cut itself, which the article later contradicts by saying medicalized khatna yields the same core harms. |
| 3 | "This tension underscores a causal divide: UN absolutism assumes uniform harm across contexts, yet empirical gaps in Asia-specific prevalence data—reliant on self-reported surveys—limit verification, with India's non-endorsement of targeted conventions preserving space for community defenses rooted in religious freedom." | F002 Straw Man | pro | Restates the UN position as an assumption of 'uniform harm' and labels it 'absolutism', though the article itself describes WHO's typology as graded by type. |

## Both-sides balance note

Run 2 flag counts by side: pro 3, anti 0, neutral 0. These are judgment-based labels, not measurements.

## What wasn't checked

- No outside fact-checking or source verification was performed.
- Labels are judgment-based flags, not computed findings.
- Reproducibility comparison: [COMPARISON.md](../../../SOPHISTRY_RERUN_2026-10-01/COMPARISON.md).
