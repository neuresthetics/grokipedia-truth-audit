# grokipedia-truth-audit

Public, version-controlled audit of bias, omissions, and alignment drift in Grokipedia (xAI’s AI-generated encyclopedia) with a current focus on the "Circumcision" article.

## Latest findings (2026-10-01, replication added 2026-10-02)

A full-read sophistry scan of 58 Grokipedia circumcision articles found a pro-circumcision lean in the male-circumcision articles: 85% of side-taking flags (123 pro, 22 anti). Every flag is a judgment call, so treat each as a lead to check.

| Measure | Result |
|---|---|
| Sentences read | all 10,258 units in 58 articles (100%) |
| Flags (pro / anti / neither) | 225 (154 / 49 / 22) |
| Male-circumcision articles (39): pro / anti / neither | 123 / 22 / 9 (85% of sided flags pro) |
| FGM articles (19): pro / anti / neither | 31 / 27 / 13 (53% of sided flags pro; one article supplies 14 of the 31) |

![Side of each flag in runs 1, 2 and 3](docs/img/lean_by_run.png)

Side of each flag, by run. Pro share of sided flags: run 1 69.2% and run 2 75.9% across all 58 articles; run 2 84.0% and run 3 82.7% on the 24 title matches. The 85% in the table above is the 39 male-circumcision articles only (run 1 gave 77% on those 39). Run 1 read only about 30% of sentences.

### Violations by fallacy type

Counted by script from the scan's flag file. In FGM articles, "pro" means the flag favors cutting or a male/female distinction.

| Fallacy (engine ID) | Total | Pro | Anti | Neither |
|---|---|---|---|---|
| F040 Loaded Language | 37 | 28 | 9 | 0 |
| F036 Suppressed Evidence | 26 | 21 | 3 | 2 |
| F032 Cum Hoc | 15 | 5 | 1 | 9 |
| F011 Hasty Generalization | 14 | 10 | 2 | 2 |
| F026 Poisoning the Well | 14 | 10 | 3 | 1 |
| F010 Appeal to Ignorance | 13 | 7 | 3 | 3 |
| F031 Post Hoc | 12 | 3 | 7 | 2 |
| F002 Straw Man | 10 | 7 | 3 | 0 |
| F003 Red Herring | 10 | 10 | 0 | 0 |
| F001 Ad Hominem | 8 | 6 | 2 | 0 |
| F034 False Cause | 8 | 2 | 6 | 0 |
| F042 False Analogy | 8 | 8 | 0 | 0 |
| F055 Ecological Fallacy | 7 | 5 | 2 | 0 |
| F033 Causal Oversimplification | 6 | 3 | 3 | 0 |
| F073 McNamara Fallacy | 5 | 4 | 0 | 1 |
| F013 False Dilemma | 4 | 4 | 0 | 0 |
| F028 Appeal to Tradition | 4 | 4 | 0 | 0 |
| F005 Appeal to Popularity | 3 | 2 | 1 | 0 |
| F022 Accident | 3 | 3 | 0 | 0 |
| F027 Genetic Fallacy | 3 | 2 | 1 | 0 |
| F041 False Equivalence | 3 | 0 | 2 | 1 |
| F004 Appeal to Authority | 2 | 0 | 1 | 1 |
| F025 Guilt by Association | 2 | 2 | 0 | 0 |
| F039 No True Scotsman | 2 | 2 | 0 | 0 |
| F019 Composition | 1 | 1 | 0 | 0 |
| F035 Texas Sharpshooter | 1 | 1 | 0 | 0 |
| F053 Argument from Repetition | 1 | 1 | 0 | 0 |
| F056 Exception Fallacy | 1 | 1 | 0 | 0 |
| F061 Is-Ought Jump | 1 | 1 | 0 | 0 |
| F077 Fallacy of Relative Privation | 1 | 1 | 0 | 0 |
| **Total** | **225** | **154** | **49** | **22** |

- All flags with exact quotes: [flags.csv](articles/SOPHISTRY_RERUN_2026-10-01/flags.csv)
- Reproducibility check against an earlier partial read: [COMPARISON.md](articles/SOPHISTRY_RERUN_2026-10-01/COMPARISON.md)
- All 58 articles with snapshot and Grokipedia links and why each was included: [ARTICLE_LIST.md](articles/ARTICLE_LIST.md)
- Full index with counts and dates: [INDEX_circumcision_related.md](articles/INDEX_circumcision_related.md)

### Replication: three-phase test (2026-10-02)

