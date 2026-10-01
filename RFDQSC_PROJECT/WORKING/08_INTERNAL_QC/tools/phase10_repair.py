#!/usr/bin/env python3
"""Phase 10: typesetting repair of the Pandoc-damaged manuscript source (idempotence not guaranteed: run once).
Run from WORKING/. Every manual replacement asserts that its target occurs exactly once."""
import re
P="02_MANUSCRIPT/RFDQSC_WORKING.tex"
t=open(P,encoding="utf-8").read()

def rep(old,new,count=1):
    global t
    assert t.count(old)==count,(t.count(old),old[:80])
    t=t.replace(old,new)

def rep_block(start,end,new):
    """replace text from `start` through the first `end` after it (end included)"""
    global t
    assert t.count(start)==1,start[:60]
    i=t.index(start); j=t.index(end,i)+len(end)
    t=t[:i]+new+t[j:]

def rep_line(prefix,new):
    global t
    lines=t.split("\n")
    idx=[k for k,l in enumerate(lines) if l.startswith(prefix)]
    assert len(idx)==1,(len(idx),prefix[:60])
    lines[idx[0]]=new
    t="\n".join(lines)

# ---- preamble ----
rep("\\usepackage{booktabs,longtable,array,calc}","\\usepackage{booktabs,array}")
rep("\\def\\LTcaptype{none}\n","")
rep("\\newunicodechar{Σ}{\\ensuremath{\\Sigma}}","\\newunicodechar{Σ}{\\ensuremath{\\sum}}")

# ---- §2.2 reciprocal paragraph (emphasis damage) ----
rep_line("For \\(f\\) ∈ \\(F_q[x]\\) with \\(f\\)(0) ≠ 0, the \\emph{(monic) reciprocal}",
r"For \(f\) ∈ \(F_q[x]\) with \(f\)(0) ≠ 0, the \emph{(monic) reciprocal} is \(f^{*}(x)=f(0)^{-1}x^{\deg f}f(1/x)\). Its roots are the inverses of the roots of \(f\), with multiplicities; \(f\mapsto f^{*}\) preserves degree and irreducibility, \((fg)^{*}=f^{*}g^{*}\), and \(\operatorname{ord}(f^{*})=\operatorname{ord}(f)\). We call \(f\) \emph{self-reciprocal} if \(f^{*}=f\). Since \((x^N-1)^{*}=x^N-1\), the reciprocal of a divisor of \(x^N-1\) is again such a divisor.")

# ---- Lemma 2.3: statement only inside the environment; consequence moved out ----
rep_block("\\begin{thmx}{Lemma 2.3 (dual containment)}","\\end{thmx}",
r"""\begin{thmx}{Lemma 2.3 (dual containment)}

Let gcd(\(N\),\(q\)) = 1, and let \(C\) be a cyclic code of length \(N\) with generator polynomial \(g_C\). Then

\[C^{\perp}\subseteq C \iff g_C(x)\,g_C^{*}(x)\mid x^N-1.\]

\end{thmx}

The criterion is standard; for completeness, a proof (via the identification \(C^{\perp}=\langle h_C^{*}\rangle\), where \(h_C=(x^N-1)/g_C\)) is given in the supplementary information (S1).

\textbf{Remark after Lemma 2.3.} The semisimple hypothesis matters for the consequence we need. If gcd(\(N\),\(q\)) = 1, then \(x^N-1\) is squarefree, so \(g_Cg_C^{*}\mid x^N-1\) forces \(\gcd(g_C,g_C^{*})=1\). Every divisor \(h\) of \(g_C\) then also satisfies \(\gcd(h,h^{*})=1\), because \(hh^{*}\) divides \(g_Cg_C^{*}\). Without the semisimple hypothesis this implication can fail.""")

# ---- Prop 3.1: clean enumerate, explanatory text outside the statement ----
i=t.index("\\begin{thmx}{Proposition 3.1"); j=t.index("\\end{thmx}",i)+len("\\end{thmx}")
blk=t[i:j]
m_a=re.search(r"\\textbf\{lcm-cover form:\}(.*?)\n  \\end\{enumerate\}",blk,re.S); assert m_a
m_b=re.search(r"\\item\n  \\textbf\{Partition form:\}(.*?)\n\\end\{enumerate\}\n\n(Part \(a\).*?)\n\n\\end\{thmx\}",blk,re.S); assert m_b
item_a=m_a.group(1).strip(); item_b=m_b.group(1).strip(); after=m_b.group(2).strip()
new31=("\\begin{thmx}{Proposition 3.1 (classical forms of \\(w\\)₀)}\n\nLet gcd(\\(N\\),\\(q\\)) = 1 and \\(N\\) ≥ 2.\n\n"
"\\begin{enumerate}\n\\def\\labelenumi{(\\alph{enumi})}\n\\tightlist\n"
"\\item \\textbf{lcm-cover form:} "+item_a+"\n"
"\\item \\textbf{Partition form:} "+item_b+"\n\\end{enumerate}\n\n\\end{thmx}\n\n"+after)
t=t[:i]+new31+t[j:]

# ---- §3.1 matrix proof ----
rep("GL\\_\\{deg \\(h\\)\\}(\\(q\\))",r"\(\mathrm{GL}_{\deg h}(q)\)")

