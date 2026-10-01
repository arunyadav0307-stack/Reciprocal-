# PHASE 01 — Research problem, literature gap and novelty

Status: COMPLETE (gate: gap statement evidence-based; every positioning claim traced to a source or softened; open source-access items routed to AUTHOR_DECISIONS).

## 1. Problem and gap (as now stated in the manuscript)
- Problem: for gcd(N,q)=1, determine w(N,q) = min deg h over divisors h | x^N−1 with ord(h)=N and gcd(h,h*)=1.
- Motivation chain (verified): in the cyclic QSC framework a_l+a_r < ord(h), h = g_C/g_D; maximal tolerance needs ord(h)=N; dual containment of C forces h to be reciprocal-free.
- Gap: the classical bound deg h ≥ w0(N,q) holds for every saturating factor but ignores the reciprocal-free constraint and can be far from attained (w(55,3)=20 vs w0=9; w(225,23)=32 vs w0=26; recomputed in Phase 0). No source found that defines or determines w(N,q).

## 2. Sources checked
| Source | What was verified | Effect |
|---|---|---|
| Fujiwara–Tonchev–Wong 2013 (arXiv:1304.0502, PRA 88, 012318) | Framework is **binary** ("classical codes over F_2"); Lemma 3: a_l+a_r < ord(f), f=h/g, ord(f) ≤ n | Framework (2.2)/(2.3) confirmed; attribution corrected |
| Luo–Ma–Lin 2019 (arXiv:1904.03902), Theorem 1 | q-ary version credited to Xie–Yang–Yuan 2016 and Luo–Ma 2018; tolerance maximal iff ord(f)=n | q-ary attribution added (both already in .bib) |
| Luo–Ma–Lin 2019, Theorem 2 ((u+v|u−v)) | Max tolerance 2n iff ord(g1/g3)=n and ord(g2/g4)=2 (n odd), or ord(g2/g4)=2n | Consistent with manuscript's Class 1 reading: ord(h)=lcm; ord(h2)=2 forces h2=x+1, self-reciprocal, excluded |
| Zhang–Ge arXiv:1508.00974 | Exists; title "Quantum Block and Synchronizable Codes Derived from Certain Classes of Polynomials"; duadic QSCs with highest possible tolerance | In-text description correct; add title in Phase 9 |
| Li–Zhu 2022 [A] | Abstract only (paywalled) | Hypotheses of Class 1 (h1, h2 nonconstant), Example 3 printed values, printed d(D) NOT verifiable → AD-004 |
| Prior work on w(N,q) | Web search (3 queries on minimal degree of prescribed order / LFSR minimal length / QSC max tolerance), zbMATH Open (title/class queries), arXiv abstract pages | Nothing equivalent found. MathSciNet not accessed. |

## 3. Novelty assessment (honest)
- New (to our knowledge): definition of w(N,q); Theorem A (support reduction with exponent-1 helpers); Theorem B (four-case formula); Theorem C (unbounded w/w0 with q varying); Prop 9.1/Cor 9.2/Prop 10.1 (bound and exact slack identity); Theorem 11.1 (calibration, conditional on [A]).
- Not new and labelled so in the manuscript: Lemma 5.1 (known in substance); w0 and formula (6.3) (classical); the framework (2.2)–(2.3).
- Contribution size is modest and arithmetic in nature; the QSC bound is a Singleton-type consequence. Positioning is therefore "new arithmetic invariant with exact structure + a clean structural cost in QSCs", not a new code family. The manuscript already avoids claims about achievable parameters.

## 4. Manuscript repairs made this phase (minimal; see CHANGELOG)
1. Attribution: binary framework to FTW; q-ary extension to XYY16, LM18 (§1.1, §1.6 related literature, §2.4).
2. Search-trace phrasing ("in the literature search performed for this work…", MathSciNet caveat) replaced by "We are not aware of earlier work…" / "To our knowledge…" (abstract, §1.1, §12.4).
3. Gap sentence added in §1.1 (w0 bound can be far from attained).
4. "primary result" self-label removed from Theorem A bullet.

## 5. Routed to later phases
- Phase 2: Lemma 2.3 edge cases (g_C=1, full space); Theorem A coinciding blocks; Theorem B Case III; Theorem C(ii) Step 2; dependence of Thm 11.1 on both h1,h2 nonconstant.
- Phase 8/10: wording about [A] misprints (AD-004); Class 2 (AD-003); remaining workflow phrasing (§12.1 computational verification, "Online Resource", "7 spurious failures").
- Phase 9: add Zhang–Ge title; bib keys A, B rename; LN year (1996 per zbMATH/Crossref; print date check).

## 6. Author decisions opened
AD-004 (access to Li–Zhu [A]); AD-005 (optional MathSciNet novelty check).
