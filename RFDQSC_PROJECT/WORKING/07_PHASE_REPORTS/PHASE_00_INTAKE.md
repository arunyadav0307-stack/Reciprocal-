# PHASE 00 — INTAKE, EVIDENCE MAPPING & BASELINE FREEZE

Date: 2026-10-01 · Branch `arena/01a0f4ec-reciprocal` · Repository commit at intake `218c794`

## 1. What was supplied

The repository contains `README.md` ("Research Paper") and one archive:
`Reciprocal free divisors of prescribed order over finite fields and the saturation cost of cyclic quantum synchronizable codes.zip`
(SHA-256 `be428312…f1ea`). It unpacks to a Springer Nature / JAMC submission package (`JAMC_Submission_Package/`).

| # | Item | Path inside package | Role | Status |
|---|------|--------------------|------|--------|
| 1 | Manuscript source | `02_Main_Manuscript_JAMC.tex` (971 lines, 86 215 B) | **authoritative manuscript** | present |
| 2 | Manuscript PDF | `01_Main_Manuscript_JAMC.pdf` (28 pp) | compiled output of #1 (checked: abstract, page count, all non-reference numerals agree with #1) | present, derivative |
| 3 | Bibliography | `03_References_JAMC.bib` (25 entries, all with DOI) | **authoritative .bib**; 25 cited keys = 25 bib keys, none missing, none uncited | present |
| 4 | Class / style | `sn-jnl.cls`, `sn-mathphys-num.bst` | required for build | present |
| 5 | Figures | `04_Figures/NO_FIGURES.txt` | none exist | n/a |
| 6 | Supplementary text | `05_Supplementary_Material/ESM_1.pdf` (3 pp: proof of Lemma 2.3, Class 2 table, verification record) | authoritative for Lemma 2.3 proof and ESM counts | present |
| 7 | Supplementary code | `05_Supplementary_Material/ESM_2.zip` = `06_Computational_Verification/scripts/*` + README (byte-identical scripts, checked) | code | present |
| 8 | Verification summary | `06_Computational_Verification/VERIFICATION_SUMMARY.txt` | claim: 409,075 checks, 0 failures | present, claim only |
| 9 | Cover letter, checklist, metadata, declarations docx, README | `07…11_*` | submission administration (placeholders) | present, not part of the paper |
| 10 | Experimental / numerical data | — | the paper has no datasets; all "data" are outputs of the scripts | **none** |
| 11 | Previous final baseline / earlier versions | — | none supplied (checklist mentions earlier 34-pp and 41-pp builds, not supplied) | **unavailable** |
| 12 | Journal instructions | — | only the checklist's paraphrase; original guidelines not supplied | **unavailable** |
| 13 | Source of cited construction [A] (Li & Zhu 2022) and FTW 2013 | — | not supplied; needed for Table 1 / Sect. 9–11 | **unavailable (to be fetched in Phase 1, public literature)** |

## 2. Project mode

**M3 — FULL PACKAGE (mathematics + code variant).** Source (.tex/.bib/.cls/.bst), compiled PDF, executable Python code (Python 3.11, sympy 1.14, numpy) all present. There are no figures, no experimental data, no mesh/time-step/PDE items (pure number-theoretic / algebraic-coding paper). Consequently phases dealing with BC/IC, mesh, time step, tolerance, stiffness and code↔figure reconciliation are re-interpreted as:
- Phase 3 (stress test): hypotheses/limiting cases of the number-theoretic statements (small q, N, degenerate supports, even q, N of either parity), not physical dimensional analysis;
- Phase 4 (numerical): exactness/integer arithmetic, enumerator completeness, range coverage of finite checks (there is no floating-point numerics except none);
- Phase 5/6: scripts ↔ Lemma/Theorem statements ↔ Table 1 / ESM tables.
M4 (delta) does not apply: no prior final baseline.

## 3. Authoritative-source decisions

- **Manuscript:** `02_Main_Manuscript_JAMC.tex` → copied to `02_MANUSCRIPT/RFDQSC_WORKING.tex`. The PDF is not edited; it is regenerated at Phase 14.
- **Bibliography:** `03_References_JAMC.bib` → `03_REFERENCES/RFDQSC_references.bib`.
- **Code:** `g4_audit.py` is the only script that produces the counts claimed in ESM_1 §S3 (409,075); `g2_*`, `g3_*`, `g1_compare.py` support Theorems A/B/C, Table 1 and Class 2; the `audit_*.py` family (`audit_lib/dist/run…run7`) is an earlier review toolkit whose content partly concerns other statements (e.g. `audit_run5.py` refers to items "R2, R3, R7, R9, Appendix A" that do not occur in this manuscript). Authority is therefore **by function, not by file name** (Phase 5 will classify each script).
- **Data:** none.
- **Figures:** none.
- **Baseline:** frozen unchanged in `01_BASELINE/JAMC_Submission_Package` with per-file SHA-256 (`BASELINE_SHA256.txt`).

