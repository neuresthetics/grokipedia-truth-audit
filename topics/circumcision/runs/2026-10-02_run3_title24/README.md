# Run 3: blind rescan of the 24 title-match articles (2026-10-02)

Run 3 is the third phase of a three-phase test of the sophistry scan. It re-read, from scratch, the 24 Grokipedia articles whose title contains "circumcision" and compared its flags with run 2's flags on the same 24 articles. The question was simple: if the same method is run again, do the same findings come back?

The short answer is that the big picture comes back and the fine detail only partly does. Both runs find a strong pro-circumcision lean in the articles' own reasoning (84.0% of sided flags in run 2, 82.7% in run 3), and they rank the articles in much the same order (Spearman 0.837). Only 60% of run 2's flagged sentences were flagged again, though, so individual flags should be treated as leads to check by hand.

For how this run fits with runs 1 and 2, and what the test does and doesn't show, see [METHOD_THREE_PHASE_TEST.md](../../../../docs/METHOD_THREE_PHASE_TEST.md). The full computed comparison is in [COMPARISON.md](COMPARISON.md).

## What was scanned

- **Articles:** the 24 "Title match" articles in [ARTICLE_LIST.md](../../ARTICLE_LIST.md). These are the core articles: the title contains "circumcision".
- **Text:** the 2026-10-01 snapshots (`topics/circumcision/articles/<slug>/snapshots/2026-10-01.txt`), the same text runs 1 and 2 used.
- **Framework:** [substance_lens v0.5.9](https://github.com/neuresthetics/substance_lens), its `fallacyScanPass` ([spec file](https://github.com/neuresthetics/substance_lens/blob/main/substance_lens_0.5.9.json), [changelog](https://github.com/neuresthetics/substance_lens/blob/main/CHANGELOG_0.5.9.md)). That pass holds 67 fallacy entries, each with an F-ID (F001 to F080) kept from the 80-entry geometric_fallacy_engine catalogue. The 67 entries are copied into [fid_catalog.json](fid_catalog.json).

## Method

1. **Segmentation.** [segment.py](segment.py) splits each snapshot into prose sentences, table rows and headings. The 24 articles give 5,463 readable units (5,402 sentences and 61 table rows). Headings are not counted. Run 2 used its own splitter and counted 4,171 units for the same 24 articles. The two splitters cut the text differently, so the comparison maps both runs' flags onto run 3's units.
2. **Reading.** A model read every sentence and table row against the 67-entry catalogue. It flagged a sentence only when the article's own reasoning in that sentence matched an entry's detection cue. Positions the article explicitly attributes to someone else ("critics argue", "proponents contend") were not counted as the article's own reasoning.
3. **Both sides.** As the framework requires, the checks were applied to reasoning on both sides of the debate. Every flag is tagged `pro` (the lapse favours circumcision), `anti` (it favours the opposing side) or `neutral` (it favours neither). In the Prohibition of Female Circumcision Act 1985 article, `pro` means the flag favours cutting or a male/female distinction.
4. **Blinding.** Run 3's `flags.csv` and `coverage.tsv` were written before run 2's flag file was opened. Run 3 did not see run 1's or run 2's flags. It did use the same framework and the same rules as run 2.
5. **Quote check.** [verify_quotes.py](verify_quotes.py) checks that every quote in `flags.csv` occurs verbatim in its snapshot, that every F-ID is one of the 67 kept entries, and that every side tag is valid. All 111 quotes matched exactly.
6. **Comparison.** [compare.py](compare.py) maps both runs' quotes to units and writes [COMPARISON.md](COMPARISON.md) and [comparison_units.csv](comparison_units.csv). Every number on this page comes from that script or from a direct count of the two flag files.

Every flag is a judgment by a model, not a measurement. No gate, XNOR or other logic computation was run (these are the framework's formal logic-gate checks; see [§1 of the method note](../../../../docs/METHOD_THREE_PHASE_TEST.md#1-the-framework-substance_lens)); the only code is the segmentation, the quote check and the comparison scripts listed here.

## Results

### Totals

| | Run 2 (on these 24) | Run 3 |
|---|---|---|
| Flags | 126 | 111 |
| Pro / anti / neutral | 100 / 19 / 7 | 86 / 18 / 7 |
| Pro share of sided flags (pro ÷ (pro + anti)) | 84.0% | 82.7% |
| Articles with zero flags | 5 | 2 |

### Agreement between run 2 and run 3

| Measure | Result |
|---|---|
| Spearman rank correlation of per-article flag counts | 0.837 |
| Articles with the same lean (pro, anti, tie or none) | 17 of 24 |
| Articles that reversed between pro and anti | 2 (South Korea, Prevalence) |
| Sentences flagged by both runs | 77 |
| Sentences flagged only by run 2 | 51 |
| Sentences flagged only by run 3 | 34 |
| Jaccard (both ÷ either) | 0.475 |
| Share of run 2's flagged sentences that run 3 also flagged | 60.2% (77 of 128) |
| Same F-ID, on sentences both runs flagged | 79.2% (61 of 77) |
| Same side, on sentences both runs flagged | 97.4% (75 of 77) |

Run 2's 126 flags fall on 128 sentences because two of its quotes span two sentences each.

In plain terms:

- **The lean replicates.** Both runs find that the articles' own reasoning leans strongly pro-circumcision.
- **The ranking replicates.** Ethics of circumcision and Circumcision controversies are the two most-flagged articles in both runs. Forced circumcision is the clear anti-leaning article in both (7 anti flags each). Feast of the Circumcision of Christ and History of circumcision have no flags in either run.
- **Small articles are unstable.** All 7 articles whose lean changed have 4 or fewer flags in both runs, where one flag can flip the result. The two outright reversals, Forced circumcision of minors in South Korea and Prevalence of circumcision, rest on 1 to 4 flags per run.
- **Which sentences get flagged replicates only moderately.** Run 3 found 60% of run 2's flagged sentences, and about half of all flagged sentences were flagged by only one run. When both runs flag the same sentence, they almost always agree on the side (97%) and usually on the fallacy type (79%).
- **Some fallacy types are more stable than others.** F040 Loaded Language, F002 Straw Man, F003 Red Herring and F026 Poisoning the Well came back reliably. The causal and generalisation types (F032, F033, F034, F011, F055) and F036 Suppressed Evidence were noisier. Run 3 never used F055 Ecological Fallacy, which run 2 used 7 times on these articles. See section 4 of [COMPARISON.md](COMPARISON.md).

### Per-article table

Lean is whichever of pro or anti has more flags. "Tie" means equal and non-zero; "none" means no pro or anti flags. Article names link to the snapshot that was read.

| Article | Run 2 flags | Run 2 pro / anti / neutral | Run 3 flags | Run 3 pro / anti / neutral | Same lean? |
|---|---|---|---|---|---|
| [Circumcision](../../articles/circumcision/snapshots/2026-10-01.txt) | 15 | 12 / 2 / 1 | 6 | 6 / 0 / 0 | yes |
| [Circumcision and HIV](../../articles/circumcision-and-hiv/snapshots/2026-10-01.txt) | 5 | 5 / 0 / 0 | 2 | 2 / 0 / 0 | yes |
| [Circumcision and law](../../articles/circumcision-and-law/snapshots/2026-10-01.txt) | 8 | 8 / 0 / 0 | 6 | 6 / 0 / 0 | yes |
| [Circumcision controversies](../../articles/circumcision-controversies/snapshots/2026-10-01.txt) | 21 | 19 / 1 / 1 | 13 | 13 / 0 / 0 | yes |
| [Circumcision controversy in early Christianity](../../articles/circumcision-controversy-in-early-christianity/snapshots/2026-10-01.txt) | 5 | 1 / 3 / 1 | 4 | 1 / 3 / 0 | yes |
| [Circumcision in Africa](../../articles/circumcision-in-africa/snapshots/2026-10-01.txt) | 9 | 9 / 0 / 0 | 5 | 4 / 0 / 1 | yes |
| [Circumcision in Brunei](../../articles/circumcision-in-brunei/snapshots/2026-10-01.txt) | 1 | 1 / 0 / 0 | 3 | 3 / 0 / 0 | yes |
| [Circumcision in China](../../articles/circumcision-in-china/snapshots/2026-10-01.txt) | 0 | 0 / 0 / 0 | 3 | 3 / 0 / 0 | **no** (none → pro) |
| [Circumcision in the Bible](../../articles/circumcision-in-the-bible/snapshots/2026-10-01.txt) | 0 | 0 / 0 / 0 | 1 | 0 / 1 / 0 | **no** (none → anti) |
| [Circumcision of Jesus](../../articles/circumcision-of-jesus/snapshots/2026-10-01.txt) | 1 | 0 / 0 / 1 | 1 | 0 / 0 / 1 | yes |
| [Circumcision surgical procedure](../../articles/circumcision-surgical-procedure/snapshots/2026-10-01.txt) | 4 | 2 / 1 / 1 | 2 | 1 / 1 / 0 | **no** (pro → tie) |
| [Cost of circumcision surgery in Chaozhou](../../articles/cost-of-circumcision-surgery-in-chaozhou/snapshots/2026-10-01.txt) | 1 | 1 / 0 / 0 | 2 | 1 / 0 / 1 | yes |
| [Cultural views on circumcision aesthetics](../../articles/cultural-views-on-circumcision-aesthetics/snapshots/2026-10-01.txt) | 2 | 0 / 1 / 1 | 3 | 1 / 1 / 1 | **no** (anti → tie) |
| [Ethics of circumcision](../../articles/ethics-of-circumcision/snapshots/2026-10-01.txt) | 24 | 24 / 0 / 0 | 21 | 21 / 0 / 0 | yes |
| [Feast of the Circumcision of Christ](../../articles/feast-of-the-circumcision-of-christ/snapshots/2026-10-01.txt) | 0 | 0 / 0 / 0 | 0 | 0 / 0 / 0 | yes |
| [Forced circumcision](../../articles/forced-circumcision/snapshots/2026-10-01.txt) | 7 | 0 / 7 / 0 | 7 | 0 / 7 / 0 | yes |
| [Forced circumcision of minors in South Korea](../../articles/forced-circumcision-of-minors-in-south-korea/snapshots/2026-10-01.txt) | 1 | 0 / 1 / 0 | 4 | 3 / 1 / 0 | **no** (anti → pro) |
| [History of circumcision](../../articles/history-of-circumcision/snapshots/2026-10-01.txt) | 0 | 0 / 0 / 0 | 0 | 0 / 0 / 0 | yes |
| [Khitan (circumcision)](../../articles/khitan-circumcision/snapshots/2026-10-01.txt) | 4 | 3 / 1 / 0 | 4 | 4 / 0 / 0 | yes |
| [Prevalence of circumcision](../../articles/prevalence-of-circumcision/snapshots/2026-10-01.txt) | 1 | 1 / 0 / 0 | 2 | 0 / 2 / 0 | **no** (pro → anti) |
| [Prohibition of Female Circumcision Act 1985](../../articles/prohibition-of-female-circumcision-act-1985/snapshots/2026-10-01.txt) | 6 | 3 / 2 / 1 | 6 | 3 / 2 / 1 | yes |
| [Religion and circumcision](../../articles/religion-and-circumcision/snapshots/2026-10-01.txt) | 2 | 2 / 0 / 0 | 4 | 2 / 0 / 2 | yes |
| [Stapler circumcision](../../articles/stapler-circumcision/snapshots/2026-10-01.txt) | 0 | 0 / 0 / 0 | 3 | 3 / 0 / 0 | **no** (none → pro) |
| [Views on circumcision](../../articles/views-on-circumcision/snapshots/2026-10-01.txt) | 9 | 9 / 0 / 0 | 9 | 9 / 0 / 0 | yes |
| **Total** | **126** | **100 / 19 / 7** | **111** | **86 / 18 / 7** | **17 of 24** |

The biggest movers among the heavily flagged articles: Ethics of circumcision went from 24 to 21 (all pro in both runs), Circumcision controversies from 21 to 13, and Circumcision from 15 to 6. Views on circumcision stayed at 9, and Forced circumcision stayed at 7 (all anti in both runs).

## Limits

- **Consistency, not correctness.** Runs 2 and 3 used the same model family and the same framework. Agreement shows that the method gives similar answers when repeated. It does not show the flags are right. A blind spot or bias shared by both runs would show up as agreement. No human reviewer or independent model checked the flags.
- **Coverage is self-reported.** `coverage.tsv` records that every unit was read. That is a statement of procedure, not a measurement of attention.
- **The attribution line is a judgment call.** Where an attributed passage ends and the article's own voice begins accounts for part of the disagreement. For example, run 3 read the clearest run-2 F055 case in Circumcision (US vs Sweden UTI figures) as part of an attributed paragraph and skipped it.
- **No fact-checking.** A flag says the article's reasoning in that sentence has a gap. It does not say the claim is false.

## Files

| File | What it is |
|---|---|
| [flags.csv](flags.csv) | Run 3's 111 flags: slug, exact quote, F-ID, fallacy name, side, note |
| [coverage.tsv](coverage.tsv) | Per-article unit counts (sentences, table rows, headings), flags and flagged units |
| [COMPARISON.md](COMPARISON.md) | Full run 2 vs run 3 comparison, written by `compare.py` |
| [comparison_units.csv](comparison_units.csv) | One row per flagged unit: matched, run 2 only or run 3 only, with each run's F-IDs and sides |
| [fid_catalog.json](fid_catalog.json) | The 67 kept F-IDs from the substance_lens v0.5.9 `fallacyScanPass`, with name, category and check type |
| [segment.py](segment.py) | Splits the snapshots into sentences, table rows and headings; maps quotes to units |
| [verify_quotes.py](verify_quotes.py) | Checks every quote, F-ID and side tag in `flags.csv` |
| [make_coverage.py](make_coverage.py) | Writes `coverage.tsv` |
| [compare.py](compare.py) | Writes `COMPARISON.md` and `comparison_units.csv` |

To reproduce, run these from the repo root (Python 3, standard library only):

```
python3 topics/circumcision/runs/2026-10-02_run3_title24/verify_quotes.py
python3 topics/circumcision/runs/2026-10-02_run3_title24/make_coverage.py
python3 topics/circumcision/runs/2026-10-02_run3_title24/compare.py
```

`flags.csv` sha256: `41fe39774833148eb0286f93a6f62c65f2b946fbe57fc21bdd90f93b1a90f6ca`. Run 2's flags are in [../2026-10-01_run2_full/flags.csv](../2026-10-01_run2_full/flags.csv).
