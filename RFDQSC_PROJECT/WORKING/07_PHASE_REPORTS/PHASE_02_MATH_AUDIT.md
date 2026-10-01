# PHASE 02 — Mathematical audit

Status: COMPLETE. Every lemma, proposition and theorem of the manuscript was re-derived line by line from its statement; no mathematical error was found in the claimed results. One precision gap was repaired, and several items that are not mathematical errors were routed. The independent script `08_INTERNAL_QC/tools/phase02_math_check.py` is a finite spot check (not exhaustive verification).

## 1. Statement-by-statement verdicts
| Item | Verdict | Notes |
|---|---|---|
| (2.1), Lemma 2.1 (lcm law) | CORRECT | ord = multiplicative order of x in F_q[x]/(f) |
| §2.2 factorisation, deg M_C = o(m), ord(M_C)=m | CORRECT | standard (Lidl–Niederreiter) |
| Lemma 2.2 (self-reciprocal ⇔ −1∈⟨q⟩) | CORRECT | edge m=1,2 handled |
| Lemma 2.3 (dual containment), incl. g_C=1 and C={0} | CORRECT | proof in ESM_1 S1 sound; holds without gcd(N,q)=1, only the consequence needs it. ESM_1 PDF has conversion damage in Step 3 (reciprocal stars eaten; reads "g_C | h_C" twice) → routed |
| Lemma 2.4 (Singleton), Cor 9.2 use for D≠{0} | CORRECT | C^⊥⊆C⊊D forces C≠{0} |
| Prop 3.1(a),(b) | CORRECT | (b) holds for every N (assign each prime to a carrier) |
| Prop 4.2 (lcm-cover) | CORRECT | m=1,2 are inadmissible, consistent with definition |
| Prop 4.3(1)–(4); w(2,q)=∞ | CORRECT | reduction direction (mod divisor) is the right one |
| Lemma 5.1 (2-adic criterion), Steps 1–5 | CORRECT | uses (1+pu)^{p^{a−1}}≡1; cyclicity of (Z/p^a)^×; no parity assumption on q |
| Cor 5.2, "shrinking" consequence | CORRECT | needs odd m≥3 |
| Theorem A, both directions, coinciding blocks | CORRECT | the "Clarification" argument is valid (strict (6.5) would give w<F, contradicting F≤w) |
| (6.3) | CORRECT | |
| §6.6 example (225,23): 32 and 26 | CORRECT | o(3)=2,o(5)=4,o(9)=6,o(25)=20 recomputed |
| Theorem B, Cases I–IV and symmetric case | CORRECT | single prime support with t≥1 is inadmissible; helper logic right |
| §7.4 examples (i)–(iv) | CORRECT | |
| Theorem C(i) | CORRECT | |
| Theorem C(ii) first part | CORRECT | gcd(2u,4v)=2 uses u odd; (p−3)(r−3)≥4 holds for p≥7, r≥5 |
| Theorem C(ii) second part, Steps 1–4 | CORRECT | Step 2's r>p is attainable (Dirichlet, infinitely many); ratio ≥ (p−1)/4 |
| Prop 9.1 | CORRECT | |
| Cor 9.2, Prop 10.1 identity | CORRECT | algebra rechecked |
| §11.1 (u+v|u−v) ↔ cyclic generator g1·g2 | CORRECT | CRT decomposition; dual of composite is C1^⊥⊕C2^⊥; so dual containment splits |
| Theorem 11.1 (i)–(iii) | CORRECT given its stated hypotheses | hypothesis "ord(h)=2n" is automatic once h2 is nonconstant (h2 | Φ_{2n}); harmless |
| Table 1 arithmetic | CORRECT | K=N−2(B+s), N+2−2w, K+2d, Δ and splits recomputed |
| Class 2 table (ESM S2) | arithmetic CORRECT | 75+1490+10269+19908=31742; 31716 saturated; N=2n and ord_N(q) values recomputed; rule is reconstructed (AD-003) |

## 2. Repairs made (manuscript)
1. Prop 9.1 "Consequences": the statement that w is "the least possible degree of a saturating factor" was a bound only. Added the (proved) attainment: take g_C = h optimal, g_D = 1 (then hh* | x^N−1, Lemma 2.3); the pair is degenerate (d(D)=1) and says nothing about quantum capability.

## 3. Independent computation (tools/phase02_math_check.py, fresh code)
- Definition-level search over cyclotomic cosets (reciprocal-free and unconstrained), odd N<400, q ∈ {2,3,4,5,7,8,9,11,13}, #cosets ≤ 18: 1,342 cases; compared with Theorem A and (6.3): 0 mismatches.
- Theorem B table vs definition level: 567 cases, 0 mismatches. Theorem B vs Theorem A formula: 6,952 cases (odd N<3000, ten q), 0 mismatches.
- Theorem C(ii) closed forms: 1,122 triples (p,r,q) with p,r<120, q prime<400, 0 mismatches (definition-level check where #cosets ≤ 18).
- Theorem 11.1(i), N=2n, definition level: 129 cases, w=w0=ord_n(q), 0 mismatches.
Scope: finite spot check only.

## 4. Items routed (not math errors)
- Phase 8/10: statements about [A] (printed values, Example 3 `m0`, "lower bounds from the component distance formula") rest on an unreadable source (AD-004). Statements about [B]: only "repeated-root cyclic/constacyclic" is confirmed (IEEE Xplore abstract); the specific "N = 12 p^s" and "powers of self-reciprocal factors" claims are not verified → soften to verified wording in Phase 10.
- Phase 10/11/14: Pandoc damage (reciprocal stars as emphasis in §2.2, Lemma 2.3 text, Prop 9.1 proof, §6.4 "m\emph{1,…,m}s"; GL\_\{deg h\}; \{A\_1,…\}; min\_\{…\}); the same damage in ESM_1 S1 Step 3. ESM_1 has no source file in the package, so it must be re-typeset from corrected text.
- Phase 6: reproduction of the 409,075-check record (g4_audit.py still running/unknown in sandbox).
- Phase 3: boundary cases (N=2, N prime power, q even, w=1, w=∞, N=3), and the lower end of Theorem C(ii) (p=7, r=5).
