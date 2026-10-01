# RESUME INSTRUCTIONS

This project has completed **Phase 0** (intake, evidence map, baseline freeze, initial value ledger).

Do NOT repeat completed phases unless later evidence reveals a contradiction.

Read, in order:
1. `00_STATE/PROJECT_STATE.md`
2. `00_STATE/CURRENT_PHASE.txt`
3. `00_STATE/COMPLETED_PHASES.txt`
4. `00_STATE/CHECKPOINT_MANIFEST.md` (verify SHA-256 of files)
5. `06_VALUE_LEDGER/VALUE_LEDGER.csv`
6. `08_INTERNAL_QC/CHANGELOG.md`
7. `08_INTERNAL_QC/AUTHOR_DECISIONS.md`
8. all files in `07_PHASE_REPORTS/` (currently `PHASE_00_INTAKE.md`)

Then begin **Phase 01 — Research problem, literature gap and novelty**, following the master prompt (phased Q1 SCI manuscript audit/repair/finalisation).

Working rules carried forward
- Manuscript under repair: `02_MANUSCRIPT/RFDQSC_WORKING.tex`; bibliography `03_REFERENCES/RFDQSC_references.bib`. Never edit `01_BASELINE/`.
- Ledger and changelog are cumulative: append/update, never restart.
- Never invent results, references, DOIs, authors, metadata. Record author-only items in `AUTHOR_DECISIONS.md`.
- Keep internal workflow language out of the manuscript.
- Build the next checkpoint with `python3 08_INTERNAL_QC/tools/make_checkpoint.py <phase>` (run from `RFDQSC_PROJECT/`, i.e. the parent of `WORKING/`: `python3 WORKING/08_INTERNAL_QC/tools/make_checkpoint.py 1`; it regenerates the manifest and verifies the zip).
- Environment: Python 3.11 + sympy + numpy available; no LaTeX engine (see PROJECT_STATE.md).
- Mathematical context: w(N,q) = least degree of a reciprocal-free divisor h of x^N−1 of order N; w0 = classical version; support-reduction Theorem A (odd N), two-prime-power Theorem B, separation Theorem C, QSC application Props 9.1/10.1, Cor 9.2, calibration Thm 11.1 + Table 1.
