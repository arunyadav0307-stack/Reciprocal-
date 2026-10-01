#!/usr/bin/env python3
"""Light structural lint for the manuscript source (no TeX engine available). usage: tex_lint.py file.tex"""
import re,sys
t=open(sys.argv[1],encoding="utf-8").read()
errs=[]
# environments
stack=[]
for m in re.finditer(r"\\(begin|end)\{([^}]+)\}",t):
    k,e=m.groups()
    if k=="begin": stack.append((e,t[:m.start()].count("\n")+1))
    else:
        if not stack or stack[-1][0]!=e: errs.append(("env mismatch",e,t[:m.start()].count("\n")+1, stack[-1] if stack else None)); 
        else: stack.pop()
if stack: errs.append(("unclosed env",stack))
# inline math pairing, per line-group (paragraph)
for n,par in enumerate(t.split("\n\n")):
    if par.count("\\(")!=par.count("\\)"): errs.append(("\\( \\) count",n,par[:80]))
    if par.count("\\[")!=par.count("\\]"): errs.append(("\\[ \\] count",n,par[:80]))
    if len(re.findall(r"(?<!\\)\$",par))%2: errs.append(("$ count",n,par[:80]))
# brace balance per fragment and overall
def bal(s):
    s=re.sub(r"\\[{}]","",s); return s.count("{")-s.count("}")
if bal(t)!=0: errs.append(("global brace balance",bal(t)))
for m in re.finditer(r"\\\((.*?)\\\)",t,re.S):
    if bal(m.group(1))!=0: errs.append(("frag brace",m.group(1)[:60]))
    if "\\(" in m.group(1): errs.append(("nested",m.group(1)[:60]))
# unicode coverage
defd=set(re.findall(r"\\newunicodechar\{(.)\}",t))
body=t[t.index("\\begin{document}"):]
body=re.sub(r"\\texorpdfstring\{.*?\}\{.*?\}","",body)
bad={c for c in body if ord(c)>127 and c not in defd and c not in "§–—‘’“”"}
if bad: errs.append(("undefined unicode",sorted(bad)))
used={c for c in body if c in defd}
print("unused unicode defs:",sorted(defd-used))
for e in errs: print("ERR",e)
print("lint errors:",len(errs))
