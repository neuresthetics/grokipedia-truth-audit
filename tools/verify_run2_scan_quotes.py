#!/usr/bin/env python3
"""Verify every run 2 flag quote occurs verbatim in its article snapshot."""
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

DATE = "2026-10-01"


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    topic = repo / "topics/circumcision"
    rerun = topic / "runs/2026-10-01_run2_full"
    with (rerun / "flags.csv").open(newline="", encoding="utf-8") as fh:
        flags = list(csv.DictReader(fh))
    by_slug = defaultdict(list)
    for row in flags:
        by_slug[row["slug"]].append(row)
    failures = []
    occurrences = []
    for slug, rows in sorted(by_slug.items()):
        snapshot_path = topic / "articles" / slug / "snapshots" / f"{DATE}.txt"
        text = snapshot_path.read_text(encoding="utf-8")
        for i, row in enumerate(rows, 1):
            count = text.count(row["quote"])
            occurrences.append(count)
            if count == 0:
                failures.append(f"{slug} flag {i}: quote absent from {snapshot_path}")
    print(f"checked {len(flags)} quotes in {len(by_slug)} articles")
    print(f"quotes found verbatim: {len(flags) - len(failures)}; absent: {len(failures)}")
    if failures:
        for failure in failures:
            print(failure)
        return 1
    duplicate_count = sum(n > 1 for n in occurrences)
    if duplicate_count:
        print(f"note: {duplicate_count} quote(s) occur more than once; all are present verbatim")
    print("QUOTE CHECK PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
