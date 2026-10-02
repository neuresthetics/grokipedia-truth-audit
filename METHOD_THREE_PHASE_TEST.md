# Three-phase test of the sophistry scan

This page explains how the sophistry scans of Grokipedia's circumcision articles were done, and how they were tested by running the same scan three times. It covers what the substance_lens framework is, what each of the three runs did and why, how the runs compare, and what the test does and doesn't show.

**Short version.** Across three runs, the main finding held: the articles' own reasoning leans strongly pro-circumcision, and the same articles come out as the worst. Exactly which sentences get flagged changed a good deal from run to run. Treat the overall lean and the article ranking as the finding, and treat each individual flag as a lead to check by hand. All three runs used the same model family and the same framework, so this test shows the method is consistent. It does not show the method is correct.

## 1. The framework: substance_lens

[substance_lens](https://github.com/neuresthetics/substance_lens) is a reasoning framework written as a JSON "thoughtware" file that is given to an AI model as instructions. Its README describes it as a method for stripping a set of claims down to the parts that survive close logical scrutiny. All three runs used version **0.5.9**: the spec file is [`substance_lens_0.5.9.json`](https://github.com/neuresthetics/substance_lens/blob/main/substance_lens_0.5.9.json), and the changes in that version are listed in [`CHANGELOG_0.5.9.md`](https://github.com/neuresthetics/substance_lens/blob/main/CHANGELOG_0.5.9.md).

The scans used one part of the spec, the **`fallacyScanPass`**, which was added in v0.5.9. Three features of it matter here.

- **The fallacy catalogue (F-IDs).** The pass takes its entries from geometric_fallacy_engine v0.1.0, an 80-entry fallacy catalogue. Of the 80, 67 were kept, 6 were dropped because an existing rule in the framework already covers them, and 7 were merged as duplicates. Each kept entry keeps its original ID (F001 to F080), a name, a category (relevance, insufficiency, presumption, ambiguity, causal or formal), a detection cue, and a repair rule. For example, F040 is Loaded Language and F036 is Suppressed Evidence. The 67 kept entries used here are copied in [fid_catalog.json](articles/SOPHISTRY_RUN3_TITLE24_2026-10-02/fid_catalog.json).
- **Both sides by default.** The spec's `dual_case_rule` says every check must run on both the claim under review and the strongest counter-case, with the same effort for each, and that a scan of one side only is incomplete. In these scans, that meant reasoning on both sides of the circumcision debate was checked, and every flag is tagged with the side it favours: **pro** (favours circumcision), **anti** (favours the opposing side) or **neutral** (favours neither). In the female genital cutting articles, "pro" means the flag favours cutting or a male/female distinction.
- **A flag is not a disproof.** The spec says a flag only withdraws support from the step it is on. It does not show the conclusion is false.

The spec also says that none of its 67 entries has a working argument-checker in code: 48 are judgment only, 10 have a partial mechanical sub-check, and 9 could be checked by code once an argument is put into formal shape. So every flag is a model's judgment. Rule **I10** ("trace honesty") forbids claiming a logic-gate computation unless its inputs, gates and outputs are shown. The framework's wider machinery (boolean gates, XNOR stability, the construction graph) was **not** run in any of these scans, and no such result is claimed.

## 2. How the framework was applied

What was actually done, in every run:

1. **Snapshots.** Each article was saved as a text snapshot on 2026-10-01 (`articles/<slug>/snapshots/2026-10-01.txt`). All three runs read the same snapshots. The 58 articles and why each was included are listed in [ARTICLE_LIST.md](articles/ARTICLE_LIST.md).
2. **Sentence segmentation.** A script split each snapshot into units: prose sentences and table rows.
3. **A model read of each sentence.** A model read each unit against the fallacy catalogue and flagged it only when the article's *own* reasoning matched an entry's detection cue. Positions the article explicitly attributes to others ("critics argue", "proponents contend") were not counted as the article's reasoning. Each flag records the exact quote, the F-ID, the side and a short note.
4. **Quote verification.** A script checked that every quoted passage occurs verbatim in its snapshot, so every flag can be traced to real text.
5. **Scripted comparison.** Scripts mapped each run's flags onto sentences and computed the counts, overlaps and correlations reported below.

No outside fact-checking was done. The scans judge whether an article's reasoning holds up, not whether its facts are true.

## 3. The three phases

### Phase 1: partial read (run 1, 2026-10-01)

**Why:** a first pass to see whether the scan finds anything, using a cheap shortcut.

Run 1 covered all 58 circumcision-related articles. Instead of reading every sentence, it read each article's lead plus a subset of body sentences picked by a cue-word triage script (`tools/sophistry_triage.py`). That came to about 30% of sentences (2,969 of 10,016 by run 1's own count). It raised 239 flags. In the 39 male-circumcision articles, 77% of the flags that took a side were pro; across all 58 articles, including the female genital cutting articles, the figure was 69%.

