# REVIEWER Q&A — Phase 12 (adversarial review)

Each entry: likely hostile question, evidence-based answer, and what (if anything) changed in the paper.

| # | Question | Answer | Paper |
|---|---|---|---|
| 1 | Is w(N,q) more than a relabelled lcm-cover problem? | It is the same finite optimization with an admissibility constraint; the contribution is the constraint's exact arithmetic (Lemma 5.1, Theorem A helpers, Theorem B), and its use as a saturation-cost bound. The paper does not claim more; Lemma 5.1 and Prop 3.1 are labelled as known in substance. | none |
| 2 | Theorem C needs q chosen after (p,r); is the separation vacuous? | It is unbounded over pairs (N,q), stated as such; fixed-q behavior is explicitly not claimed (Sect. 8.3 remark, §1.5, §12.1, open directions). | none |
| 3 | Theorem 11.1 depends on a paper (Li–Zhu) whose full text was unavailable to the audit. | Theorem 11.1 is now stated for the algebraic structure only (g_C = g1g2, g_D = g3g4, g3 | g1 | x^n−1, g4 | g2 | x^n+1, C dual-containing, h1 and h2 nonconstant, ord(h) = 2n). The proof uses only these, Lemma 2.3 and Lemma 2.1; it does not use any other property of Li–Zhu. Its application to Li–Zhu's codes rests on their codes having this structure (AD-004). | hypothesis of Thm 11.1 made explicit (Phase 12) |
| 4 | Is s ≥ 2w a defect of Li–Zhu or an artifact of the template? | It reflects the requirement of nontrivial factors on both sides; the paper says it is a property of the construction, not a statement about code quality; without nonconstant h1 only s ≥ w holds (246 of 318 constant-h1 saturated pairs have s < 2w; Phase 3). | none |
| 5 | Is (9.1) anything beyond Singleton? | No; it is stated as an elementary consequence (Sect. 9.4, 10.3). The value is the cost term w that depends only on (N,q). | none |
| 6 | Tolerance a_l + a_r < ord(h) is quoted, not derived. | It is the cited framework (FTW binary; XYY16, LM18 q-ary), verified against FTW Lemma 3 and LML19 Theorem 1; the paper uses only (2.2) and (2.3). | none |
| 7 | Quantum error-correction capability is not addressed. | Correct and stated: w does not determine K, d(D) or quantum distances. | none |
| 8 | Computational evidence: independent or circular? | Two independent routes (dynamic programme vs coset brute force, 1,999 cases) plus theorem-level checks; all counts reproduced (Phase 6). Presented as complement to proofs, "not exhaustive". | none |
| 9 | Even N and three or more primes are excluded. | Theorem A is for odd N (cyclicity of (ℤ/2^a)^× fails); listed in open directions. Computations include 3 and 4 primes, even q. | none |
| 10 | Class 2 rests on a reconstructed rule. | Said so in §11.4 and ESM_1 S2; no theorem claimed; AD-003. | none |
| 11 | [LZ22]'s printed d(D) values differ from the exact ones. | Table 2 shows both columns; the paper does not assert a misprint (AD-004). | none |
| 12 | Novelty search limited to open databases. | Wording is "not aware of earlier work"; AD-005 offers MathSciNet check. | none |