## 4. Environment

- Python 3.11 + sympy 1.14 + numpy installed → scripts executable.
- **No LaTeX engine** (`xelatex`, `pdflatex`, `latexmk`, `tectonic` absent). `apt` mirrors, CTAN, conda and GitHub release-asset hosts are unreachable from the sandbox; only PyPI, npm and github.com web/API are reachable. Consequence: a faithful compile with the Springer class is **not yet possible**; a fallback (npm `texlive` pdfTeX-WASM tree) is an option to evaluate before Phase 10; the final compile requirement of Phase 14 is at risk and is recorded as an environment blocker, not hidden.
- Background run of `g4_audit.py` started to test whether the 409,075 count is reproducible (results will be entered in Phase 6; not claimed here).

## 5. Intake observations (not yet repaired; routed to later phases)

Science / structure
1. The paper is a pure-mathematics result set (Lemma 5.1, Theorems A, B, C(i)(ii), Props 9.1/10.1, Cor 9.2, Thm 11.1) with a one-table "calibration" of a published QSC construction [A]. Proofs are the primary evidence; computations are a stress test. (Phases 2–3)
2. Class 2 of [A] is treated under a *reconstructed* index rule ("only partially legible in the available source"). This is weak evidence and mixes uncertain reading of a source with the paper's claims. (Phase 8 decision; see AD-003.)
3. Example 3 of [A] is said to print a self-reciprocal factor m0 = x−1 in g1,g3, which the manuscript corrects silently in its computation. Needs comparison with the published paper. (Phase 1/9)
4. Framework statements (2.2), (2.3) are attributed to FTW 2013; the exact hypotheses of FTW (which polynomial's order bounds tolerance; role of D) must be checked against the original. (Phase 1/2)
5. Novelty language: "no invariant equivalent to w(N,q) was identified in the literature search performed for this work" appears in abstract, §1.3, §12.4 and the cover letter. Needs a real, documented search (Phase 1) and rewording (Phase 8/11).

Workflow traces inside the manuscript (must be removed/rephrased in Phases 8, 10, 11)
6. §12.3 narrates an enumerator bug ("7 spurious failures"), §11.1 says printed inconsistencies "are recorded explicitly rather than corrected silently", abstract states "stress-tested in 409,075 computational checks", ESM names `audit_*` scripts, text says "Online Resource", "the available source", "verification record", "the literature search performed for this work", "defensive scope paragraphs" (§1.5, §12.1, §12.4).

LaTeX / source quality (Phase 9/10/14)
7. The .tex is a Pandoc-style conversion: reciprocal stars consumed by emphasis markup (e.g. §2.2 "f\emph{(x)=… f}", Lemma 2.3 text, Prop 9.1 proof, §6.4 "m\emph{1,…,m}s"), broken subscripts `GL\_\{deg h\}`, `\{A\_1,…\}`, `min\_\{…\}`, display equations as `center`+inline math with manual "(5.1)" tags and no `\label/\ref`, theorem numbers hard-coded in titles, ~50 `\newunicodechar` hacks, plain-text tables in §6–7.
8. Table 1 caption uses literal "[A]" instead of `\cite`.
9. Scripts and README expose internal naming (`audit_*`, `g1…g4`), and contain material unrelated to this paper.

Administrative (not scientific)
10. All author/affiliation/funding/competing-interest/AI-use/contribution fields are placeholders. They are not invented (AD-001).

## 6. Completion gate (Phase 0)

- [x] evidence map exists (§1)
- [x] authoritative sources identified (§3)
- [x] baseline frozen (`01_BASELINE`, SHA-256 manifest)
- [x] VALUE_LEDGER created (`06_VALUE_LEDGER/VALUE_LEDGER.csv`, 61 rows; worked examples and Table 1 arithmetic recomputed; claims otherwise tagged PENDING)
- [x] missing evidence identified (§1 rows 10–13, §4)
- [x] project state written (`00_STATE/`)
- [x] checkpoint created (`CHECKPOINTS/RFDQSC_CHECKPOINT_PHASE_00.zip`)

Phase 0 recomputation tool: `08_INTERNAL_QC/tools/phase00_ledger_check.py` (definition-level coset search; all 14 quoted w / w0 values reproduced; Table 1 Δ values and the 409,075 and 31,742 / 31,716 sums reproduced arithmetically).
