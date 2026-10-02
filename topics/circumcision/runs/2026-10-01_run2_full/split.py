#!/usr/bin/env python3
"""Deterministic sentence splitter for the 58 snapshots (run 2).
Writes sentences.jsonl (slug, sid, kind, start, end, quote) where quote is an exact
substring of the snapshot (trailing citation markers removed), and read/<slug>.txt
reading views (citation markers stripped, for reading only)."""
import re, json, os
REPO='articles'
idx=open(f'{REPO}/INDEX_circumcision_related.md').read()
slugs=re.findall(r'^\| \d+ \| .*? \| https://\S+ \| `([^`]+)` \|',idx,re.M)
assert len(slugs)==58, len(slugs)
ABBR=set('Pte e.g i.e U.S U.K Dr St vs al approx No Fig c ca Mr Mrs Ms Jr Sr Inc Ltd Co cf Vol pp p Ch Gen Ex Lev Deut Rom Gal Col Phil Acts Matt Jn Lk Mk Gen etc Prof Rev Mt Num Josh Sam Kgs Esth Isa Jer Ezek Hos Ps Prov Eccl Mic Hab Zech Mal Heb Jas Pet Eph Thess Tim Tit Jud v Sec Art Ed Eds U.N Hon Gov Sen Rep Capt Lt Col Gen Maj Sgt Ste Ave Blvd Dept Univ Assn Inst Corp Bros Mt Ft No Nos Pt Pts B.C A.D B.C.E C.E a.m p.m Ph.D M.D'.split())
CIT=r'(?:\s*\[\d+\])*'
end_re=re.compile(r'([.!?]["”’\')\]]*)('+CIT+r')(\s+)(?=["“‘(\[]?[A-Z0-9])')
def split_para(text, base):
    out=[]; start=0
    for m in end_re.finditer(text):
        # check abbreviation before the period
        pre=text[start:m.start()+1]
        w=re.search(r'([A-Za-z.]+)\.$', pre)
        if m.group(1).startswith('.') and w:
            tok=w.group(1)
            if tok in ABBR or re.fullmatch(r'[A-Z]',tok) or re.fullmatch(r'(?:[A-Za-z]\.)+[A-Za-z]',tok):
                continue
        e=m.end(2)
        out.append((base+start, base+e)); start=m.end(3)
    if start<len(text): out.append((base+start, base+len(text)))
    return out
def strip_trailing_cit(s):
    return re.sub(r'(?:\s*\[\d+\])+\s*$','',s).rstrip()
rows=[]
for slug in slugs:
    raw=open(f'{REPO}/{slug}/snapshots/2026-10-01.txt',encoding='utf-8').read()
    hdr=raw.index('\n=====')
    body_start=raw.index('\n',hdr+1)+1
    pos=body_start; sid=0; view=[]
    for line in raw[body_start:].split('\n'):
        ls=pos; pos+=len(line)+1
        if not line.strip(): continue
        if line.startswith('#'):
            view.append(f'{line.strip()}'); continue
        kind='table' if ' | ' in line else 'para'
        spans=[(ls,ls+len(line))] if kind=='table' else split_para(line, ls)
        for a,b in spans:
            q=strip_trailing_cit(raw[a:b]).strip()
            if not q: continue
            a2=raw.index(q,a)
            assert raw[a2:a2+len(q)]==q
            sid+=1
            rows.append(dict(slug=slug,sid=sid,kind=kind,start=a2,end=a2+len(q),quote=q))
            view.append(f'{sid}{"T" if kind=="table" else ""}: '+re.sub(r'\s*\[\d+\]','',q))
    open(f'read/{slug}.txt','w').write('\n'.join(view)+'\n')
with open('sentences.jsonl','w') as f:
    for r in rows: f.write(json.dumps(r,ensure_ascii=False)+'\n')
from collections import Counter
c=Counter(r['slug'] for r in rows)
print(len(rows),'units'); print(sum(1 for r in rows if r['kind']=='para'),'sentences')
json.dump(slugs,open('slugs.json','w'))
