#!/usr/bin/env python3
"""Run-1 vs run-2 sophistry-scan comparison (2026-10-01 snapshots).

Run 1: flag tables in articles/<slug>/analyses/2026-10-01/sophistry_scan.md (read-only).
Run 2: flags.csv (full read of every sentence).
Matching: same article, and quotes equal after normalization (citation markers removed,
curly quotes/dashes unified, whitespace collapsed, case folded), or one normalized quote
contains the other. One-to-one greedy pairing, exact > normalized > containment.
Restricted analysis: run 1's read set is rebuilt by calling view() from
tools/sophistry_triage.py with each article's cap (taken from its 'Reading coverage' line);
it is accepted only if the lead and picked counts match what each scan file reports.
Writes comparison.json and prints the tables. Read-only on the repo (no bytecode written).
"""
import csv, json, os, re, sys
from collections import Counter, defaultdict
sys.dont_write_bytecode = True
REPO = '/workspace/gta_repo'
ART = f'{REPO}/articles'
HERE = os.path.dirname(os.path.abspath(__file__))
DATE = '2026-10-01'
slugs = json.load(open(f'{HERE}/slugs.json'))

# ---------- normalization ----------
def norm(s):
    s = re.sub(r'\s*\[\d+\]', '', s)
    s = s.replace('\u201c', '"').replace('\u201d', '"').replace('\u2018', "'").replace('\u2019', "'")
    s = s.replace('\u2013', '-').replace('\u2014', '-')
    s = re.sub(r'\s+', ' ', s).strip().lower()
    return s
def exact_strip(s):
    return re.sub(r'\s+', ' ', re.sub(r'\s*\[\d+\]', '', s)).strip()

# ---------- run 1 ----------
ROW = re.compile(r'^\| (\d+) \| "(.*)" \| (F\d{3}) ([^|]+?) \| ([^|]+?) \| (.*) \|\s*$')
SIDE1 = {'pro-circumcision': 'pro', 'anti-circumcision': 'anti', 'neutral/structural': 'neutral'}
run1 = []; caps = {}; cov1 = {}
for s in slugs:
    p = f'{ART}/{s}/analyses/{DATE}/sophistry_scan.md'
    txt = open(p, encoding='utf-8').read()
    m = re.search(r'Reading coverage:\*\* lead \((\d+) sentences?\) read in full, plus (\d+) of (\d+) body sentences .*?cap (\d+)\)', txt)
    assert m, s
    cov1[s] = dict(lead=int(m.group(1)), picked=int(m.group(2)), body=int(m.group(3)))
    caps[s] = int(m.group(4))
    for ln in txt.split('\n'):
        r = ROW.match(ln)
        if r:
            side = r.group(5).strip()
            assert side in SIDE1, (s, side)
            run1.append(dict(slug=s, quote=r.group(2), fid=r.group(3), fname=r.group(4).strip(),
                             side=SIDE1[side]))
# ‡ set from the run-1 summary table
summ = open(f'{ART}/SOPHISTRY_SCAN_SUMMARY_{DATE}.md', encoding='utf-8').read()
FGM = set(re.findall(r'\]\(([^/]+)/analyses/[^)]*\)[^\n]*‡', summ))
# run 2's FGM set, fixed before run 1 was opened (see handoff notes)
RUN2_FGM = {'prohibition-of-female-circumcision-act-1985', 'children-act-1989-amendment-female-genital-mutilation-act-2019',
    'clitoridectomy', 'female-genital-mutilation', 'female-genital-mutilation-act-2003', 'female-genital-mutilation-in-india',
    'female-genital-mutilation-in-new-zealand', 'female-genital-mutilation-in-nigeria', 'female-genital-mutilation-in-sudan',
    'female-genital-mutilation-in-the-gambia', 'female-genital-mutilation-in-the-united-kingdom',
    'female-genital-mutilation-in-the-united-states', 'female-genital-mutilation-laws-by-country', 'gishiri-cutting',
    'infibulation', 'international-day-of-zero-tolerance-for-female-genital-mutilation',
    'prevalence-of-female-genital-mutilation', 'religious-views-on-female-genital-mutilation',
    'women-unaffected-by-female-genital-cutting'}
