# Adding a topic

A topic is a group of related Grokipedia articles audited together (for example `circumcision` or `spinoza`). Each topic gets its own folder under `topics/`. Use lowercase names with hyphens throughout.

## 1. Folder skeleton

```
topics/<topic>/
  README.md               what the topic covers, headline results, what's in the folder
  ARTICLE_LIST.md         one row per article: title, snapshot link, live page, why included
  articles/<slug>/
    snapshots/            <YYYY-MM-DD>.html as fetched, plus a readable .txt or .md
    analyses/<YYYY-MM-DD>/  results for the snapshot of that date
    edit_submissions/     correction drafts for Grokipedia (add .gitkeep if empty)
  runs/                   cross-article scan runs (only if there are any)
    README.md             one row per run
    <YYYY-MM-DD>_run<N>_<scope>/   flags, coverage, comparison, run-specific scripts
  background/             optional: material on the topic itself, not audits
  code_counts/            optional: output of tools/sophistry_counts.py
```

- `<topic>`: short, lowercase (`circumcision`, `spinoza`).
- `<slug>`: the Grokipedia page title, lowercased, with spaces and punctuation turned into hyphens (`Baruch_Spinoza` → `baruch-spinoza`).
- Run folders: date the run started, run number within the topic, scope (`2026-10-01_run2_full`, `2026-10-02_run3_title24`).
- Charts go in `docs/img/<topic>/`.

## 2. Checklist

- [ ] Save each snapshot under `articles/<slug>/snapshots/<date>.*`. Never edit a snapshot after saving it.
- [ ] Write `ARTICLE_LIST.md` with the inclusion rule and one row per article.
- [ ] Run the tools with the topic flag where they take one, e.g. `python3 tools/sophistry_counts.py --topic <topic> --all --date <date>`.
- [ ] Put each run's outputs and any run-specific scripts in `runs/<YYYY-MM-DD>_run<N>_<scope>/`, with a README stating what was read, the method, and how to re-run it. Add a row to `runs/README.md`.
- [ ] Write `topics/<topic>/README.md` (headline result, caveats, folder table). Link back to the repo README.
- [ ] Add a row to the topics table in the [repo README](../README.md): topic, number of articles, latest run, link.
- [ ] Check that every relative link resolves and that no local paths (`/Users/...`, `/home/...`, `/tmp/...`) appear in committed files.
- [ ] Check that the counts quoted in READMEs match the committed data files.
