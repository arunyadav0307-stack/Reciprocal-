# CHANGELOG (cumulative)

| Phase | Location | Change | Reason | Evidence |
|-------|----------|--------|--------|----------|
| 00 | project | Baseline frozen unchanged in `01_BASELINE/`; working copies created (`02_MANUSCRIPT/RFDQSC_WORKING.tex`, `03_REFERENCES/RFDQSC_references.bib`, `04_CODE/*`) | Phase 0 gate | SHA-256 manifest |
| 00 | manuscript | **No scientific or textual change to the manuscript** | Phase 0 is intake only | `diff` against baseline = empty |
| 01 | §1.1, §1.6, §2.4 (tex) | Binary framework attributed to FTW; q-ary extension attributed to XYY16, LM18 (keys already in .bib) | FTW is binary only; q-ary version credited to XYY16/LM18 | arXiv:1304.0502; arXiv:1904.03902 Thm 1 |
| 01 | Abstract, §1.1, §12.4 (tex) | "In the literature search performed for this work…" and MathSciNet caveat replaced by "We are not aware of earlier work…" / "To our knowledge…" | Workflow trace in a research paper; keep hedged priority statement | Phase 1 searches |
| 01 | §1.1 (tex) | Added sentence: classical bound deg h ≥ w0 can be far from attained under the reciprocal-free constraint | State the gap precisely | Examples (55,3), (225,23) recomputed in Phase 0 |
| 01 | §1.4 (tex) | Removed "primary result" self-label of Theorem A | Unneeded self-promotion | — |
| 01 | VALUE_LEDGER | Rows V062–V067 added | Literature verification | — |
| 02 | §9.2 (tex) | Added attainment of w (g_C=h, g_D=1; degenerate pair) after "least possible degree of a saturating factor" | The claim was only a bound; attainment is provable | Lemma 2.3; derivation in Phase 2 report |
| 02 | tools | Added `phase02_math_check.py` (independent definition-level checks) | Evidence for Theorems A, B, C, 11.1(i) | 0 failures on finite ranges |
| 02 | VALUE_LEDGER | Rows V068–V078 | Math audit | — |
| 03 | tools/evidence | Added `phase03_boundary_check.py`; saved `evidence/g4_audit_output_run1.txt` | Boundary stress test; reproduction of authors' check record | 0 failures; counts sum to 409,075 |
| 03 | manuscript | No change | No boundary failure found | Phase 3 report |
| 03 | VALUE_LEDGER | Rows V079–V084 | Boundary/limit evidence | — |
| 04 | evidence | Saved reproduction outputs (g4 run 2, g3_class/g3_calib) and ENVIRONMENT.txt | Numerical audit | identical to claimed values |
| 04 | manuscript/code | No change | No numerical defect; hygiene items routed to Phases 5/6 | Phase 4 report |
| 04 | VALUE_LEDGER | Rows V085–V090 | Reproduction evidence | — |
| 05 | 04_CODE/curated, CODE_MAP.md | Curated code package created (no import-time legacy tests, manuscript labels, no dead code, README/requirements); originals unchanged | Code hygiene defects from Phase 4 | outputs identical to originals |
| 05 | tools | Added `phase05_trace.py` | Trace of quoted values | 29/29 |
| 05 | manuscript | No change | No discrepancy found | Phase 5 report |
| 05 | VALUE_LEDGER | Rows V091–V093 | — | — |
| 06 | VALUE_LEDGER | Statuses of V003–V016, V029–V057 updated from PENDING to verified/reproduced; V042 split into code half (reproduced) and source half (AD-004) | Closing Phase 2–5 evidence | Phase 2–5 outputs |
| 06 | evidence | EVIDENCE_SHA256.txt added | Reproducibility record | sha256sum |
| 06 | manuscript | No change; computational-scope wording prepared for Phase 8/10 | V&V separation of verification and validation | Phase 6 report |
| 07 | Table 1 caption, header, text (tex) | Caption states which column is quoted from [A]; `\cite{A}` replaces literal "[A]"; `Table~\ref{tab1}` references added; `\resizebox` guard against overflow | Caption inaccurate ("computed values" for a quoted column); no cross-reference; 12-column width risk | Phase 4/5 reproduction; Phase 7 report |
| 07 | VALUE_LEDGER | Row V094 | — | — |
