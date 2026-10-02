# grokipedia-truth-audit

Public, version-controlled audit of bias, omissions, and alignment drift in Grokipedia (xAI’s AI-generated encyclopedia) with a current focus on the "Circumcision" article.

## Latest findings (2026-10-01)

Two blind scans of 58 Grokipedia circumcision articles both found a pro-circumcision lean (77% and 85% of side-taking flags), with no article flipping. Individual flags were less stable (44% re-flagged), so treat each as a lead to check.

- Per-article scans and a table of violations by fallacy type: [SOPHISTRY_SCAN_SUMMARY_2026-10-01.md](articles/SOPHISTRY_SCAN_SUMMARY_2026-10-01.md)
- Run 1 vs run 2 comparison: [SOPHISTRY_RERUN_2026-10-01/COMPARISON.md](articles/SOPHISTRY_RERUN_2026-10-01/COMPARISON.md)
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