Results: [SOPHISTRY_SCAN_SUMMARY_2026-10-01.md](articles/SOPHISTRY_SCAN_SUMMARY_2026-10-01.md), plus a `sophistry_scan_run1_partial.md` file in each article's `analyses/2026-10-01/` folder (for example [Circumcision](articles/circumcision/analyses/2026-10-01/sophistry_scan_run1_partial.md)).

**Weakness:** the triage script decided what got read, so unread sentences could hide flags, and the shortcut itself could bias the result.

### Phase 2: blind full read (run 2, 2026-10-01)

**Why:** to remove the shortcut and to test whether run 1's findings come back when the scan is done again without seeing them.

Run 2 read every unit of all 58 articles: 10,258 units. It was done without opening run 1's scans, run 1's summary or the triage script. It raised 225 flags: 154 pro, 49 anti and 22 neutral.

Compared with run 1, run 2 re-flagged 44% of the sentences run 1 had flagged. Where both runs flagged the same sentence, they gave the same F-ID 67% of the time and the same side 90% of the time. The Spearman correlation of per-article flag counts was 0.75. The pro lean in the male-circumcision articles held (77% in run 1, 85% in run 2). The lean of the female genital cutting articles did not hold.

Results: [SOPHISTRY_RERUN_2026-10-01/COMPARISON.md](articles/SOPHISTRY_RERUN_2026-10-01/COMPARISON.md) and [flags.csv](articles/SOPHISTRY_RERUN_2026-10-01/flags.csv).

**Weakness:** runs 1 and 2 read different amounts of text, so some of their disagreement comes from coverage rather than judgment.

### Phase 3: focused blind replication (run 3, 2026-10-02)

**Why:** to compare two runs that both read everything, on the articles that matter most.

Run 3 re-read, blind and in full, only the 24 "title match" articles (the title contains "circumcision"). These are the core articles and carry most of the flags. Run 3's flags were written before run 2's flag file was opened. The comparison is against run 2's flags on the same 24 articles.

- Run 2 on the 24: 126 flags (100 pro, 19 anti, 7 neutral), 84.0% pro.
- Run 3 on the 24: 111 flags (86 pro, 18 anti, 7 neutral), 82.7% pro.
- Spearman correlation of per-article counts: 0.837. Article lean matched in 17 of 24 articles. Two articles, Forced circumcision of minors in South Korea and Prevalence of circumcision, reversed between pro and anti. All 7 mismatches were articles with 4 or fewer flags.
- Sentence overlap: 77 sentences flagged by both, 51 only by run 2, 34 only by run 3 (Jaccard 0.475). Run 3 reproduced 60% of run 2's flagged sentences. Where both flagged the same sentence, the F-ID matched 79% of the time and the side 97% of the time.
- The heaviest articles stayed heaviest. Ethics of circumcision went from 24 to 21 flags (all pro in both runs), Circumcision controversies from 21 to 13, Circumcision from 15 to 6, and Views on circumcision stayed at 9. Forced circumcision stayed at 7, all anti in both runs.

Results: [SOPHISTRY_RUN3_TITLE24_2026-10-02/README.md](articles/SOPHISTRY_RUN3_TITLE24_2026-10-02/README.md) and [COMPARISON.md](articles/SOPHISTRY_RUN3_TITLE24_2026-10-02/COMPARISON.md).

