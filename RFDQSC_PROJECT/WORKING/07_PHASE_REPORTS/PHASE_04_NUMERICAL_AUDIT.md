# PHASE 04 — Numerical method and computational reliability

Status: COMPLETE. The study is exact-arithmetic number theory (no floating-point quantity enters any result). No numerical defect was found in the code that produces the manuscript's numbers; code-hygiene items are routed to Phase 5/6.

## 1. Arithmetic and representation
- All quantities are Python integers (arbitrary precision): multiplicative orders by repeated modular multiplication, lcm by `//gcd`, polynomial arithmetic over Z/q (q prime) with exact integer coefficients, exact minimum distance by parity-check column dependence (`mindist_H`, `dcyc` using cyclic symmetry to fix coordinate 0). No tolerances, no floats in any reported value (floats appear only in printed ratios in `g2_test3.py`; the manuscript's ratios are not taken from them).
- Prime-power q: orders are computed from the integer q (correct). Polynomial computations (Table 1, Class 2) use prime q only (3, 37, 5, 7), so Z/q is a field.
- Determinism: no random generator is used (the `random` import in `g2_test.py` is unused). `g4_audit.py` was run twice (221 s, 233 s): outputs identical.

## 2. Algorithm review
| Routine | Review |
|---|---|
| `mo`, `adm` | `adm` scans q^0..q^(o−1) for −1, returns False for m<3: matches the definition of admissible divisor |
| `wdp` (DP over lcm-states, each divisor at most once) | exact; justified by the set form in Prop 4.2 |
| `wcoset` (brute force over cyclotomic cosets) | independent of Prop 4.2; excludes self-reciprocal cosets and reciprocal pairs; skips cases with >22 candidate cosets: 198 of 2,197 (q,N) pairs skipped, 1,999 tested (91%) |
| `wA`, `w0A`, `wB` | direct transcriptions of (6.2), (6.3) and the Theorem B table; same formulas as the manuscript (no helper beyond exponent 1) |
| `mindist_H`, `dcyc` | smallest number of linearly dependent parity-check columns = minimum distance; exact; exponential in distance but small here (N ≤ 82) |
| Theorem C(ii) instance search | q produced by CRT then stepping by pr until prime: preserves q ≡ primitive roots mod p and r; `mo` checks confirm |
| Class 2 enumeration (`g3_class.py`) | follows the reconstructed index rule (AD-003); its counts depend on that rule |

Independence caveat: the Theorem A/B/C rows of `g4_audit.py` compare the DP (which relies on Prop 4.2) with the closed forms; independence from Prop 4.2 is provided only by the 1,999 coset brute-force cases. Phases 2–3 added fresh independent definition-level checks (1,342 + 1,332 + 234 cases; Phase 2/3 reports).

## 3. Reproduction runs (authors' scripts, unmodified, copies in /tmp, outputs in 08_INTERNAL_QC/evidence)
- `g4_audit.py`: eight rows 1,999 / 99,981 / 39,968 / 39,968 / 195,405 / 30,079 / 594 / 1,081 (sum 409,075), 0 failures; twice.
- `g3_calib.py` (Table 1): dD = 4, 6, 4 for Examples 1–3; K = 2, 42, 48; Δ = 12, 20, 18; N+2−2w = 22, 74, 74; K+2dD = 10, 54, 56; dual containment True; ord(h)=N; for Example 3 with the printed m0 included: dual containment False (dD=5, A=17, B=9). **Table 1 reproduced.** (The printed values from [A] are not reproducible from here: AD-004.)
- `g3_class.py` (Class 2): tuples 75 / 1,490 / 10,269 / 19,908 (total 31,742); ord(h)<N in 0 / 8 / 6 / 12; minimum s = 8 / 6 / 8 / 12; s-ranges 8–24, 6–66, 8–124, 12–144. **ESM S2 table reproduced** (under the reconstructed rule).
- Class 1 check in the same script: 134 instances, 0 violations of w(2n,q) = ord_n(q) = ord_{2n}(q).

## 4. Findings routed
1. `g2_test.py` contains the legacy support-reduction enumerator and runs its tests at import. Importing it from `g3_calib.py`, `g3_class.py`, `g2_test3.py` re-executes ~2 minutes of tests and prints the 7 "T2 FAIL" lines (the manuscript's "7 spurious failures", caused by the legacy enumerator allowing each support once). The numbers are correctly explained in the manuscript, but a released package must not run this at import. → Phase 5/6 (curated code copy; originals untouched; AD-002).
2. README requirements omit numpy (imported by audit_run*.py and audit_dist.py). → Phase 5/9.
3. Dead code in `g3_calib.py` (`selfdual`, `Cd="-"`). → Phase 5.
4. Script labels ("Lemma 1", "Theorem 2", "Thm2/Thm3") do not match manuscript numbering. → Phase 5 mapping table.
5. Scope: all computations are finite ranges; the manuscript already says so (§12.3). No claim is made beyond them.

## 5. Manuscript changes this phase
None.