# ---- partitions, (6.2), (6.3), S = {m_1..m_s} ----
rep("\\{A\\_1, \\ldots, A\\_\\(s\\)\\}",r"\(\{A_1,\ldots,A_s\}\)",2)
rep_line("\\begin{center}\\(w\\)(\\(N\\),\\(q\\)) = min\\_\\{",
r"\[w(N,q)=\min_{\{A_1,\ldots,A_s\}\ \text{partition of }P}\ \sum_{j=1}^{s}c(A_j),\qquad (6.2)\]")
rep_line("\\begin{center}\\(w\\)₀(\\(N\\),\\(q\\)) = min\\_\\{",
r"\[w_0(N,q)=\min_{\{A_1,\ldots,A_s\}\ \text{partition of }P}\ \sum_{j=1}^{s}o(n_{A_j}).\qquad (6.3)\]")
rep("Let \\(S\\) = \\{\\(m\\)\\emph{1, \\ldots, \\(m\\)}\\(s\\)\\} be the underlying set.",r"Let \(S=\{m_1,\ldots,m_s\}\) be the underlying set.")
rep("Let \\(S\\) = \\{\\(m\\)\\emph{1, \\ldots, \\(m\\)}\\(r\\)\\}, viewed as a set.",r"Let \(S=\{m_1,\ldots,m_r\}\), viewed as a set.") if t.count("\\{\\(m\\)\\emph{1, \\ldots, \\(m\\)}\\(r\\)\\}")==1 else None

# ---- Prop 9.1 proof ----
rep_line("\\(h\\) divides \\(g_C\\), which divides \\(x^N\\) − 1. By Lemma 2.3",
r"\(h\) divides \(g_C\), which divides \(x^N-1\). By Lemma 2.3, \(g_Cg_C^{*}\) divides \(x^N-1\). Since gcd(\(N\),\(q\)) = 1, \(x^N-1\) is squarefree, so \(\gcd(g_C,g_C^{*})=1\). As \(h\mid g_C\) and \(h^{*}\mid g_C\), this gives \(\gcd(h,h^{*})=1\). Together with \(\operatorname{ord}(h)=N\), \(h\) is feasible for \(w\)(\(N\),\(q\)), and the inequality follows from Definition 4.1.")

# ---- Theorem B table -> numbered booktabs table ----
rep_block("{\\def\\LTcaptype{none} % do not increment counter","\\end{longtable}\n}",
r"""\begin{table}[ht]
\caption{Values of $w_0(N,q)$ and $w(N,q)$ for $N=p^ar^b$ (Theorem B); notation as in the setting above.}\label{tabB}
\centering\small
\begin{tabular}{@{}llll@{}}
\toprule
Case & Condition & $w(N,q)$ & $w_0(N,q)$\\
\midrule
I & $t_p=t_r\ge 1$ & $\infty$ & $\min(L,\,o_p+o_r)$\\
II & $t_p=t_r=0$ & $\min(L,\,o_p+o_r)$ & $\min(L,\,o_p+o_r)$\\
III & $t_p=0,\ t_r\ge 1$ & $\min\bigl(L,\,o_p+\operatorname{lcm}(o_{p0},o_r)\bigr)$ & $\min(L,\,o_p+o_r)$\\
IV & $t_p,t_r\ge 1,\ t_p\ne t_r$ & $\min\bigl(L,\,\operatorname{lcm}(o_p,o_{r0})+\operatorname{lcm}(o_{p0},o_r)\bigr)$ & $\min(L,\,o_p+o_r)$\\
\bottomrule
\end{tabular}
\end{table}""")
rep("\\(w\\)(\\(N\\),\\(q\\)) is given by the table above.","\\(w\\)(\\(N\\),\\(q\\)) is given by Table~\\ref{tabB}.")

# ---- §11.3 prose around Table (calibration) ----
rep_line("Table~\\ref{tab1} lists computed values.",
r"Table~\ref{tab1} lists the computed values for the three examples of \cite{LZ22}. Here \(d\)(\(D\)) is the exact classical minimum distance of the cyclic code \(D\) with generator \(g_D=g_3g_4\), computed by parity-check rank; the values printed in \cite{LZ22} are lower bounds. For Example 3 we use the factor lists of \cite{LZ22} without the factor \(m_0=x-1\), which is self-reciprocal and therefore incompatible with dual containment; with this reading, the dimensions \([40,32]\) and \([40,36]\) and \(h=m_4m_5\) given in \cite{LZ22} are reproduced. Examples 1 and 2 belong to Class 1. Example 3 belongs to the BCH class (Class 2) of \cite{LZ22}, so its values come from direct computation, not from Theorem 11.1.")
rep_line("In Table~\\ref{tab1}, \\(w\\)₀ = \\(w\\)",
r"In Table~\ref{tab1}, \(w_0=w=\operatorname{ord}_N(q)\), \(N+2-2w=22,74,74\) and \(K+2d(D)=10,54,56\) for Examples 1--3.")

# ---- fragment-level typography ----
OPS=["ord","lcm","gcd","min","max","deg","supp","dim"]
def fix_frag(m):
    f=m.group(1)
    f=f.replace("^{*}","\0")        # protect existing
    f=f.replace("*","^{*}").replace("\0","^{*}")
    f=re.sub(r"(?<![\\A-Za-z])("+"|".join(OPS)+r")(?![A-Za-z])",r"\\operatorname{\1}",f)
    f=re.sub(r"(?<![\\A-Za-z])GL(?![A-Za-z])",r"\\mathrm{GL}",f)
    return "\\("+f+"\\)"
body_start=t.index("\\begin{document}")
head,body=t[:body_start],t[body_start:]
# star directly after a fragment: \(h\)*  ->  \(h^{*}\)
body=re.sub(r"\\\)\*",r"^{*}\\)",body)
body=re.sub(r"\\\((.*?)\\\)",fix_frag,body,flags=re.S)
t=head+body
open(P,"w",encoding="utf-8").write(t)
print("done")
