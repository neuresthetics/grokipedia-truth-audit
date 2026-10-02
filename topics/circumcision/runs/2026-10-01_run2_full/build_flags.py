#!/usr/bin/env python3
"""Build flags.csv from raw_flags.tsv (run 2).
Each snippet (taken from the citation-stripped reading view) is mapped to its sentence
unit in sentences.jsonl; the output quote is the exact raw sentence text from the
snapshot (trailing citation markers removed). fname is taken from the spec JSON.
Also writes coverage.tsv."""
import csv, json, re, sys
from collections import Counter, defaultdict
REPO='topics/circumcision/articles'
spec=json.load(open('substance_lens v0.5.9 spec'))
def find_kept(o):
    if isinstance(o,dict):
        if 'fallacyScanPass' in o: return o['fallacyScanPass']['kept']
        for v in o.values():
            r=find_kept(v)
            if r is not None: return r
    return None
kept=find_kept(spec)
FN={}
for e in kept:
    fid=e.get('id') or e.get('fid') or e.get('F-ID')
    FN[fid]=e.get('name')
assert len(FN)==67, len(FN)
slugs=json.load(open('slugs.json'))
units=defaultdict(list)
for line in open('sentences.jsonl',encoding='utf-8'):
    r=json.loads(line); units[r['slug']].append(r)
snap={s:open(f'{REPO}/{s}/snapshots/2026-10-01.txt',encoding='utf-8').read() for s in slugs}
strip=lambda s: re.sub(r'\s*\[\d+\]','',s)
norm=lambda s: re.sub(r'\s+',' ',s).strip()
out=[]; fails=[]; method=Counter()
with open('raw_flags.tsv',encoding='utf-8') as f:
    rd=csv.reader(f,delimiter='\t',quoting=csv.QUOTE_NONE)
    hdr=next(rd)
    for row in rd:
        if not row or not row[0].strip(): continue
        slug,snip,fid,side,note=row
        assert slug in snap, slug
        assert fid in FN, fid
        assert side in ('pro','anti','neutral'), side
        hits=[u for u in units[slug] if snip in strip(u['quote'])]
        how='exact'
        if not hits:
            hits=[u for u in units[slug] if norm(snip) in norm(strip(u['quote']))]; how='ws-normalized'
        if not hits:
            fails.append((slug,snip)); continue
        texts={u['quote'] for u in hits}
        if len(texts)>1:
            fails.append((slug,'AMBIGUOUS: '+snip)); continue
        if len(hits)>1: how+='+dup-first'
        u=hits[0]; method[how]+=1
        q=u['quote']
        assert q in snap[slug] and snap[slug][u['start']:u['end']]==q
        out.append(dict(slug=slug,quote=q,fid=fid,fname=FN[fid],side=side,note=note,sid=u['sid']))
if fails:
    for x in fails: print('FAIL',x)
    sys.exit(1)
# duplicates (same slug+sentence flagged twice)
dup=Counter((r['slug'],r['sid']) for r in out)
d2=[k for k,v in dup.items() if v>1]
with open('flags.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['slug','quote','fid','fname','side','note'])
    w.writeheader()
    for r in out: w.writerow({k:r[k] for k in ['slug','quote','fid','fname','side','note']})
# re-verify from the written file
n=0
for r in csv.DictReader(open('flags.csv',encoding='utf-8')):
    assert r['quote'] in snap[r['slug']]; n+=1
print('flags written:',len(out),'| re-verified quotes in snapshot:',n)
print('match method:',dict(method))
print('same-sentence multiple flags:',d2)
# coverage
with open('coverage.tsv','w') as f:
    f.write('slug\tunits_total\tunits_read\tparas\ttable_rows\tflags\n')
    fc=Counter(r['slug'] for r in out)
    T=[0,0]
    for s in slugs:
        us=units[s]; p=sum(u['kind']=='para' for u in us); t=len(us)-p
        f.write(f'{s}\t{len(us)}\t{len(us)}\t{p}\t{t}\t{fc[s]}\n'); T[0]+=len(us)
    f.write(f'TOTAL\t{T[0]}\t{T[0]}\t\t\t{len(out)}\n')
print('coverage units:',T[0])