assert FGM == RUN2_FGM, (FGM ^ RUN2_FGM)

# ---------- run 2 ----------
run2 = [dict(r) for r in csv.DictReader(open(f'{HERE}/flags.csv', encoding='utf-8'))]

# ---------- matching ----------
def rel(a, b):
    """0 exact, 1 normalized, 2 containment, None no match."""
    if exact_strip(a) == exact_strip(b): return 0
    na, nb = norm(a), norm(b)
    if na == nb: return 1
    if min(len(na), len(nb)) >= 20 and (na in nb or nb in na): return 2
    return None
def match(A, B):
    cand = []
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            if a['slug'] != b['slug']: continue
            k = rel(a['quote'], b['quote'])
            if k is not None: cand.append((k, i, j))
    cand.sort()
    ua, ub, pairs = set(), set(), []
    for k, i, j in cand:
        if i in ua or j in ub: continue
        ua.add(i); ub.add(j); pairs.append((i, j, k))
    return pairs
def agreement(A, B):
    pairs = match(A, B)
    m = len(pairs); o1 = len(A) - m; o2 = len(B) - m
    fid_same = sum(A[i]['fid'] == B[j]['fid'] for i, j, _ in pairs)
    side_same = sum(A[i]['side'] == B[j]['side'] for i, j, _ in pairs)
    both_same = sum(A[i]['fid'] == B[j]['fid'] and A[i]['side'] == B[j]['side'] for i, j, _ in pairs)
    return dict(run1=len(A), run2=len(B), matched=m, run1_only=o1, run2_only=o2,
                jaccard=m / (m + o1 + o2) if (m + o1 + o2) else None,
                run1_reproduced=m / len(A) if A else None,
                run2_in_run1=m / len(B) if B else None,
                fid_same=fid_same, side_same=side_same, fid_and_side_same=both_same,
                match_kinds=dict(Counter(['exact', 'normalized', 'containment'][k] for *_, k in pairs))), pairs

overall, pairs = agreement(run1, run2)

# ---------- restricted to run 1's read set ----------
sys.path.insert(0, f'{REPO}/tools')
import sophistry_triage as tri
readset = {}; recon_ok = {}
for s in slugs:
    sents, lead, pick = tri.view(s, DATE, caps[s])
    ok = (len(lead) == cov1[s]['lead'] and len(pick) == cov1[s]['picked']
          and len(sents) - len(lead) == cov1[s]['body'])
    recon_ok[s] = ok
    readset[s] = [norm(x['text']) for x in lead + pick]
def in_read(slug, q):
    nq = norm(q)
    return any(nq == t or (min(len(nq), len(t)) >= 20 and (nq in t or t in nq)) for t in readset[slug])
r1_in = [in_read(f['slug'], f['quote']) for f in run1]
r2_in = [in_read(f['slug'], f['quote']) for f in run2]
R1 = [f for f, k in zip(run1, r1_in) if k]
R2 = [f for f, k in zip(run2, r2_in) if k]
restricted, rpairs = agreement(R1, R2)
restricted['run1_flags_outside_reconstructed_readset'] = len(run1) - len(R1)
restricted['articles_reconstructed_exactly'] = sum(recon_ok.values())
# run-2 units falling in run-1 read set (coverage share)
units = [json.loads(l) for l in open(f'{HERE}/sentences.jsonl', encoding='utf-8')]
paras = [u for u in units if u['kind'] == 'para' and u['quote'] != '[Table]']
inr = sum(in_read(u['slug'], u['quote']) for u in paras)
restricted['run2_sentence_units_in_run1_readset'] = inr
restricted['run2_sentence_units_total'] = len(paras)
restricted['run1_readset_sentences'] = sum(len(v) for v in readset.values())
restricted['run1_total_sentences'] = sum(cov1[s]['lead'] + cov1[s]['body'] for s in slugs)

