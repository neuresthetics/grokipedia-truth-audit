# Sophistry and fallacy scan: Female genital mutilation in the United States

- **Article:** Female genital mutilation in the United States
- **URL:** https://grokipedia.com/page/Female_genital_mutilation_in_the_United_States
- **Snapshot file:** `articles/female-genital-mutilation-in-the-united-states/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9 fallacy scan, run 2 (full read, blind rerun). Both-sides by default; no outside fact-checking.
- **Reading coverage:** 187/187 units read in full (187 paragraphs, 0 table rows).

## Verdict

Run 2 found 5 flags: 0 pro, 5 anti, and 0 neutral. The lean is anti. Main patterns were F034 False Cause (1); F002 Straw Man (1); F001 Ad Hominem (1); F010 Appeal to Ignorance (1); F011 Hasty Generalization (1). Flags are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug female-genital-mutilation-in-the-united-states` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 6380 |
| Sentences (prose + list items; headings and tables excluded) | 187 |
| Sentences with no citation marker of their own | 28 (15%) |
| Paragraphs/list items with no citation marker at all | 1 of 67 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 103 |
| Distinct citation numbers used in text | 103 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 1 | 0.2 | notable (1) |
| MOS:WTW contentious labels | 1 | 0.2 | sect (1) |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 1 | 0.2 | purported (1) |
| MOS:WTW editorializing | 1 | 0.2 | only (1) |
| MOS:WTW connectives (but/despite/however...) | 36 | 5.6 | despite (13), though (9), but (6), while (6), however (2) |
| MOS:WTW synonyms for 'said' | 10 | 1.6 | reveal (6), expose (2), claim (1), clarify (1) |
| Hyland 2005 hedges | 77 | 12.1 | often (10), rather (10), claims (7), approximately (6), estimated (6) |
| Hyland 2005 boosters | 20 | 3.1 | certain (5), show (5), established (3), demonstrate (1), demonstrated (1) |

## Flags

Every flag below is a **judgment call** based on the run 2 reading, not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false.

| n | quote | Fxxx Name | side | note |
|---:|---|---|---|---|
| 1 | "Causal mechanisms stem from anatomical disruption and associated trauma, independent of confounding social factors in migrant contexts." | F034 False Cause | anti | Asserts that the causal attribution holds independent of confounders, with no analysis cited, after citing correlational survey data. |
| 2 | "Proponents of relativism often frame FGM as a private cultural rite, such as informal "cutting ceremonies" conducted in immigrant enclaves, thereby excusing non-consensual procedures on minors as beyond external judgment." | F002 Straw Man | anti | Attributes to unnamed 'proponents of relativism' a position of 'excusing non-consensual procedures', a weak version that is then refuted. |
| 3 | "Sources advancing relativism, often from anthropological circles, exhibit selective application by condemning equivalent male practices less rigorously, revealing inconsistency rather than principled neutrality." | F001 Ad Hominem | anti | Dismisses the relativist position by charging its sources with inconsistency rather than answering the argument. It also asserts the male practices are 'equivalent'. |
| 4 | "Despite an estimated at-risk population exceeding 500,000 girls and women from high-prevalence immigrant communities, the paucity of documented cases post-2017 suggests potential deterrence effects from heightened awareness and legal risks, though underreporting remains a challenge." | F010 Appeal to Ignorance | anti | Takes the absence of documented cases as evidence that deterrence works, while the same sentence and section stress underreporting. |
| 5 | "Without such imperatives, assimilation falters, as evidenced by ongoing clandestine networks, reinforcing arguments that education alone insufficiently supplants entrenched norms without legal compulsion and cultural integration requirements." | F011 Hasty Generalization | anti | Generalizes from the existence of clandestine networks to a claim that assimilation fails without legal compulsion and vetting. |

## Both-sides balance note

Run 2 flag counts by side: pro 0, anti 5, neutral 0. These are judgment-based labels, not measurements.

## What wasn't checked

- No outside fact-checking or source verification was performed.
- Labels are judgment-based flags, not computed findings.
- Reproducibility comparison: [COMPARISON.md](../../../SOPHISTRY_RERUN_2026-10-01/COMPARISON.md).
