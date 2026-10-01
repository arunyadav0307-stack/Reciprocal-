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
| 08 | Abstract (tex) | Class 1 result stated precisely; "stress-tested…no failures" replaced | Precision; workflow wording | Thm 11.1; g4 reproduction |
| 08 | §1.5, §12.1, §12.2, §12.3, §12.4, Conclusion (tex) | Defensive scope text shortened/positive; unverified [B] details removed; process narrative (7 spurious failures) removed; §12.4 renamed "Open directions"; priority statement kept only in §1.3 | Keep a normal research paper; evidence-supported statements only | Phase 8 report |
| 08 | §11.1, §11.3, §11.4 (tex) | "printed inconsistencies … silently" removed; claims about [A] reduced to the facts needed; Class 2 rule described neutrally | AD-004 / AD-003 defaults | — |
| 08 | whole tex | "Online Resource 1/2" → "supplementary information" | Journal terminology | — |
| 08 | VALUE_LEDGER | workflow-trace row closed; V095 added | — | — |
| 09 | bib keys (bib + tex) | `A` → `LZ22`, `B` → `DMLHW20`; all `\cite{A}`, `\cite{B}`, `\cite{A,B}` updated | Non-descriptive keys | — |
| 09 | tex `\bibliography` | `03_References_JAMC` → `RFDQSC_references` (working bib name) | Name mismatch would break bibtex | Phase 9 report |
| 09 | tex header comment | engine claim ("Compile with XeLaTeX or LuaLaTeX …") replaced by neutral build sequence | Unverified compile claim; no engine in sandbox | — |
| 09 | bib content | No change (25/25 entries match Crossref) | — | Crossref query |
| 09 | VALUE_LEDGER | V061 closed; V096–V099 added | — | — |
| 10 | tex §2.2, §2.4 (Lemma 2.3), §3.1-3.2, §6, §9.2, all | Reciprocal stars restored as `^{*}`; emphasis/brace damage repaired; operator names via `\operatorname`; Σ mapped to `\sum`; Lemma 2.3 remark moved out of the lemma; Prop 3.1 list rebuilt; (6.2),(6.3) typeset as displays | Pandoc damage | phase10_repair.py, tex_lint.py |
| 10 | tex §7.1 | Theorem B case table → numbered booktabs Table 1 (`tabB`); calibration table is now Table 2 | Journal: numbered, captioned tables | — |
| 10 | tex §11.3 | Prose before/after the calibration table tidied (duplicate definitions removed) | Redundancy | — |
| 10 | tex preamble | longtable, calc, `\LTcaptype` removed; 3 unused unicode hacks removed (δ, λ, …) | Dead code | tex_lint.py |
| 10 | supplementary | ESM_1.tex added; ESM_1.pdf rebuilt (PyMuPDF); wording and S3 narrative aligned with the paper | Consistency with Phase 8 | Phase 10 report |
| 10 | VALUE_LEDGER | V094 location updated; V100–V103 added | — | — |
| 11 | tex (spelling, §2.4, §7.3, §11.3, §11.4) | see VOICE_CHANGES.md | language | Phase 11 report |
| 11 | VALUE_LEDGER | V104 | — | — |
| 12 | tex Thm 11.1 hypotheses | "Class-1 pair of [LZ22]" → explicit structural hypotheses | Independence from unreadable source | Phase 12 report |
| 12 | REVIEWER_QA, VALUE_LEDGER V105 | added | — | — |
| 13 | VALUE_LEDGER | V106; statuses of Thm 11.1 rows reworded | Consistency with Phase 12 | Phase 13 report |
| 14 | 09_OUTPUTS | FINAL tex/bib, ESM_1/ESM_2, cover letter, submission package, README | Delivery | Phase 14 report |
| 14 | curated code | docstring/README: Table 1 → Table 2 (no computation changed) | Table renumbering | calibrate_examples rerun |
