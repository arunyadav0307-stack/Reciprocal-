# PHASE 14 — Compile and deliver

Status: COMPLETE WITH ONE BLOCKER — the manuscript PDF was not compiled.

## Blocker
No TeX engine is available in the working environment (no pdflatex/xelatex/lualatex/tectonic; apt, CTAN, conda and TeX Live mirrors are unreachable; PyPI and npm offer no TeX distribution; the npm `texlive` package fetches its tree from a remote server). Therefore `RFDQSC_FINAL.pdf` does not exist, and nothing in this package claims a compile. Substitute checks run: `tools/tex_lint.py` (0 errors), cross-reference scan (Phase 13), citation/bib key equality (25 = 25).

Author action: compile `RFDQSC_FINAL.tex` (latex or xelatex → bibtex → twice more; for example on Overleaf with the supplied `sn-jnl.cls`, `sn-mathphys-num.bst`) and check: page count (28-page limit in the author's checklist), width of Table 2 (`\resizebox`), reference list, and the unicode mappings.

## Delivered (`09_OUTPUTS/`, copied to `RFDQSC_PROJECT/FINAL/`)
- `RFDQSC_FINAL.tex`, `RFDQSC_FINAL.bib` (`\bibliography{RFDQSC_FINAL}`)
- `ESM_1.pdf` (built with PyMuPDF; source `ESM_1.tex`), `ESM_2.zip` (curated code; `calibrate_examples.py` rerun from the unzipped package reproduces Table 2)
- `COVER_LETTER.txt`, `SUBMISSION_README.txt`
- `RFDQSC_FINAL_SUBMISSION_PACKAGE.zip`: flat; tex, bib, cls, bst, ESM_1.pdf/tex, ESM_2.zip, cover letter, README; contains no internal QC files, workflow terms or tool names (grep-checked).
- `RFDQSC_FINAL_CHECKPOINT.zip`: complete history (= checkpoint 14).

## Open author items
AD-001 (names, affiliations, declarations, AI-use statement), AD-002 (code location), AD-003/004 (Class 2 rule; access to Li–Zhu), AD-005 (optional MathSciNet check), AD-006 (ESM_2 choice and cover letter).
