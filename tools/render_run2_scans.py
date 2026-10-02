#!/usr/bin/env python3
"""Render the per-article full-read sophistry scans from rerun inputs."""
from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

DATE = "2026-10-01"
RERUN_DIR = Path("articles/SOPHISTRY_RERUN_2026-10-01")
PARTIAL_NAME = "sophistry_scan_run1_partial.md"
SCAN_NAME = "sophistry_scan.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def esc_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def lean(sides: Counter[str]) -> str:
    if not sides:
        return "no flagged lean"
    highest = max(sides.values())
    winners = [side for side in ("pro", "anti", "neutral") if sides[side] == highest]
    if len(winners) == 1:
        return winners[0]
    return "mixed (" + "/".join(winners) + " tie)"


def patterns(flags: list[dict[str, str]]) -> str:
    by_name: Counter[str] = Counter()
    first: dict[str, int] = {}
    for i, flag in enumerate(flags):
        name = f"{flag['fid']} {flag['fname']}"
        by_name[name] += 1
        first.setdefault(name, i)
    ordered = sorted(by_name, key=lambda name: (-by_name[name], first[name]))
    return "; ".join(f"{name} ({by_name[name]})" for name in ordered) if ordered else "none"


def extract_code_counts(partial: str) -> str:
    try:
        after = partial.split("## Code counts", 1)[1]
        return after.split("## Flags", 1)[0].strip("\n")
    except IndexError as exc:
        raise ValueError("run 1 file lacks the expected Code counts/Flags sections") from exc


def render_one(repo: Path, slug: str, coverage: dict[str, str], flags: list[dict[str, str]], counts: dict) -> Path:
    article_dir = repo / "articles" / slug
    partial_path = article_dir / "analyses" / DATE / PARTIAL_NAME
    if not partial_path.is_file():
        raise FileNotFoundError(partial_path)
    partial = partial_path.read_text(encoding="utf-8")
    code_counts = extract_code_counts(partial)

    side_counts = Counter(flag["side"] for flag in flags)
    total = len(flags)
    title = counts["title"]
    url = counts["url"]
    snapshot = f"articles/{slug}/snapshots/{DATE}.txt"
    units_read = coverage["units_read"]
    units_total = coverage["units_total"]
    paras = coverage["paras"]
    table_rows = coverage["table_rows"]

    verdict = (
        f"Run 2 found {total} flag{'s' if total != 1 else ''}: "
        f"{side_counts['pro']} pro, {side_counts['anti']} anti, and "
        f"{side_counts['neutral']} neutral. The lean is {lean(side_counts)}. "
        f"Main patterns were {patterns(flags)}. Flags are judgment calls."
    )

    lines = [
        f"# Sophistry and fallacy scan: {title}",
        "",
        f"- **Article:** {title}",
        f"- **URL:** {url}",
        f"- **Snapshot file:** `{snapshot}` (sources: `2026-10-01_sources.csv`)",
        f"- **Snapshot date / scan date:** {DATE} / {DATE} (PT)",
        "- **Method:** substance_lens v0.5.9 fallacy scan, run 2 (full read, blind rerun). Both-sides by default; no outside fact-checking.",
        f"- **Reading coverage:** {units_read}/{units_total} units read in full ({paras} paragraphs, {table_rows} table rows).",
        "",
        "## Verdict",
        "",
        verdict,
        "",
        "## Code counts",
        "",
        code_counts,
        "",
        "## Flags",
        "",
        "Every flag below is a **judgment call** based on the run 2 reading, not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false.",
        "",
        "| n | quote | Fxxx Name | side | note |",
        "|---:|---|---|---|---|",
    ]
    if flags:
        for i, flag in enumerate(flags, 1):
            lines.append(
                "| " + " | ".join(
                    [
                        str(i),
                        esc_cell('"' + flag["quote"] + '"'),
                        esc_cell(f"{flag['fid']} {flag['fname']}"),
                        esc_cell(flag["side"]),
                        esc_cell(flag["note"]),
                    ]
                ) + " |"
            )
    else:
        lines.append("| — | No run 2 flags. | — | — | No judgment-based flags were recorded. |")
    lines.extend(
        [
            "",
            "## Both-sides balance note",
            "",
            f"Run 2 flag counts by side: pro {side_counts['pro']}, anti {side_counts['anti']}, neutral {side_counts['neutral']}. These are judgment-based labels, not measurements.",
            "",
            "## What wasn't checked",
            "",
            "- No outside fact-checking or source verification was performed.",
            "- Labels are judgment-based flags, not computed findings.",
            "- Reproducibility comparison: [COMPARISON.md](../../../SOPHISTRY_RERUN_2026-10-01/COMPARISON.md).",
            "",
        ]
    )
    out = article_dir / "analyses" / DATE / SCAN_NAME
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    repo = args.repo.resolve()
    rerun = repo / RERUN_DIR

    flags_rows = read_csv(rerun / "flags.csv")
    with (rerun / "coverage.tsv").open(newline="", encoding="utf-8") as fh:
        coverage_rows = list(csv.DictReader(fh, delimiter="\t"))
    coverage = {row["slug"]: row for row in coverage_rows if row["slug"] != "TOTAL"}
    with (repo / "tools/output/sophistry_counts_2026-10-01.json").open(encoding="utf-8") as fh:
        counts_rows = json.load(fh)
    counts = {row["slug"]: row for row in counts_rows}
    flags_by_slug: dict[str, list[dict[str, str]]] = {}
    for row in flags_rows:
        flags_by_slug.setdefault(row["slug"], []).append(row)

    slugs = set(coverage)
    if len(slugs) != 58:
        raise ValueError(f"expected 58 article coverage rows, found {len(slugs)}")
    if set(counts) != slugs:
        raise ValueError("coverage and code-count article sets differ")
    if set(flags_by_slug) - slugs:
        raise ValueError("flags contain unknown article slugs")
    for slug in sorted(slugs):
        flags = flags_by_slug.get(slug, [])
        expected = int(coverage[slug]["flags"])
        if len(flags) != expected:
            raise ValueError(f"{slug}: flags.csv has {len(flags)}, coverage.tsv says {expected}")
        render_one(repo, slug, coverage[slug], flags, counts[slug])
    print(f"wrote {len(slugs)} run 2 scan files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
