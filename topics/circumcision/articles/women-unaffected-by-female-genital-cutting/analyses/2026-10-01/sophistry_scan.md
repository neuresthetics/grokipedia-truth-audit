# Sophistry and fallacy scan: Women unaffected by female genital cutting

- **Article:** Women unaffected by female genital cutting
- **URL:** https://grokipedia.com/page/Women_unaffected_by_female_genital_cutting
- **Snapshot file:** `articles/women-unaffected-by-female-genital-cutting/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9 fallacy scan, run 2 (full read, blind rerun). Both-sides by default; no outside fact-checking.
- **Reading coverage:** 151/151 units read in full (147 paragraphs, 4 table rows).

## Verdict

Run 2 found 14 flags: 14 pro, 0 anti, and 0 neutral. The lean is pro. Main patterns were F011 Hasty Generalization (4); F040 Loaded Language (3); F013 False Dilemma (2); F002 Straw Man (1); F026 Poisoning the Well (1); F001 Ad Hominem (1); F032 Cum Hoc (1); F034 False Cause (1). Flags are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug women-unaffected-by-female-genital-cutting` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 4854 |
| Sentences (prose + list items; headings and tables excluded) | 146 |
| Sentences with no citation marker of their own | 41 (28%) |
| Paragraphs/list items with no citation marker at all | 1 of 47 |
| Table rows (not counted as sentences) | 4 |
| Sources listed in sources CSV | 56 |
| Distinct citation numbers used in text | 56 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 0 | 0.0 | none |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 4 | 0.8 | only (4) |
| MOS:WTW connectives (but/despite/however...) | 31 | 6.4 | while (10), but (8), though (8), despite (4), however (1) |
| MOS:WTW synonyms for 'said' | 7 | 1.4 | reveal (6), assert (1) |
| Hyland 2005 hedges | 89 | 18.3 | often (22), rather (16), may (9), approximately (5), indicate (5) |
| Hyland 2005 boosters | 17 | 3.5 | found (7), showed (3), show (2), believed (1), certain (1) |

## Flags

Every flag below is a **judgment call** based on the run 2 reading, not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false.

| n | quote | Fxxx Name | side | note |
|---:|---|---|---|---|
| 1 | "This group comprises the overwhelming majority of the world's approximately four billion females, as female genital cutting affects only over 230 million girls and women alive today, concentrated in about 30 countries across Africa (144 million cases), Asia (over 80 million), and parts of the Middle East." | F040 Loaded Language | pro | The word 'only' minimizes a figure of 230 million. |
| 2 | "The mutilation narrative, dominant in Western human rights and media discourses, posits inherent physical, sexual, and psychological devastation, often extrapolating from severe Type III infibulation cases (prevalent in <10% of instances globally) to all forms, while downplaying self-reports of normalcy." | F002 Straw Man | pro | Straw man: the opposing view is characterized as extrapolating from infibulation to all forms. |
| 3 | "This supports cutting proponents' view that pathologizing narratives amplify harm via social exclusion, as institutional emphases on mutilation—often from ideologically aligned NGOs—overlook resilience in unaffected women who report intact pleasure and well-being, per community-based surveys in Mali and Sierra Leone (e.g., 70-80% satisfaction rates in ritual contexts)." | F026 Poisoning the Well | pro | Poisons the well against NGO sources by calling them 'ideologically aligned' instead of engaging their evidence. |
| 4 | "Such distinctions reveal how source biases, including ethnocentric assumptions in academia, skew toward harm amplification over causal disaggregation of cultural versus procedural impacts." | F001 Ad Hominem | pro | Rejects harm findings by attributing ethnocentric bias to the researchers. |
| 5 | "In Demographic and Health Surveys (DHS) conducted across countries where female genital cutting (FGC) is prevalent, substantial proportions of women who have undergone the procedure express support for its continuation, indicating a lack of perceived personal detriment to well-being." | F011 Hasty Generalization | pro | Infers that women perceive no personal harm from their support for continuing the practice for daughters, which the article elsewhere ties to social-norm pressure. |
| 6 | "This suggests that reported physical complaints in FGC-affected women may often stem from stigma or access barriers rather than the cutting procedure." | F011 Hasty Generalization | pro | Generalizes from a single cross-sectional diaspora study to FGC-affected women in general. |
| 7 | "Cohort studies report no procedure-independent elevation in physical morbidities, with adverse events more tied to social exclusion than anatomical changes (e.g., 16.6% recent gynecological events unrelated to FGC status)." | F011 Hasty Generalization | pro | Applies findings from a mostly Type I/II Somali-American sample (the 16.6% figure) to Type III infibulation. |
| 8 | "Psychological distress, when present, correlates more strongly with migration-induced acculturation stress or anti-FGC campaigns than the cutting event itself, per longitudinal self-reports." | F032 Cum Hoc | pro | Treats a correlation as showing that distress comes from campaigns rather than from cutting. |
| 9 | "These accounts challenge pathologizing frameworks, emphasizing subjective normalcy over imposed victimhood." | F040 Loaded Language | pro | 'Pathologizing' and 'imposed victimhood' are loaded framing of the harm position. |
| 10 | "This suggests that social determinants, rather than the cutting itself, drive many reported harms, challenging direct causal attributions in global narratives." | F011 Hasty Generalization | pro | Draws a global causal conclusion from one adjusted cross-sectional study. |
| 11 | "Empirical links between FGC and systemic patriarchy remain weakly established, as practices are frequently initiated and controlled by women for social cohesion, not male dominance, and reports of fulfilling sexual lives post-cutting contradict narratives of inherent debilitation." | F013 False Dilemma | pro | False dilemma: women's enforcement of the practice is treated as excluding patriarchal causation. |
| 12 | "These findings imply that anti-FGC campaigns may amplify harms through stigmatization and eroded healthcare trust, prioritizing ideological uniformity over context-specific evidence." | F040 Loaded Language | pro | 'Ideological uniformity' is loaded characterization of the campaigns. |
| 13 | "Demographic and Health Surveys (DHS) across practicing countries corroborate higher endorsement rates among women compared to men, underscoring self-perpetuation over imposed victimhood." | F013 False Dilemma | pro | Frames women's support and victimhood as mutually exclusive. |
| 14 | "The persistence of cutting despite billions in funding—such as the Joint Programme's focus on attitude shifts yielding only modest, non-sustained behavioral changes—suggests campaigns overlook practitioner perspectives that prioritize cultural continuity over Western-framed harm narratives." | F034 False Cause | pro | Attributes persistence to campaigns overlooking practitioners, without evidence for that cause. Population growth is noted elsewhere. |

## Both-sides balance note

Run 2 flag counts by side: pro 14, anti 0, neutral 0. These are judgment-based labels, not measurements.

## What wasn't checked

- No outside fact-checking or source verification was performed.
- Labels are judgment-based flags, not computed findings.
- Reproducibility comparison: [COMPARISON.md](../../../SOPHISTRY_RERUN_2026-10-01/COMPARISON.md).