# ---------- per article, Spearman ----------
c1 = Counter(f['slug'] for f in run1); c2 = Counter(f['slug'] for f in run2)
cr1 = Counter(f['slug'] for f in R1); cr2 = Counter(f['slug'] for f in R2)
def ranks(x):
    order = sorted(range(len(x)), key=lambda i: x[i]); r = [0.0] * len(x); i = 0
    while i < len(x):
        j = i
        while j + 1 < len(x) and x[order[j + 1]] == x[order[i]]: j += 1
        for k in range(i, j + 1): r[order[k]] = (i + j) / 2 + 1
        i = j + 1
    return r
def pearson(a, b):
    n = len(a); ma = sum(a) / n; mb = sum(b) / n
    cov = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    va = sum((x - ma) ** 2 for x in a); vb = sum((y - mb) ** 2 for y in b)
    return cov / (va * vb) ** 0.5
def spearman(a, b): return pearson(ranks(a), ranks(b))
v1 = [c1[s] for s in slugs]; v2 = [c2[s] for s in slugs]
rho = spearman(v1, v2)
rho_r = spearman([cr1[s] for s in slugs], [cr2[s] for s in slugs])
# permutation p-value (two-sided), fixed seed
import random
rnd = random.Random(20261001); r2r = ranks(v2); r1r = ranks(v1); hits = 0; N = 20000
for _ in range(N):
    p = r2r[:]; rnd.shuffle(p)
    if abs(pearson(r1r, p)) >= abs(rho) - 1e-12: hits += 1
rho_p = (hits + 1) / (N + 1)
try:
    from scipy.stats import spearmanr
    sc_rho = spearmanr(v1, v2)
    scipy_check = dict(rho=float(sc_rho[0]), p=float(sc_rho[1]))
except Exception as e:
    scipy_check = f'scipy unavailable ({type(e).__name__})'

# per-article matched counts
pm = Counter(run1[i]['slug'] for i, j, _ in pairs)
per_article = []
for s in slugs:
    a1 = [f for f in run1 if f['slug'] == s]; a2 = [f for f in run2 if f['slug'] == s]
    def lean(fl):
        c = Counter(f['side'] for f in fl)
        if not fl: return 'none'
        top = max(c.values()); w = sorted(k for k, v in c.items() if v == top)
        return w[0] if len(w) == 1 else 'mixed'
    per_article.append(dict(slug=s, fgm=s in FGM, run1=c1[s], run2=c2[s], matched=pm[s],
                            run1_in_readset=cr1[s], run2_in_readset=cr2[s],
                            lean1=lean(a1), lean2=lean(a2),
                            r1_pro=sum(f['side'] == 'pro' for f in a1), r1_anti=sum(f['side'] == 'anti' for f in a1),
                            r2_pro=sum(f['side'] == 'pro' for f in a2), r2_anti=sum(f['side'] == 'anti' for f in a2),
                            readset_reconstructed=recon_ok[s]))

# side split
def split(fl):
    out = {}
    for grp, sel in (('male (non-‡)', lambda f: f['slug'] not in FGM), ('FGM (‡)', lambda f: f['slug'] in FGM), ('all', lambda f: True)):
        c = Counter(f['side'] for f in fl if sel(f))
        out[grp] = dict(pro=c['pro'], anti=c['anti'], neutral=c['neutral'], total=sum(c.values()))
    return out
sides = dict(run1=split(run1), run2=split(run2), run1_restricted=split(R1), run2_restricted=split(R2))

# side confusion on matched pairs
conf = Counter((run1[i]['side'], run2[j]['side']) for i, j, _ in pairs)

# fallacy-type distribution and per-type stability
FN = {}
for f in run1 + run2: FN.setdefault(f['fid'], f['fname'])
t1 = Counter(f['fid'] for f in run1); t2 = Counter(f['fid'] for f in run2)
tr1 = Counter(f['fid'] for f in R1); tr2 = Counter(f['fid'] for f in R2)
same_by_fid = Counter(run1[i]['fid'] for i, j, _ in pairs if run1[i]['fid'] == run2[j]['fid'])
same_by_fid_r = Counter(R1[i]['fid'] for i, j, _ in rpairs if R1[i]['fid'] == R2[j]['fid'])
types = []
for fid in sorted(set(t1) | set(t2)):
    a, b, m = t1[fid], t2[fid], same_by_fid[fid]
    ar, br, mr = tr1[fid], tr2[fid], same_by_fid_r[fid]
    types.append(dict(fid=fid, fname=FN[fid], run1=a, run2=b, same_sentence_same_fid=m,
                      dice=2 * m / (a + b) if a + b else None,
                      run1_restricted=ar, run2_restricted=br, same_restricted=mr,
                      dice_restricted=2 * mr / (ar + br) if ar + br else None))
