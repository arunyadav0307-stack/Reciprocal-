# PHASE 06 — Verification, validation and reproducibility

Status: COMPLETE. The value ledger now has no open code-reproduction or proof-audit item. Open items are source-access (AD-004), reconstructed Class 2 rule (AD-003) and the Phase 9 citation check (V061).

## 1. Verification (is the mathematics/code right?)
| Layer | Method | Strength | Outcome |
|---|---|---|---|
| Proofs | Line-by-line re-derivation of all lemmas, propositions, theorems (Phase 2) | proof-level for the stated hypotheses | no error found |
| Independent computation | Fresh definition-level coset search (Phases 2, 3): 1,342 + 567 (Thm B) + 1,332 + 234 (even N) cases; Theorem C(ii) 1,122 triples; N=2n enumeration of 850 saturated pairs | finite spot checks | 0 mismatches |
| Authors' check record | `g4_audit.py` run twice, curated `verify_theorems.py` once | finite-range, partly dependent on Prop 4.2 (only 1,999 cases independent of it) | 409,075 checks, 0 failures; identical across runs |
| Example computations | `g3_calib.py` (Table 1), `g3_class.py` (Class 2) | exact | reproduced |
| Code↔paper | `phase05_trace.py` | exact | 29/29 values |
A finite check is not a proof, and the manuscript says so; none of the statements in the paper relies on a computation for its proof.

## 2. Validation (does it agree with the outside world?)
- This is a pure-mathematics paper with no experimental or observational data: there is nothing to validate against measurements, and none is claimed.
- External agreement obtained: the cyclic QSC framework (2.2)–(2.3) against FTW (binary) and Luo–Ma–Lin Theorem 1 (q-ary, citing XYY16, LM18); Class 1 tolerance logic against Luo–Ma–Lin Theorem 2; existence of classical interpretations of w0 (least period of a linear recurrence; GL_k(q) element orders) by derivation.
- Not validated: values printed in Li–Zhu [A] (their d(D), Example 3 factor list, hypotheses) because the paper is not accessible (AD-004). The Table 1 columns "d(D) [A]" and the statement about the printed `m0` therefore remain reported as the authors' reading of [A].
- Class 2: observations are reproduced, but the index rule is reconstructed (AD-003); they do not validate [A].

## 3. Reproducibility record
- Environment: Python 3.11.2, sympy 1.14.0 (numpy 2.4.6 installed but not required by the curated code). See `08_INTERNAL_QC/evidence/ENVIRONMENT.txt`.
- Determinism: no RNG; two full runs identical.
- Run times: `verify_theorems.py` ≈ 4 min; `calibrate_examples.py` ≈ 2 min (Table 1 exact distances for N=80 dominate); `class2_observations.py` ≈ 2 min; total ≈ 8 minutes on one core.
- Commands: `cd 04_CODE/curated && python3 verify_theorems.py && python3 calibrate_examples.py && python3 class2_observations.py`.
- Archived outputs with SHA-256: `08_INTERNAL_QC/evidence/*.txt`, `EVIDENCE_SHA256.txt`.
- Inputs: all parameters are in the scripts; there is no external data and no data folder (05_DATA intentionally absent).

## 4. Statement wording for the manuscript (for Phases 8/10)
- Computational scope sentence (state once, in the body, not as a process narrative): "The statements of Lemma 5.1, Theorems A, B and C and Theorem 11.1(i) were also checked by exact computation over finite ranges (prime powers q<128 and the N-ranges listed in the supplement); these checks complement the proofs and are not part of them."
- Data availability: no datasets were generated or analysed; code location depends on AD-002.
- Replace "7 spurious failures" / "Online Resource" process language by the above (Phase 8/10).

## 5. Manuscript changes this phase
None (wording prepared above, applied in Phases 8/10).

## 6. Ledger status after Phase 6
All proof-audit and script-reproduction rows closed; open: V061 (citation, Ph9); AD-004-linked rows V042, V066; reconstructed-rule rows V043–V048 flagged.
