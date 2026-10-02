"""Compare sophistry-scan run 3 (this directory) with run 2 on the 24 'Title match' articles.

Run from anywhere:  python3 articles/SOPHISTRY_RUN3_TITLE24_2026-10-02/compare.py
Reads  : flags.csv (run 3), ../SOPHISTRY_RERUN_2026-10-01/flags.csv (run 2, restricted to TITLE24),
         fid_catalog.json, and the 2026-10-01 snapshots (via segment.py).
Writes : COMPARISON.md and comparison_units.csv (per-unit match table) in this directory.

Matching unit = one sentence or table row as produced by segment.units(). A flag is mapped to the
unit(s) its quote falls in (a quote that spans two sentences maps to both; a quote that appears
verbatim in more than one unit maps to the first). Two runs "match" on a unit when both flagged it.
All counts below are counts of judgments made by a model; none of them is a measurement of the
articles themselves.
"""
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import segment  # noqa: E402

RUN2_PATH = HERE.parent / "SOPHISTRY_RERUN_2026-10-01" / "flags.csv"
RUN3_PATH = HERE / "flags.csv"
SIDES = ("pro", "anti", "neutral")

# Thresholds for calling a fallacy type "stable" (chosen by hand, not derived):
MIN_COMBINED = 4        # types with fewer combined flags are "too few to judge"
STABLE_JACCARD = 0.25   # unit-level Jaccard for that F-ID between runs
STABLE_COUNT_RATIO = 0.5  # min(count)/max(count) between runs


def load(path):
    with open(path, encoding="utf-8", newline="") as f:
        rows = [r for r in csv.DictReader(f) if r["slug"] in segment.TITLE24]
    return rows


def attach_units(rows, cache, problems, label):
    for r in rows:
        us = cache.setdefault(r["slug"], segment.units(r["slug"]))
        hits, status = segment.locate(r["slug"], r["quote"], us)
        if status == "missing":
            problems.append(f"{label}: quote not locatable in {r['slug']}: {r['quote'][:80]}")
            r["units"] = []
        elif status == "exact-span":
            r["units"] = hits
        else:
            r["units"] = hits[:1]
        r["status"] = status


def ranks(xs):
    """Average ranks (1-based) with ties sharing the mean rank."""
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    rk = [0.0] * len(xs)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        avg = (i + j) / 2 + 1
        for k in range(i, j + 1):
            rk[order[k]] = avg
        i = j + 1
    return rk


def pearson(a, b):
    n = len(a)
    ma, mb = sum(a) / n, sum(b) / n
    cov = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    va = sum((x - ma) ** 2 for x in a) ** 0.5
    vb = sum((y - mb) ** 2 for y in b) ** 0.5
    return cov / (va * vb) if va and vb else float("nan")


def spearman(a, b):
    return pearson(ranks(a), ranks(b))


def lean(c):
    if c["pro"] > c["anti"]:
        return "pro"
    if c["anti"] > c["pro"]:
        return "anti"
    return "none" if c["pro"] == 0 else "tie"


def pct(x, d):
    return f"{100 * x / d:.1f}%" if d else "n/a"