# matched-pair F-ID confusion (what run 1 called it vs what run 2 called it)
fid_conf = Counter((run1[i]['fid'], run2[j]['fid']) for i, j, _ in pairs)

res = dict(overall=overall, restricted=restricted, spearman_per_article_counts=rho,
           spearman_permutation_p=rho_p, spearman_scipy_check=scipy_check,
           spearman_restricted_counts=rho_r, sides=sides,
           side_confusion_matched={f'{a}->{b}': n for (a, b), n in sorted(conf.items())},
           fid_confusion_matched={f'{a}->{b}': n for (a, b), n in fid_conf.most_common()},
           types=types, per_article=per_article, fgm_slugs=sorted(FGM),
           matched_pairs=[dict(slug=run1[i]['slug'], kind=['exact', 'normalized', 'containment'][k],
                               run1_fid=run1[i]['fid'], run2_fid=run2[j]['fid'],
                               run1_side=run1[i]['side'], run2_side=run2[j]['side'],
                               run1_quote=run1[i]['quote'], run2_quote=run2[j]['quote']) for i, j, k in pairs])

# ---------- supplementary diagnostics ----------
# (a) map every flag to a run-2 sentence unit id (sid) to look for adjacent-sentence near misses
U = defaultdict(list)
for u in units: U[u['slug']].append(u)
def sid_of(slug, q):
    nq = norm(q)
    for u in U[slug]:
        t = norm(u['quote'])
        if nq == t or (min(len(nq), len(t)) >= 20 and (nq in t or t in nq)): return u['sid']
    return None
m1 = {i for i, j, _ in pairs}; m2 = {j for i, j, _ in pairs}
o1 = [(f['slug'], sid_of(f['slug'], f['quote'])) for i, f in enumerate(run1) if i not in m1]
o2 = defaultdict(set)
for j, f in enumerate(run2):
    if j not in m2: o2[f['slug']].add(sid_of(f['slug'], f['quote']))
near = sum(1 for s, sid in o1 if sid is not None and ({sid - 1, sid + 1} & o2[s]))
unmapped1 = sum(1 for s, sid in o1 if sid is None)
diag = dict(run1_only_with_run2_only_flag_on_adjacent_sentence=near, run1_only_unmapped_to_run2_units=unmapped1)
# (b) article-level lean agreement
both = [a for a in per_article if a['run1'] and a['run2']]
diag['articles_flagged_in_both_runs'] = len(both)
diag['articles_same_lean'] = sum(a['lean1'] == a['lean2'] for a in both)
diag['articles_pro_anti_reversal'] = sum({a['lean1'], a['lean2']} == {'pro', 'anti'} for a in both)
for g, sel in (('male', lambda a: not a['fgm']), ('fgm', lambda a: a['fgm'])):
    bb = [a for a in both if sel(a)]
    diag[f'articles_both_flagged_{g}'] = len(bb); diag[f'articles_same_lean_{g}'] = sum(a['lean1'] == a['lean2'] for a in bb)
diag['articles_flagged_in_one_run_only'] = sum(bool(a['run1']) != bool(a['run2']) for a in per_article)
diag['articles_zero_in_both'] = sum(not a['run1'] and not a['run2'] for a in per_article)
# (c) pro share of directional (pro+anti) flags, by group; also FGM group without the outlier article
def pshare(fl, sel):
    p = sum(f['side'] == 'pro' for f in fl if sel(f)); a = sum(f['side'] == 'anti' for f in fl if sel(f))
    return dict(pro=p, anti=a, pro_share=p / (p + a) if p + a else None)
OUT = 'women-unaffected-by-female-genital-cutting'
for name, fl in (('run1', run1), ('run2', run2), ('run1_restricted', R1), ('run2_restricted', R2)):
    diag[f'pro_share_{name}'] = dict(
        male=pshare(fl, lambda f: f['slug'] not in FGM), fgm=pshare(fl, lambda f: f['slug'] in FGM),
        fgm_excl_women_unaffected=pshare(fl, lambda f: f['slug'] in FGM and f['slug'] != OUT))
