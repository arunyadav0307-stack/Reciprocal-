# PHASE 05 — Code ↔ equation ↔ parameter ↔ result reconciliation

Status: COMPLETE. Every number quoted in the manuscript text that is computable is traced to a computation; no discrepancy between code, equation and manuscript was found. The code-side defects found in Phase 4 are fixed in a curated copy; the original scripts are untouched.

## 1. Equation ↔ code
- Prop 4.2: `wdp` (DP over lcm states, each divisor once, admissible divisors only for w; all divisors >1 for w0). Matches the set formulation.
- Lemma 5.1: `adm` (direct definition) compared with `admsupp` (2-adic criterion on prime supports).
- Theorem A (6.2), (6.3): `wA`, `w0A` enumerate set partitions of the prime support (sympy `multiset_partitions`), block cost = min over helper subsets of the other primes at exponent 1 with admissible support; same objects as §6.1.
- Theorem B: `wB` reproduces the table (Cases I–IV and symmetric case), including exponent-1 helpers.
- Theorem C(ii): instance search uses CRT + stepping by pr to a prime (Dirichlet); asserts o(p)=p−1, o(r)=r−1 and the closed forms.
- Theorem 11.1(i), Class 1: `ord_{2n}=ord_n`, factor degrees of Φ_n, Φ_2n all equal to o, w=w0=o.
- Table 1: B=deg g_D, s=deg h, K=N−2 deg g_C, Δ=(N+2−2w)−(K+2d(D)), d(D) exact; dual containment tested as g_C g_C* | x^N−1.
No equation is implemented differently from the manuscript. (The legacy enumerator in g2_test.py is the one exception, and the manuscript describes it correctly.)

## 2. Parameter ↔ code
q ranges (prime powers <128), N ranges (odd N<2000; two-prime odd N<20000; N<200 for the coset check), primes p,r<400, n<400 (Class 1) match ESM S3. Table 1 parameters (q,N) = (3,26),(37,82),(3,80) with the coset index lists of [A] as coded in `g3_calib.py` (taken from the authors' reading of [A]; AD-004). Class 2 parameters (q,m) = (3,2),(5,2),(7,2),(3,3) with n=(q^{2m}−1)/(q−1).

## 3. Result ↔ manuscript (traced by `08_INTERNAL_QC/tools/phase05_trace.py`: 29 quoted values, 0 mismatches)
w and w0 for (143,3), (55,3), (225,23), (35,3), (5,3); w(2,q)=∞; o-values for q=23 and q=3; t-classes; Table 1 w, ord_N and N+2−2w; Class 2 N and ord_N; totals 31,742/31,716 and 409,075; Theorem C(ii) smallest triple. Table 1 remaining entries (B,s,K,d(D),Δ) and the Class 2 distributions were reproduced by the authors' scripts in Phase 4.

## 4. Fixes (code package; originals unchanged)
Curated package `04_CODE/curated/` (rfd_core.py, poly_tools.py, verify_theorems.py, calibrate_examples.py, class2_observations.py, README.md, requirements.txt):
- no import-time execution of legacy tests (the 7 "T2 FAIL" lines and a 2-minute rerun no longer occur when a library is imported);
- labels use the manuscript numbering (Lemma 5.1, Theorem 11.1);
- dead code removed; numpy dependency removed; README lists requirements.
Output of the curated scripts compared with the originals: identical counts (verify_theorems: 1,999 / 99,981 / 39,968 / 39,968 / 195,405 / 30,079 / 594 / 1,081, 0 failures, 238 s; Table 1 lines identical except the removed "dC=-" placeholder; Class 2 lines identical).
`04_CODE/CODE_MAP.md` maps originals ↔ curated ↔ manuscript.

## 5. Open
- AD-002 (what is released, and where) — curated package is ready as option for the author. The non-shipped scripts (audit_run*.py, g1_compare.py, g2_test2.py) are an earlier exploratory toolkit, some unrelated to the final manuscript.
- The manuscript's "Online Resource 2" wording is a Phase 8/10 item.
