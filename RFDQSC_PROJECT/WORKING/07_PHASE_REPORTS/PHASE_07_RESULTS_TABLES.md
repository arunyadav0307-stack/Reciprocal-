# PHASE 07 — Results, figures, tables and interpretation

Status: COMPLETE. The manuscript contains no figures and one numbered table (Table 1), plus the unnumbered case table of Theorem B (in the statement). No figure is added: the results are theorems and exact formulas, and a decorative plot would add no evidence (minimum-intervention rule).

## 1. Table 1 audit
- Every entry recomputed/reproduced (Phases 4–5): w0=w=3,5,4; B=6,10,8; s=6,10,8; K=2,42,48; exact d(D)=4,6,4; Δ=12,20,18; 2(s−w)=6,10,8; 2(B+1−d(D))=6,10,10. Row sums: Δ = 2(s−w)+2(B+1−d(D)) holds in each row; N+2−2w=22,74,74 and K+2d(D)=10,54,56 agree with the text.
- Column "d(D) [A]" (3,4,3) reproduces what the authors read from [A]; not verifiable here (AD-004).
- Issues found and fixed:
  1. Caption said "computed values" although one column is quoted from [A]. Now: all entries computed except the column d(D) [A], with citation.
  2. Table was never referred to by number before it appeared and the text used a literal "Table 1". Now `Table~\ref{tab1}` before and after.
  3. The literal "[A]" in caption and header replaced by `\cite{A}`.
  4. Twelve columns at \small may exceed the text width of sn-jnl and cannot be checked without compilation: wrapped in `\resizebox` that only shrinks when wider than \textwidth. Re-check at Phase 14 once a compile is possible.
- "What the table shows": claims checked against the numbers: s=2w in all three (equality case of Thm 11.1(ii) for Examples 1–2 only, correctly stated); Δ ≥ 2w for Examples 1–2; strict because d(D)<B+1; "roughly equal" split 6+6, 10+10, 8+10. Correct.

## 2. Theorem B case table
Checked against the proof and the code (`wB`): entries correct; the table sits inside the theorem statement as an unnumbered longtable, which is acceptable; its prose reference "the table above" is clear.

## 3. Other quantitative statements in the text
Examples in §1.3, §4.4, §6.6, §7.4 traced (Phase 5). Counts in §11.4/§12.3 reproduced (Phase 4–5). No quantity is reported without a computation or derivation.

## 4. Interpretation control
- Claims limited to proved statements; the manuscript explicitly disclaims general optimality of the QSC bound and any fixed-q statement. No overstatement found in the results sections.
- Open: the sentence "the exact classical distances d(D) exceed the lower bounds printed in [A]" (§11.3 and conclusions) depends on AD-004; to be softened or kept in Phases 8/10 per the author's answer.

## 5. Figures
None exist; none required. Figure files are not part of the package (matches `NO_FIGURES.txt`). Final package will have no figure folder.
