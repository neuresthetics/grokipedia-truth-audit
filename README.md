# grokipedia-truth-audit

Public, version-controlled audit of bias, omissions, and alignment drift in Grokipedia (xAI’s AI-generated encyclopedia) with a current focus on the "Circumcision" article.

## Latest findings (2026-10-01)

A full-read sophistry scan of 58 Grokipedia circumcision articles found a pro-circumcision lean in the male-circumcision articles: 85% of side-taking flags (123 pro, 22 anti). Every flag is a judgment call, so treat each as a lead to check.

| Measure | Result |
|---|---|
| Sentences read | all 10,258 units in 58 articles (100%) |
| Flags (pro / anti / neither) | 225 (154 / 49 / 22) |
| Male-circumcision articles (39): pro / anti / neither | 123 / 22 / 9 (85% of sided flags pro) |
| FGM articles (19): pro / anti / neither | 31 / 27 / 13 (53% of sided flags pro; one article supplies 14 of the 31) |

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
- Index of the 58 articles: [INDEX_circumcision_related.md](articles/INDEX_circumcision_related.md)

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
