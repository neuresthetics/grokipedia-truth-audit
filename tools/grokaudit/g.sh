#!/bin/bash
# usage: g.sh N 'regex' [context_chars]
f=$(printf "${CACHE:-out/cache}/ref%03d.txt" $1); c=${3:-220}
python3 - "$f" "$2" "$c" <<'PY'
import sys,re
f,p,c=sys.argv[1],sys.argv[2],int(sys.argv[3])
try: t=re.sub(r'\s+',' ',open(f,encoding='utf-8',errors='replace').read())
except FileNotFoundError: print('NO FILE',f); sys.exit()
ms=list(re.finditer(p,t,re.I))
print(f'-- {f.split("/")[-1]} /{p}/ {len(ms)} hits (len {len(t)})')
for m in ms[:6]: print('   …'+t[max(0,m.start()-c):m.end()+c]+'…')
PY