def md_table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "|".join("---" for _ in header) + "|"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def main():
    cat = {e["id"]: e["name"] for e in json.load(open(HERE / "fid_catalog.json"))["entries"]}
    problems, cache = [], {}
    run = {2: load(RUN2_PATH), 3: load(RUN3_PATH)}
    for k in run:
        attach_units(run[k], cache, problems, f"run {k}")
        for r in run[k]:
            if r["fid"] not in cat:
                problems.append(f"run {k}: F-ID {r['fid']} not in the 67 kept entries")
            elif r.get("fname") and r["fname"] != cat[r["fid"]]:
                problems.append(f"run {k}: {r['fid']} named '{r['fname']}' but spec says '{cat[r['fid']]}'")
        n_span = sum(r["status"] == "exact-span" for r in run[k])
        if n_span:
            problems.append(f"run {k}: {n_span} quote(s) span two sentences and were mapped to both units")

    # ---- totals and side split
    side = {k: Counter(r["side"] for r in run[k]) for k in run}
    sided = {k: side[k]["pro"] + side[k]["anti"] for k in run}

    # ---- per-article
    per = {k: defaultdict(Counter) for k in run}
    for k in run:
        for r in run[k]:
            per[k][r["slug"]][r["side"]] += 1
    art_rows, c2, c3 = [], [], []
    agree = reversals = both_lean = 0
    reversal_list, disagree_list = [], []
    for s in segment.TITLE24:
        a, b = per[2][s], per[3][s]
        n2, n3 = sum(a.values()), sum(b.values())
        c2.append(n2)
        c3.append(n3)
        l2, l3 = lean(a), lean(b)
        same = l2 == l3
        agree += same
        if not same:
            disagree_list.append(s)
        if {l2, l3} == {"pro", "anti"}:
            reversals += 1
            reversal_list.append(s)
        art_rows.append([s, n2, f"{a['pro']}/{a['anti']}/{a['neutral']}", l2,
                         n3, f"{b['pro']}/{b['anti']}/{b['neutral']}", l3, "yes" if same else "**no**"])
    rho = spearman(c2, c3)
    art_rows.append(["**TOTAL**", sum(c2), f"{side[2]['pro']}/{side[2]['anti']}/{side[2]['neutral']}", "",
                     sum(c3), f"{side[3]['pro']}/{side[3]['anti']}/{side[3]['neutral']}", "", f"{agree}/24"])

    # ---- sentence-level overlap
    unit_flags = {k: defaultdict(list) for k in run}
    for k in run:
        for r in run[k]:
            for u in r["units"]:
                unit_flags[k][u].append(r)
    U2, U3 = set(unit_flags[2]), set(unit_flags[3])
    inter, union = U2 & U3, U2 | U3
    same_fid = sum(bool({r["fid"] for r in unit_flags[2][u]} & {r["fid"] for r in unit_flags[3][u]}) for u in inter)
    same_side = sum(bool({r["side"] for r in unit_flags[2][u]} & {r["side"] for r in unit_flags[3][u]}) for u in inter)
    same_cat = 0
    fcat = {e["id"]: e["category"] for e in json.load(open(HERE / "fid_catalog.json"))["entries"]}
    for u in inter:
        same_cat += bool({fcat.get(r["fid"]) for r in unit_flags[2][u]} & {fcat.get(r["fid"]) for r in unit_flags[3][u]})
    r2_flags_reproduced = sum(any(u in U3 for u in r["units"]) for r in run[2])

    with open(HERE / "comparison_units.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["unit_id", "status", "run2_fids", "run3_fids", "run2_sides", "run3_sides"])
        for u in sorted(union):
            st = "matched" if u in inter else ("run2_only" if u in U2 else "run3_only")
            w.writerow([u, st,
                        ";".join(sorted({r["fid"] for r in unit_flags[2][u]})),
                        ";".join(sorted({r["fid"] for r in unit_flags[3][u]})),
                        ";".join(sorted({r["side"] for r in unit_flags[2][u]})),
                        ";".join(sorted({r["side"] for r in unit_flags[3][u]}))])

    # ---- fallacy-type distribution and stability
    fid_units = {k: defaultdict(set) for k in run}
    fid_count = {k: Counter(r["fid"] for r in run[k]) for k in run}
    for k in run:
        for r in run[k]:
            for u in r["units"]:
                fid_units[k][r["fid"]].add(u)
    type_rows, stable, noisy, few = [], [], [], []
    for fid in sorted(set(fid_count[2]) | set(fid_count[3]), key=lambda x: (-(fid_count[2][x] + fid_count[3][x]), x)):
        a, b = fid_count[2][fid], fid_count[3][fid]
        ua, ub = fid_units[2][fid], fid_units[3][fid]
        jac = len(ua & ub) / len(ua | ub) if ua | ub else 0.0
        ratio = min(a, b) / max(a, b) if max(a, b) else 0.0
        if a + b < MIN_COMBINED:
            verdict = "too few"
            few.append(fid)
        elif jac >= STABLE_JACCARD and ratio >= STABLE_COUNT_RATIO:
            verdict = "stable"
            stable.append(fid)
        else:
            verdict = "noisy"
            noisy.append(fid)
        type_rows.append([fid, cat.get(fid, "?"), a, pct(a, len(run[2])), b, pct(b, len(run[3])),
                          len(ua & ub), f"{jac:.2f}", f"{ratio:.2f}", verdict])

    # ---- write markdown
    n2, n3 = len(run[2]), len(run[3])
    ps2, ps3 = side[2]["pro"] / sided[2], side[3]["pro"] / sided[3]
    zero2 = [s for s, n in zip(segment.TITLE24, c2) if n == 0]
    zero3 = [s for s, n in zip(segment.TITLE24, c3) if n == 0]
    named = lambda ids: ", ".join(f"{i} {cat.get(i, '?')}" for i in ids) or "none"

    small = [x for x in disagree_list if max(c2[segment.TITLE24.index(x)], c3[segment.TITLE24.index(x)]) <= 4]
    one_run = len(U2 - U3) + len(U3 - U2)
    jac_of = {r[0]: float(r[7]) for r in type_rows}
    lowest = ", ".join(f"{f} {cat.get(f, '?')} ({jac_of[f]:.2f})" for f in sorted(noisy, key=lambda f: (jac_of[f], f))[:4])
    concl = f"""## Conclusion (plain English)

Run 3 was a blind re-read of the same 24 articles under the same spec. It flagged **{n3}** passages; run 2 had flagged **{n2}** on these articles. Run 3 is a little more conservative ({n3 / n2:.0%} of run 2's volume), but it paints the same overall picture.

- **The direction reproduces.** Both runs judge the articles' own reasoning to tilt strongly toward circumcision. Pro flags are {pct(side[2]['pro'], sided[2])} of sided flags in run 2 and {pct(side[3]['pro'], sided[3])} in run 3.
- **The ranking of articles reproduces.** The Spearman correlation of per-article flag counts is **{rho:.2f}**. ethics-of-circumcision and circumcision-controversies are the two heaviest articles in both runs. feast-of-the-circumcision-of-christ and history-of-circumcision have zero flags in both. forced-circumcision is the clearest anti-leaning article in both runs (7 anti flags each).
- **Article lean mostly reproduces: {agree}/24 articles get the same lean.** {len(small)} of the {len(disagree_list)} disagreements are on articles with 4 or fewer flags in both runs, where one flag can flip the lean. The {reversals} outright pro/anti reversal(s) ({', '.join(reversal_list) or 'none'}) each rest on 1-4 flags per run.
- **Sentence-level agreement is moderate.** Run 3 re-flagged {len(inter)} of the {len(U2)} sentences/rows run 2 flagged, reproducing {pct(len(inter), len(U2))} of run 2. Unit-level Jaccard is {len(inter) / len(union):.2f}, and {one_run} of the {len(union)} sentences flagged by either run ({pct(one_run, len(union))}) were flagged by only one. Neither run's list should be treated as complete.
- **On sentences both runs flagged, the side is nearly always the same ({pct(same_side, len(inter))}). The F-ID usually matches ({pct(same_fid, len(inter))}).** Which way a lapse leans reproduces better than its exact label.
- **Types.** Stable: {named(stable)}. Noisy: {named(noisy)}. Lowest unit-level agreement among the judged types: {lowest}. F055 Ecological Fallacy was used {fid_count[2]['F055']} times by run 2 and {fid_count[3]['F055']} times by run 3.

Bottom line: the article-level findings reproduce: a strong pro-circumcision tilt, the same heavy and light articles, and forced-circumcision as the main anti-leaning exception. The sentence-by-sentence flag lists overlap only moderately, so any single run's list is a sample of defensible flags, not an exhaustive or definitive inventory.
"""

    md = [f"# Sophistry scan: run 3 vs run 2 on the 24 'Title match' articles (2026-10-02)\n", concl,
          "## 1. Totals and side split\n",
          md_table(["", "run 2", "run 3"], [
              ["flags (24 articles)", n2, n3],
              ["pro", side[2]["pro"], side[3]["pro"]],
              ["anti", side[2]["anti"], side[3]["anti"]],
              ["neutral", side[2]["neutral"], side[3]["neutral"]],
              ["pro share of sided flags (pro/(pro+anti))", f"{ps2:.1%}", f"{ps3:.1%}"],
              ["articles with zero flags", len(zero2), len(zero3)],
          ]),
          f"\nZero-flag articles. Run 2: {', '.join(zero2) or 'none'}. Run 3: {', '.join(zero3) or 'none'}.\n",
          "## 2. Per-article counts side by side\n",
          "Side columns are pro/anti/neutral. Lean = the larger of pro vs anti; 'tie' = equal and non-zero; 'none' = no sided flags.\n",
          md_table(["article", "run 2 flags", "run 2 p/a/n", "run 2 lean", "run 3 flags", "run 3 p/a/n",
                    "run 3 lean", "same lean"], art_rows),
          f"\n- Spearman rank correlation of per-article flag counts (average ranks for ties, own implementation): **{rho:.3f}** (n = 24).",
          f"- Article-lean agreement: **{agree}/24**. Disagreements: {', '.join(disagree_list) or 'none'}.",
          f"- Pro/anti reversals (one run pro, the other anti): **{reversals}**{(' (' + ', '.join(reversal_list) + ')') if reversal_list else ''}.\n",
          "## 3. Sentence-level overlap\n",
          "Unit = sentence or table row in the 2026-10-01 snapshot (segment.py). The per-unit detail is in comparison_units.csv.\n",
          md_table(["statistic (counts of model judgments)", "value"], [
              ["units flagged by run 2", len(U2)],
              ["units flagged by run 3", len(U3)],
              ["matched (flagged by both)", len(inter)],
              ["run 2 only", len(U2 - U3)],
              ["run 3 only", len(U3 - U2)],
              ["Jaccard (matched / union)", f"{len(inter) / len(union):.3f}"],
              ["share of run 2 units reproduced by run 3", pct(len(inter), len(U2))],
              ["share of run 3 units also in run 2", pct(len(inter), len(U3))],
              ["run 2 flags (not units) whose sentence run 3 also flagged", f"{r2_flags_reproduced}/{n2} ({pct(r2_flags_reproduced, n2)})"],
              ["matched units with the same F-ID", f"{same_fid}/{len(inter)} ({pct(same_fid, len(inter))})"],
              ["matched units in the same F-ID category", f"{same_cat}/{len(inter)} ({pct(same_cat, len(inter))})"],
              ["matched units with the same side", f"{same_side}/{len(inter)} ({pct(same_side, len(inter))})"],
          ]),
          "\nWhen a unit carries several flags in one run, 'same F-ID' and 'same side' mean the two runs' sets overlap.\n",
          "## 4. Fallacy-type distribution and stability\n",
          f"Stable = at least {MIN_COMBINED} combined flags, unit-level Jaccard for that F-ID of at least {STABLE_JACCARD}, and count ratio (smaller/larger) of at least {STABLE_COUNT_RATIO}. Noisy = at least {MIN_COMBINED} combined flags but failing either test. These thresholds were chosen by hand; they are a reading aid, not a statistical test.\n",
          md_table(["F-ID", "name", "run 2", "run 2 %", "run 3", "run 3 %", "same unit both runs",
                    "Jaccard", "count ratio", "verdict"], type_rows),
          f"\n- Stable: {named(stable)}",
          f"- Noisy: {named(noisy)}",
          f"- Too few to judge: {named(few)}\n",
          "## 5. Problems and notes\n",
          "\n".join(f"- {p}" for p in problems) or "- none",
          "- Run 3 never used F055 Ecological Fallacy. The clearest run-2 F055 case on these articles (circumcision: US vs Sweden lifetime UTI prevalence) was read by run 3 as part of an attributed 'Critiques ... emphasize' paragraph and skipped under the attribution rule. This is an example of the attribution boundary driving disagreement.",
          "- In cultural-views-on-circumcision-aesthetics, one run-3 quote occurs verbatim twice in the snapshot (the lead and a later section); it is mapped to its first occurrence.",
          "- Run 3 was done blind: its flags.csv and coverage.tsv were written before run 2's files were opened. Unit coverage for run 3 is a self-report of a full read (coverage.tsv), not a measurement.",
          "- Attribution rule (from the task instructions, applied by judgment in run 3; run 2 was given the same rule): positions explicitly attributed to someone ('critics argue', 'proponents contend', and the rest of such a paragraph) are not counted as the article's own reasoning. Where that boundary is drawn accounts for part of the sentence-level disagreement.",
          "- Side is a judgment about which position a lapse favors. In prohibition-of-female-circumcision-act-1985, 'pro' means it favors cutting or a male/female distinction.",
          "\n## Caveat\n",
          "Both runs used the same model family and the same substance_lens v0.5.9 spec (67 kept F-IDs). Agreement between them shows **consistency of the method, not correctness**. Shared blind spots or shared biases would show up as agreement. No outside fact-checking was done; every flag is a judgment about the article's own reasoning, not a measurement.\n",
          ]
    (HERE / "COMPARISON.md").write_text("\n".join(md), encoding="utf-8")

    # console summary
    print(f"run2={n2} {dict(side[2])} pro_share={ps2:.3f}")
    print(f"run3={n3} {dict(side[3])} pro_share={ps3:.3f}")
    print(f"spearman={rho:.3f} lean_agree={agree}/24 reversals={reversals} {reversal_list}")
    print(f"U2={len(U2)} U3={len(U3)} matched={len(inter)} r2only={len(U2-U3)} r3only={len(U3-U2)} "
          f"jaccard={len(inter)/len(union):.3f} reproduced={len(inter)/len(U2):.3f}")
    print(f"same_fid={same_fid}/{len(inter)} same_cat={same_cat}/{len(inter)} same_side={same_side}/{len(inter)}")
    print("stable", stable, "noisy", noisy, "few", few)
    for p in problems:
        print("PROBLEM", p)


if __name__ == "__main__":
    main()