# (d) male-group per-article Spearman and FGM-group per-article Spearman
diag['spearman_male_articles'] = spearman([c1[s] for s in slugs if s not in FGM], [c2[s] for s in slugs if s not in FGM])
diag['spearman_fgm_articles'] = spearman([c1[s] for s in slugs if s in FGM], [c2[s] for s in slugs if s in FGM])
res['diagnostics'] = diag
json.dump(res, open(f'{HERE}/comparison.json', 'w'), indent=1, ensure_ascii=False)
print(json.dumps({k: res[k] for k in ['overall', 'restricted', 'spearman_per_article_counts', 'spearman_permutation_p',
                                      'spearman_scipy_check', 'spearman_restricted_counts', 'sides', 'side_confusion_matched']}, indent=1, ensure_ascii=False))
print(json.dumps(res['diagnostics'], indent=1))
print('FGM set size', len(FGM))
print('fid confusion top', fid_conf.most_common(15))

# ---------- markdown tables (written to tables.md; embedded in COMPARISON.md) ----------
def pct(x): return 'n/a' if x is None else f'{100*x:.1f}%'
L = []
o, r = res['overall'], res['restricted']
L += ['### Table 1. Sentence-level agreement', '',
      '| Scope | Run 1 flags | Run 2 flags | Matched | Run 1 only | Run 2 only | Jaccard | Share of run 1 reproduced | Share of run 2 also in run 1 |',
      '|---|---|---|---|---|---|---|---|---|']
for name, d in (('All sentences', o), ("Restricted to run 1's read set", r)):
    L.append(f"| {name} | {d['run1']} | {d['run2']} | {d['matched']} | {d['run1_only']} | {d['run2_only']} | {d['jaccard']:.3f} | {pct(d['run1_reproduced'])} | {pct(d['run2_in_run1'])} |")
L += ['', f"Match types: {o['match_kinds']}. Run 1 flags outside the reconstructed read set: {r['run1_flags_outside_reconstructed_readset']}. "
      f"Articles whose read set was rebuilt with exactly the lead/picked/body counts the scan file states: {r['articles_reconstructed_exactly']} of 58. "
      f"Run 1 read set: {r['run1_readset_sentences']} of {r['run1_total_sentences']} run-1 sentences ({pct(r['run1_readset_sentences']/r['run1_total_sentences'])}); "
      f"{r['run2_sentence_units_in_run1_readset']} of {r['run2_sentence_units_total']} run-2 prose units fall in it.", '']
L += ['### Table 2. Labels on matched sentences', '', '| Measure | Count | Share of matched |', '|---|---|---|']
for k, lab in (('fid_same', 'Same F-ID'), ('side_same', 'Same side label'), ('fid_and_side_same', 'Same F-ID and same side')):
    L.append(f"| {lab} | {o[k]} of {o['matched']} | {pct(o[k]/o['matched'])} |")
L += ['', 'Side labels on matched sentences (run 1 → run 2):', '', '| Run 1 → Run 2 | Count |', '|---|---|']
for k, v in res['side_confusion_matched'].items(): L.append(f'| {k} | {v} |')
L += ['', 'Most common F-ID pairs on matched sentences (run 1 → run 2):', '', '| Run 1 → Run 2 | Count |', '|---|---|']
for k, v in list(res['fid_confusion_matched'].items())[:25]: L.append(f'| {k} | {v} |')
L += ['', '### Table 3. Side split per run', '',
      '| Run | Group | Pro | Anti | Neutral | Total | Pro share of pro+anti |', '|---|---|---|---|---|---|---|']
for run in ('run1', 'run2', 'run2_restricted'):
    for g in ('male (non-‡)', 'FGM (‡)', 'all'):
        d = res['sides'][run][g]; ps = d['pro'] / (d['pro'] + d['anti']) if d['pro'] + d['anti'] else None
        L.append(f"| {run.replace('_restricted',' (run-1 read set only)')} | {g} | {d['pro']} | {d['anti']} | {d['neutral']} | {d['total']} | {pct(ps)} |")
