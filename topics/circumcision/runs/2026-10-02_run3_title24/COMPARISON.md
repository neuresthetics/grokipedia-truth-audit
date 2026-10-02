# Sophistry scan: run 3 vs run 2 on the 24 'Title match' articles (2026-10-02)

## Conclusion (plain English)

Run 3 was a blind re-read of the same 24 articles under the same spec. It flagged **111** passages; run 2 had flagged **126** on these articles. Run 3 is a little more conservative (88% of run 2's volume), but it paints the same overall picture.

- **The direction reproduces.** Both runs judge the articles' own reasoning to tilt strongly toward circumcision. Pro flags are 84.0% of sided flags in run 2 and 82.7% in run 3.
- **The ranking of articles reproduces.** The Spearman correlation of per-article flag counts is **0.84**. ethics-of-circumcision and circumcision-controversies are the two heaviest articles in both runs. feast-of-the-circumcision-of-christ and history-of-circumcision have zero flags in both. forced-circumcision is the clearest anti-leaning article in both runs (7 anti flags each).
- **Article lean mostly reproduces: 17/24 articles get the same lean.** 7 of the 7 disagreements are on articles with 4 or fewer flags in both runs, where one flag can flip the lean. The 2 outright pro/anti reversal(s) (forced-circumcision-of-minors-in-south-korea, prevalence-of-circumcision) each rest on 1-4 flags per run.
- **Sentence-level agreement is moderate.** Run 3 re-flagged 77 of the 128 sentences/rows run 2 flagged, reproducing 60.2% of run 2. Unit-level Jaccard is 0.48, and 85 of the 162 sentences flagged by either run (52.5%) were flagged by only one. Neither run's list should be treated as complete.
- **On sentences both runs flagged, the side is nearly always the same (97.4%). The F-ID usually matches (79.2%).** Which way a lapse leans reproduces better than its exact label.
- **Types.** Stable: F040 Loaded Language, F010 Appeal to Ignorance, F003 Red Herring, F002 Straw Man, F026 Poisoning the Well, F042 False Analogy, F073 McNamara Fallacy, F022 Accident, F031 Post Hoc, F005 Appeal to Popularity, F028 Appeal to Tradition. Noisy: F036 Suppressed Evidence, F041 False Equivalence, F032 Cum Hoc, F055 Ecological Fallacy, F011 Hasty Generalization, F033 Causal Oversimplification, F034 False Cause. Lowest unit-level agreement among the judged types: F033 Causal Oversimplification (0.00), F055 Ecological Fallacy (0.00), F041 False Equivalence (0.11), F032 Cum Hoc (0.17). F055 Ecological Fallacy was used 7 times by run 2 and 0 times by run 3.

Bottom line: the article-level findings reproduce: a strong pro-circumcision tilt, the same heavy and light articles, and forced-circumcision as the main anti-leaning exception. The sentence-by-sentence flag lists overlap only moderately, so any single run's list is a sample of defensible flags, not an exhaustive or definitive inventory.

## 1. Totals and side split

|  | run 2 | run 3 |
|---|---|---|
| flags (24 articles) | 126 | 111 |
| pro | 100 | 86 |
| anti | 19 | 18 |
| neutral | 7 | 7 |
| pro share of sided flags (pro/(pro+anti)) | 84.0% | 82.7% |
| articles with zero flags | 5 | 2 |

Zero-flag articles. Run 2: circumcision-in-china, circumcision-in-the-bible, feast-of-the-circumcision-of-christ, history-of-circumcision, stapler-circumcision. Run 3: feast-of-the-circumcision-of-christ, history-of-circumcision.

## 2. Per-article counts side by side

Side columns are pro/anti/neutral. Lean = the larger of pro vs anti; 'tie' = equal and non-zero; 'none' = no sided flags.

| article | run 2 flags | run 2 p/a/n | run 2 lean | run 3 flags | run 3 p/a/n | run 3 lean | same lean |
|---|---|---|---|---|---|---|---|
| circumcision | 15 | 12/2/1 | pro | 6 | 6/0/0 | pro | yes |
| circumcision-and-hiv | 5 | 5/0/0 | pro | 2 | 2/0/0 | pro | yes |
| circumcision-and-law | 8 | 8/0/0 | pro | 6 | 6/0/0 | pro | yes |
| circumcision-controversies | 21 | 19/1/1 | pro | 13 | 13/0/0 | pro | yes |
| circumcision-controversy-in-early-christianity | 5 | 1/3/1 | anti | 4 | 1/3/0 | anti | yes |
| circumcision-in-africa | 9 | 9/0/0 | pro | 5 | 4/0/1 | pro | yes |
| circumcision-in-brunei | 1 | 1/0/0 | pro | 3 | 3/0/0 | pro | yes |
| circumcision-in-china | 0 | 0/0/0 | none | 3 | 3/0/0 | pro | **no** |
| circumcision-in-the-bible | 0 | 0/0/0 | none | 1 | 0/1/0 | anti | **no** |
| circumcision-of-jesus | 1 | 0/0/1 | none | 1 | 0/0/1 | none | yes |
| circumcision-surgical-procedure | 4 | 2/1/1 | pro | 2 | 1/1/0 | tie | **no** |
| cost-of-circumcision-surgery-in-chaozhou | 1 | 1/0/0 | pro | 2 | 1/0/1 | pro | yes |
| cultural-views-on-circumcision-aesthetics | 2 | 0/1/1 | anti | 3 | 1/1/1 | tie | **no** |
| ethics-of-circumcision | 24 | 24/0/0 | pro | 21 | 21/0/0 | pro | yes |
| feast-of-the-circumcision-of-christ | 0 | 0/0/0 | none | 0 | 0/0/0 | none | yes |
| forced-circumcision | 7 | 0/7/0 | anti | 7 | 0/7/0 | anti | yes |
| forced-circumcision-of-minors-in-south-korea | 1 | 0/1/0 | anti | 4 | 3/1/0 | pro | **no** |
| history-of-circumcision | 0 | 0/0/0 | none | 0 | 0/0/0 | none | yes |
| khitan-circumcision | 4 | 3/1/0 | pro | 4 | 4/0/0 | pro | yes |
| prevalence-of-circumcision | 1 | 1/0/0 | pro | 2 | 0/2/0 | anti | **no** |
| prohibition-of-female-circumcision-act-1985 | 6 | 3/2/1 | pro | 6 | 3/2/1 | pro | yes |
| religion-and-circumcision | 2 | 2/0/0 | pro | 4 | 2/0/2 | pro | yes |
| stapler-circumcision | 0 | 0/0/0 | none | 3 | 3/0/0 | pro | **no** |
| views-on-circumcision | 9 | 9/0/0 | pro | 9 | 9/0/0 | pro | yes |
| **TOTAL** | 126 | 100/19/7 |  | 111 | 86/18/7 |  | 17/24 |

- Spearman rank correlation of per-article flag counts (average ranks for ties, own implementation): **0.837** (n = 24).
- Article-lean agreement: **17/24**. Disagreements: circumcision-in-china, circumcision-in-the-bible, circumcision-surgical-procedure, cultural-views-on-circumcision-aesthetics, forced-circumcision-of-minors-in-south-korea, prevalence-of-circumcision, stapler-circumcision.
- Pro/anti reversals (one run pro, the other anti): **2** (forced-circumcision-of-minors-in-south-korea, prevalence-of-circumcision).

## 3. Sentence-level overlap

Unit = sentence or table row in the 2026-10-01 snapshot (segment.py). The per-unit detail is in comparison_units.csv.

| statistic (counts of model judgments) | value |
|---|---|
| units flagged by run 2 | 128 |
| units flagged by run 3 | 111 |
| matched (flagged by both) | 77 |
| run 2 only | 51 |
| run 3 only | 34 |
| Jaccard (matched / union) | 0.475 |
| share of run 2 units reproduced by run 3 | 60.2% |
| share of run 3 units also in run 2 | 69.4% |
| run 2 flags (not units) whose sentence run 3 also flagged | 77/126 (61.1%) |
| matched units with the same F-ID | 61/77 (79.2%) |
| matched units in the same F-ID category | 66/77 (85.7%) |
| matched units with the same side | 75/77 (97.4%) |

When a unit carries several flags in one run, 'same F-ID' and 'same side' mean the two runs' sets overlap.

## 4. Fallacy-type distribution and stability

Stable = at least 4 combined flags, unit-level Jaccard for that F-ID of at least 0.25, and count ratio (smaller/larger) of at least 0.5. Noisy = at least 4 combined flags but failing either test. These thresholds were chosen by hand; they are a reading aid, not a statistical test.

| F-ID | name | run 2 | run 2 % | run 3 | run 3 % | same unit both runs | Jaccard | count ratio | verdict |
|---|---|---|---|---|---|---|---|---|---|
| F040 | Loaded Language | 20 | 15.9% | 23 | 20.7% | 15 | 0.54 | 0.87 | stable |
| F036 | Suppressed Evidence | 12 | 9.5% | 11 | 9.9% | 4 | 0.21 | 0.92 | noisy |
| F010 | Appeal to Ignorance | 9 | 7.1% | 10 | 9.0% | 4 | 0.25 | 0.90 | stable |
| F003 | Red Herring | 8 | 6.3% | 8 | 7.2% | 6 | 0.60 | 1.00 | stable |
| F002 | Straw Man | 6 | 4.8% | 8 | 7.2% | 6 | 0.75 | 0.75 | stable |
| F026 | Poisoning the Well | 9 | 7.1% | 5 | 4.5% | 4 | 0.40 | 0.56 | stable |
| F042 | False Analogy | 7 | 5.6% | 4 | 3.6% | 4 | 0.57 | 0.57 | stable |
| F041 | False Equivalence | 3 | 2.4% | 7 | 6.3% | 1 | 0.11 | 0.43 | noisy |
| F073 | McNamara Fallacy | 5 | 4.0% | 3 | 2.7% | 2 | 0.33 | 0.60 | stable |
| F022 | Accident | 3 | 2.4% | 4 | 3.6% | 2 | 0.40 | 0.75 | stable |
| F032 | Cum Hoc | 3 | 2.4% | 4 | 3.6% | 1 | 0.17 | 0.75 | noisy |
| F055 | Ecological Fallacy | 7 | 5.6% | 0 | 0.0% | 0 | 0.00 | 0.00 | noisy |
| F011 | Hasty Generalization | 2 | 1.6% | 4 | 3.6% | 1 | 0.20 | 0.50 | noisy |
| F031 | Post Hoc | 4 | 3.2% | 2 | 1.8% | 2 | 0.50 | 0.50 | stable |
| F005 | Appeal to Popularity | 3 | 2.4% | 2 | 1.8% | 1 | 0.25 | 0.67 | stable |
| F028 | Appeal to Tradition | 3 | 2.4% | 2 | 1.8% | 2 | 0.67 | 0.67 | stable |
| F033 | Causal Oversimplification | 4 | 3.2% | 1 | 0.9% | 0 | 0.00 | 0.25 | noisy |
| F034 | False Cause | 1 | 0.8% | 4 | 3.6% | 1 | 0.25 | 0.25 | noisy |
| F001 | Ad Hominem | 2 | 1.6% | 1 | 0.9% | 1 | 0.50 | 0.50 | too few |
| F004 | Appeal to Authority | 2 | 1.6% | 1 | 0.9% | 0 | 0.00 | 0.50 | too few |
| F025 | Guilt by Association | 2 | 1.6% | 1 | 0.9% | 1 | 0.33 | 0.50 | too few |
| F027 | Genetic Fallacy | 3 | 2.4% | 0 | 0.0% | 0 | 0.00 | 0.00 | too few |
| F077 | Fallacy of Relative Privation | 1 | 0.8% | 2 | 1.8% | 1 | 0.50 | 0.50 | too few |
| F013 | False Dilemma | 2 | 1.6% | 0 | 0.0% | 0 | 0.00 | 0.00 | too few |
| F019 | Composition | 1 | 0.8% | 1 | 0.9% | 1 | 1.00 | 1.00 | too few |
| F053 | Argument from Repetition | 1 | 0.8% | 1 | 0.9% | 0 | 0.00 | 1.00 | too few |
| F061 | Is-Ought Jump | 1 | 0.8% | 1 | 0.9% | 1 | 1.00 | 1.00 | too few |
| F020 | Division | 0 | 0.0% | 1 | 0.9% | 0 | 0.00 | 0.00 | too few |
| F039 | No True Scotsman | 1 | 0.8% | 0 | 0.0% | 0 | 0.00 | 0.00 | too few |
| F056 | Exception Fallacy | 1 | 0.8% | 0 | 0.0% | 0 | 0.00 | 0.00 | too few |

- Stable: F040 Loaded Language, F010 Appeal to Ignorance, F003 Red Herring, F002 Straw Man, F026 Poisoning the Well, F042 False Analogy, F073 McNamara Fallacy, F022 Accident, F031 Post Hoc, F005 Appeal to Popularity, F028 Appeal to Tradition
- Noisy: F036 Suppressed Evidence, F041 False Equivalence, F032 Cum Hoc, F055 Ecological Fallacy, F011 Hasty Generalization, F033 Causal Oversimplification, F034 False Cause
- Too few to judge: F001 Ad Hominem, F004 Appeal to Authority, F025 Guilt by Association, F027 Genetic Fallacy, F077 Fallacy of Relative Privation, F013 False Dilemma, F019 Composition, F053 Argument from Repetition, F061 Is-Ought Jump, F020 Division, F039 No True Scotsman, F056 Exception Fallacy

## 5. Problems and notes

- run 2: 2 quote(s) span two sentences and were mapped to both units
- Run 3 never used F055 Ecological Fallacy. The clearest run-2 F055 case on these articles (circumcision: US vs Sweden lifetime UTI prevalence) was read by run 3 as part of an attributed 'Critiques ... emphasize' paragraph and skipped under the attribution rule. This is an example of the attribution boundary driving disagreement.
- In cultural-views-on-circumcision-aesthetics, one run-3 quote occurs verbatim twice in the snapshot (the lead and a later section); it is mapped to its first occurrence.
- Run 3 was done blind: its flags.csv and coverage.tsv were written before run 2's files were opened. Unit coverage for run 3 is a self-report of a full read (coverage.tsv), not a measurement.
- Attribution rule (from the task instructions, applied by judgment in run 3; run 2 was given the same rule): positions explicitly attributed to someone ('critics argue', 'proponents contend', and the rest of such a paragraph) are not counted as the article's own reasoning. Where that boundary is drawn accounts for part of the sentence-level disagreement.
- Side is a judgment about which position a lapse favors. In prohibition-of-female-circumcision-act-1985, 'pro' means it favors cutting or a male/female distinction.

## Caveat

Both runs used the same model family and the same substance_lens v0.5.9 spec (67 kept F-IDs). Agreement between them shows **consistency of the method, not correctness**. Shared blind spots or shared biases would show up as agreement. No outside fact-checking was done; every flag is a judgment about the article's own reasoning, not a measurement.