### The three phases side by side

| | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Date | 2026-10-01 | 2026-10-01 | 2026-10-02 |
| Articles | 58 | 58 | 24 (title matches) |
| What was read | Lead + triage-picked sentences, about 30% | Every unit (10,258) | Every unit of the 24 |
| Blind to earlier flags | First run | Yes (blind to run 1) | Yes (blind to run 2) |
| Flags (pro / anti / neutral) | 239 (126 / 56 / 57) | 225 (154 / 49 / 22) | 111 (86 / 18 / 7) |
| Pro share of sided flags | 77% in male-circumcision articles | 85% in male-circumcision articles | 82.7% on the 24 (run 2 on the same 24: 84.0%) |
| Compared against | (none) | Run 1 | Run 2, same 24 articles |
| Previous run's flagged sentences found again | (none) | 44% | 60% |
| Same F-ID, on shared sentences | (none) | 67% | 79% |
| Same side, on shared sentences | (none) | 90% | 97% |
| Spearman, per-article counts | (none) | 0.75 (58 articles) | 0.837 (24 articles) |

Agreement went up between the run 1/run 2 comparison and the run 2/run 3 comparison. That is expected, since runs 2 and 3 both read everything and run 3 covered only the core articles. It should not be read as the method getting better.

## 4. What the test shows and doesn't show

**What it shows**

- **The aggregate lean replicates.** In every run, most flags that take a side are pro-circumcision in the male-circumcision articles: 77%, 85%, and 84.0% vs 82.7% on the 24 title matches.
- **The ranking of the worst articles replicates.** Ethics of circumcision and Circumcision controversies are among the three most-flagged articles in every run, and among the title-match articles Forced circumcision is the main anti-leaning exception each time. Per-article counts correlate at 0.75 (run 1 vs 2) and 0.837 (run 2 vs 3).
- **When two runs flag the same sentence, they nearly always agree on which side it favours** (90% and 97%).

**What it doesn't show**

- **That any single flag is right.** Only 44% (run 1 to 2) and 60% (run 2 to 3) of flagged sentences came back. Any one run's list is a sample of defensible flags, not a complete or final inventory. Individual flags are leads to check by hand.
- **Stable results for small articles.** Articles with only a few flags can change lean with a single flag. All 7 lean mismatches in run 3 were articles with 4 or fewer flags.
- **Correctness.** All three runs used the same model family and the same method. Agreement between them measures **consistency (reliability), not correctness (validity)**. A blind spot or bias shared by the runs would show up as agreement. No independent human or second-model judge reviewed the flags.
- **Full independence.** The "blind" runs did not see earlier flags, but all three runs used the same framework, the same catalogue and the same attribution rule.
- **That the articles' facts are wrong.** A flag points to a gap in the article's reasoning, not a false claim. No outside fact-checking was done.
- **Any logic-gate result.** No XNOR, gate or other formal computation from substance_lens was run. The only computations were the scripts listed above: segmentation, quote checks and comparisons.

**What would strengthen it:** an independent check of a sample of flags by human reviewers, a different model family run against the same catalogue, or both.

## 5. Where the files are

| Phase | Folder or file |
|---|---|
| Run 1 | [articles/SOPHISTRY_SCAN_SUMMARY_2026-10-01.md](articles/SOPHISTRY_SCAN_SUMMARY_2026-10-01.md) and `articles/<slug>/analyses/2026-10-01/sophistry_scan_run1_partial.md` |
| Run 2 | [articles/SOPHISTRY_RERUN_2026-10-01/](articles/SOPHISTRY_RERUN_2026-10-01/COMPARISON.md) (flags, coverage, comparison with run 1) |
| Run 3 | [articles/SOPHISTRY_RUN3_TITLE24_2026-10-02/](articles/SOPHISTRY_RUN3_TITLE24_2026-10-02/README.md) (flags, coverage, comparison with run 2, scripts) |
| Framework | [neuresthetics/substance_lens](https://github.com/neuresthetics/substance_lens), spec [substance_lens_0.5.9.json](https://github.com/neuresthetics/substance_lens/blob/main/substance_lens_0.5.9.json) |