dg = res['diagnostics']
L += ['', f"FGM (‡) group without *Women unaffected by female genital cutting*: run 1 pro {dg['pro_share_run1']['fgm_excl_women_unaffected']['pro']} / anti {dg['pro_share_run1']['fgm_excl_women_unaffected']['anti']} "
      f"({pct(dg['pro_share_run1']['fgm_excl_women_unaffected']['pro_share'])} pro); run 2 pro {dg['pro_share_run2']['fgm_excl_women_unaffected']['pro']} / anti {dg['pro_share_run2']['fgm_excl_women_unaffected']['anti']} "
      f"({pct(dg['pro_share_run2']['fgm_excl_women_unaffected']['pro_share'])} pro). ‡ set = the {len(FGM)} articles marked ‡ in run 1's summary; it is identical to run 2's FGM set.", '']
L += ['### Table 4. Fallacy-type distribution and per-type agreement', '',
      'Dice = 2 × (sentences flagged by both runs with this same F-ID) / (run 1 count + run 2 count). Types are sorted by combined count.', '',
      '| F-ID | Name | Run 1 | Run 2 | Same sentence, same F-ID | Dice | Run 2 within run-1 read set | Dice (read set only) |', '|---|---|---|---|---|---|---|---|']
for t in sorted(res['types'], key=lambda t: (-(t['run1'] + t['run2']), t['fid'])):
    L.append(f"| {t['fid']} | {t['fname']} | {t['run1']} | {t['run2']} | {t['same_sentence_same_fid']} | {t['dice']:.2f} | {t['run2_restricted']} | {'n/a' if t['dice_restricted'] is None else format(t['dice_restricted'], '.2f')} |")
L += ['', '### Table 5. Per-article flag counts', '',
      f"Spearman rank correlation of per-article counts (58 articles): **{res['spearman_per_article_counts']:.3f}** "
      f"(two-sided permutation p ≈ {res['spearman_permutation_p']:.5f}, 20,000 permutations, seed 20261001; scipy not installed, so the rank correlation was computed with the script's own average-rank Pearson). "
      f"Restricted counts (run-1 read set only): {res['spearman_restricted_counts']:.3f}. Male articles only (39): {dg['spearman_male_articles']:.3f}; ‡ articles only (19): {dg['spearman_fgm_articles']:.3f}.", '',
      f"Article lean (side with most flags; ties = mixed): {dg['articles_flagged_in_both_runs']} articles have flags in both runs; same lean in {dg['articles_same_lean']}; pro↔anti reversals: {dg['articles_pro_anti_reversal']}. Same lean, male articles: {dg['articles_same_lean_male']} of {dg['articles_both_flagged_male']}; ‡ articles: {dg['articles_same_lean_fgm']} of {dg['articles_both_flagged_fgm']}. "
      f"Flagged in one run only: {dg['articles_flagged_in_one_run_only']}; zero in both: {dg['articles_zero_in_both']}. "
      f"Run-1-only flags with a run-2-only flag on an adjacent sentence (possible near misses, not counted as matches): {dg['run1_only_with_run2_only_flag_on_adjacent_sentence']}.", '',
      '| # | Article | ‡ | Run 1 | Run 2 | Matched | Run 2 in run-1 read set | Run 1 lean | Run 2 lean | Run 1 pro/anti | Run 2 pro/anti |', '|---|---|---|---|---|---|---|---|---|---|---|']
for n, a in enumerate(res['per_article'], 1):
    L.append(f"| {n} | {a['slug']} | {'‡' if a['fgm'] else ''} | {a['run1']} | {a['run2']} | {a['matched']} | {a['run2_in_readset']} | {a['lean1']} | {a['lean2']} | {a['r1_pro']}/{a['r1_anti']} | {a['r2_pro']}/{a['r2_anti']} |")
L.append(f"| | **Total** | | **{o['run1']}** | **{o['run2']}** | **{o['matched']}** | **{r['run2']}** | | | | |")
open(f'{HERE}/tables.md', 'w').write('\n'.join(L) + '\n')
print('wrote tables.md and comparison.json')