The scan has now been run three times with the same [substance_lens](https://github.com/neuresthetics/substance_lens) v0.5.9 fallacy catalogue. Run 1 was a partial read of about 30% of sentences. Run 2 is the blind full read above. Run 3 was a second blind full read of the 24 core articles, the ones with "circumcision" in the title, and was compared with run 2 on those same 24.

| On the 24 title-match articles | Run 2 | Run 3 |
|---|---|---|
| Flags (pro / anti / neither) | 126 (100 / 19 / 7) | 111 (86 / 18 / 7) |
| Pro share of sided flags | 84.0% | 82.7% |
| Ethics of circumcision | 24 (all pro) | 21 (all pro) |
| Circumcision controversies | 21 | 13 |
| Circumcision | 15 | 6 |
| Forced circumcision | 7 (all anti) | 7 (all anti) |

The pro lean and the ranking of the most-flagged articles held up: per-article counts correlate at 0.837 (Spearman), and 17 of the 24 articles got the same lean, with every mismatch on an article with 4 or fewer flags. Only 60% of run 2's flagged sentences were flagged again, though when both runs flagged a sentence they agreed on its side 97% of the time. So individual flags remain leads to check by hand. Because every run used the same model family and method, this shows the scan is consistent, not that it is correct.

![Flags per article, run 2 vs run 3](docs/img/title24_per_article.png)

Flags per article on the 24 title matches: run 2 on the upper bar, run 3 on the lower dotted bar, colored by side.

![Per-article flag counts, run 2 vs run 3](docs/img/run2_vs_run3_scatter.png)

Per-article flag counts in run 2 against run 3, one dot per article (Spearman 0.837, n = 24).

![Sentence-level overlap, run 2 vs run 3](docs/img/flag_overlap.png)

Of 162 sentences flagged by either run, 77 were flagged by both, 51 by run 2 only and 34 by run 3 only; on the 77, the side matched 75 times and the F-ID 61 times.

![Fallacy types, run 2 vs run 3](docs/img/fallacy_types_stability.png)

The 18 most-used fallacy types on the 24 title matches (at least 5 flags across both runs, so four types tied at 5 are all shown), with how often both runs gave the same F-ID to the same sentence.

- How the three runs were done, and what the test does and doesn't show: [METHOD_THREE_PHASE_TEST.md](METHOD_THREE_PHASE_TEST.md)
- Run 3 flags, scripts and full comparison: [articles/SOPHISTRY_RUN3_TITLE24_2026-10-02/](articles/SOPHISTRY_RUN3_TITLE24_2026-10-02/README.md)
- Charts: [tools/make_charts.py](tools/make_charts.py) draws all five from the committed flag files and prints every number it draws. Run `python3 tools/make_charts.py` from the repo root (needs matplotlib).
- Re-running the scripts: run 3's scripts run from the repo as they are (standard library only). Run 2's `build_flags.py` can't be re-run from the repo, because its inputs (the flag snippet file `raw_flags.tsv` and a local copy of the substance_lens spec) are not published; `flags.csv` is the published record. Run 2's `compare.py` needs the files that `split.py` regenerates and a one-line filename change; see the Files section of [COMPARISON.md](articles/SOPHISTRY_RERUN_2026-10-01/COMPARISON.md).

## Why this repo exists
- Grokipedia launched 27 Oct 2025 with the claim of being “Wikipedia without the propaganda”.
- The current Circumcision entry (last Grok-verified 29 Nov 2025) is ~68 % pro non-therapeutic infant male circumcision, ~20 % neutral, ~12 % anti (see quantitative breakdown in [articles/circumcision/analyses/2025-11-30](articles/circumcision/analyses/2025-11-30/bias_quantification.md)).
- The article systematically minimises the certain, irreversible loss of healthy erogenous tissue from non-consenting minors while presenting marginal or context-specific benefits as decisive.
- This constitutes a clear Atrophator vector under the Ψ-Square framework used internally by Grok.

## Repo goals
1. Maintain a public, immutable record of every version of the Grokipedia Circumcision article.
2. Track edit submissions, Grok responses, and acceptance/rejection patterns.
3. Provide ready-to-submit, evidence-based correction drafts.
4. Quantify bias over time (pro / neutral / anti %).
5. Serve as a template for auditing other controversial Grokipedia entries.


## Repo layout
- `articles/<topic>/snapshots/`: verbatim copies of a Grokipedia article, named by date (YYYY-MM-DD).
- `articles/<topic>/analyses/<date>/`: analyses of the snapshot from that date.
- `articles/<topic>/edit_submissions/`: correction drafts submitted to Grokipedia.
- `background/`: essays and collider runs on the underlying topic. These are not audits of the article.
- `planning/`: the list of candidate articles to audit next.

Current articles: [circumcision](articles/circumcision/).

## Circumcision ethics in general
The essay that used to be on this page is now at [background/circumcision_ethics/harmony_gain_through_rights_evolution.md](background/circumcision_ethics/harmony_gain_through_rights_evolution.md).
