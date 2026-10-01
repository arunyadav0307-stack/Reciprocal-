# PHASE 03 — Dimensional, boundary-condition and limiting-case stress test

Status: COMPLETE. No manuscript statement was found to fail at a boundary; no manuscript text was changed in this phase. Tool: `08_INTERNAL_QC/tools/phase03_boundary_check.py` (fresh code; finite spot checks only, not proofs).

## 1. Dimensional / parameter consistency (pure-mathematics analogue of "units")
- K = N − 2·deg g_C ≥ 0 always, since g_C g_C* | x^N−1 gives 2 deg g_C ≤ N. Checked on every enumerated pair (850 saturated dual-containing pairs, Part 4).
- Finite w always satisfies 2w ≤ N (compatible with K ≥ 0 for the degenerate pair g_C=h, g_D=1 of §9.2): verified for 1,332 (q,N) cases; no violation.
- Length bookkeeping: N + a_l + a_r with a_l + a_r ≤ N − 1 (saturated), so the length is at most 2N − 1; consistent with the framework statement.
- Identity (10.1) and Singleton d(D) ≤ B+1 verified numerically with exact d(D) for the instances where exhaustive minimum distance was feasible (4 pairs; the identity is algebraic and proved in Phase 2).

## 2. Boundary values (definition-level coset search vs. manuscript statements)
| Boundary | Statement checked | Cases | Result |
|---|---|---|---|
| N = 2 (q odd) | w(2,q)=∞, w0=1 | 8 q-values | agrees |
| N = 3 | w=1 if q≡1 (mod 3), ∞ if q≡2 | all q tested | agrees |
| N prime power | w0 = o(N); w = o(N) or ∞ by admissibility | all in range | agrees |
| w = 1 | iff N | q−1 (N>2), Prop 4.3(4) | 1,332 cases | agrees |
| finiteness | w<∞ iff N admissible, Prop 4.3(1) | 1,332 | agrees |
| range | w0 ≤ w, 1 ≤ w ≤ ord_N(q), w0 ≤ ord_N(q) | 1,332 | agrees |
| q even / prime-power q | q ∈ {2,4,8,16} included | in the 1,332 | agrees |
| Even N | lcm-cover form (Prop 4.2) for even N, reciprocal-free and unconstrained | 234 | agrees (supports the use of Prop 4.2/9.1 for N = 2n) |
Ranges: q ∈ {2,3,4,5,7,8,9,11,13,16,25,27}, N < 200 with ≤ 18 cyclotomic cosets.

## 3. Limiting cases of the theorems
- Theorem C(ii) lower end p=7, r=5: every prime q<400 that is a primitive root mod 7 and mod 5 gives w=12 and w0=10, as in Theorem B (iii) and the closed forms (p−1)(r−1)/2 and p+r−2. The ratio bound (p−1)/4 of Step 4 is derived only for the choice r>p made in Step 2, so it is not asserted at (p,r)=(7,5); no inconsistency.
- Remark "for p = 3 one gets w0 = r−1 = w": verified for every admissible (q,r) found (q ≡ 2 mod 3, q primitive root mod r, r ≡ 5 mod 8, r<200): w = w0 = r−1.
- Theorem 11.1 for n = 3,5,7,11,13,17 with q ∈ {3,5,7,11,13} (all primes q with the field arithmetic implemented): full enumeration of every saturated dual-containing pair (C,D): 850 pairs.
  - 532 pairs have both h1 and h2 nonconstant: all satisfy s ≥ 2w and w = ord_n(q) (Thm 11.1 (i),(ii)).
  - Every saturated pair has a nonconstant negacyclic part h2 (ord(h) = 2n forces it), as used in the proof.
  - 318 pairs have h1 constant; **246 of them have s < 2w** (s = w is possible). So the hypothesis "both nonconstant" (taken from [A]) is essential to s ≥ 2w. The theorem already states it; the Class 1 remark in §11.2 ("Source of the factor 2") is consistent. Whether [A] indeed imposes it cannot be checked (AD-004).
  - Theorem 11.1(iii) checked with exact d(D) on the 4 instances small enough for exhaustive minimum distance (Δ ≥ 2w, identity (10.1)); coverage is small and is not a verification of (iii), which is proved.

## 4. Reproduction of the computational record (early result, formalised in Phase 6)
The background run of the authors' `g4_audit.py` completed (221 s) with the eight rows of counts 1,999; 99,981; 39,968; 39,968; 195,405; 30,079; 594; 1,081 (sum 409,075) and 0 failures each. Output saved as `08_INTERNAL_QC/evidence/g4_audit_output_run1.txt`. Labels in the script ("Lemma 1", "Theorem 2") differ from manuscript numbering (Lemma 5.1, Theorem 11.1): a Phase 5 reconciliation item.

## 5. Conclusions and routing
- No boundary failure; no manuscript change.
- Phase 5: script/manuscript label mapping. Phase 6: formal record of the run (hardware/runtime/versions) and the fact that the ledger now holds a reproduced value.
- Phase 8/10: optional one-sentence remark that without a nonconstant h1 one has only s ≥ w (supported by Part 4). Not needed for correctness; to be decided with AD-004.
