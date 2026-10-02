# Sophistry and fallacy scan: Prohibition of Female Circumcision Act 1985

- **Article:** Prohibition of Female Circumcision Act 1985
- **URL:** https://grokipedia.com/page/prohibition_of_female_circumcision_act_1985
- **Snapshot file:** `topics/circumcision/articles/prohibition-of-female-circumcision-act-1985/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9 fallacy scan, run 2 (full read, blind rerun). Both-sides by default; no outside fact-checking.
- **Reading coverage:** 122/122 units read in full (122 paragraphs, 0 table rows).

## Verdict

Run 2 found 6 flags: 3 pro, 2 anti, and 1 neutral. The lean is pro. Main patterns were F040 Loaded Language (2); F073 McNamara Fallacy (1); F033 Causal Oversimplification (1); F002 Straw Man (1); F036 Suppressed Evidence (1). Flags are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug prohibition-of-female-circumcision-act-1985` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 4486 |
| Sentences (prose + list items; headings and tables excluded) | 122 |
| Sentences with no citation marker of their own | 34 (28%) |
| Paragraphs/list items with no citation marker at all | 5 of 47 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 43 |
| Distinct citation numbers used in text | 43 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 0 | 0.0 | none |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 1 | 0.2 | purported (1) |
| MOS:WTW editorializing | 5 | 1.1 | only (5) |
| MOS:WTW connectives (but/despite/however...) | 29 | 6.5 | while (9), despite (8), though (5), but (4), although (2) |
| MOS:WTW synonyms for 'said' | 1 | 0.2 | assert (1) |
| Hyland 2005 hedges | 39 | 8.7 | rather (9), often (8), typically (5), could (3), indicate (3) |
| Hyland 2005 boosters | 8 | 1.8 | certain (3), demonstrated (1), incontrovertible (1), known (1), realized (1) |

## Flags

Every flag below is a **judgment call** based on the run 2 reading, not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false.

| n | quote | Fxxx Name | side | note |
|---:|---|---|---|---|
| 1 | "The empirical record of zero convictions under the Act demonstrated its primarily symbolic function, with no deterrent effect evidenced in court outcomes." | F073 McNamara Fallacy | neutral | Conviction counts are treated as the measure of deterrence. Zero convictions cannot show the absence of a deterrent effect. |
| 2 | "Cultural relativism influenced enforcement shortcomings, with police and social services often prioritizing community cohesion over child protection, influenced by diversity training that emphasized sensitivity to immigrant customs and discouraged interventions perceived as culturally insensitive." | F033 Causal Oversimplification | anti | Enforcement failure is attributed mainly to diversity training and relativism, though the article itself lists other causes (secrecy, evidentiary hurdles, resource limits). |
| 3 | "Narratives attributing FGM persistence solely to socioeconomic factors like poverty have been overstated, as empirical data show the practice occurring across income levels within affected diasporas, driven fundamentally by ritualistic and patriarchal traditions rather than economic deprivation alone." | F002 Straw Man | anti | Rebuts an unattributed 'solely socioeconomic' position that the article does not show anyone holding. |
| 4 | "Parliamentary discussions during the Bill's passage highlighted medical testimonies on irreversible damage over unsubstantiated equivalence to benign rituals, underscoring that tolerance of mutilatory customs undermines the state's duty to minors irrespective of origin." | F040 Loaded Language | pro | The article's own voice calls the male/female comparison an 'unsubstantiated equivalence to benign rituals', a loaded dismissal of the comparison. |
| 5 | "While ethical scrutiny of non-therapeutic infant male circumcision persists—citing potential loss of erogenous tissue and autonomy violations—the absence of equivalent regulation does not negate FGM's empirically greater morbidity, as evidenced by global health data showing FGM's complication rates far exceeding those of male circumcision (e.g., up to 15-30% acute issues in some FGM types versus under 1% for males in controlled settings)." | F036 Suppressed Evidence | pro | Pairs the worst FGM types in uncontrolled settings against male circumcision in controlled settings, a mismatched comparison that inflates the contrast. |
| 6 | "This distinction reflects causal prioritization of documented outcomes over superficial procedural analogies, rather than cultural or gender bias." | F040 Loaded Language | pro | Labels the opposing analogy 'superficial' and asserts the absence of bias without supporting it. |

## Both-sides balance note

Run 2 flag counts by side: pro 3, anti 2, neutral 1. These are judgment-based labels, not measurements.

## What wasn't checked

- No outside fact-checking or source verification was performed.
- Labels are judgment-based flags, not computed findings.
- Reproducibility comparison: [COMPARISON.md](../../../../runs/2026-10-01_run2_full/COMPARISON.md).
