# PROJECT STATE — checkpoint after PHASE 00

## Project
- Title: *Reciprocal-free divisors of prescribed order over finite fields and the saturation cost of cyclic quantum synchronizable codes*
- Authors: **not supplied** (placeholders; AD-001)
- Target journal: Journal of Applied Mathematics and Computing (Springer), Springer Nature `sn-jnl` template, numbered references (`sn-mathphys-num`)
- Article type: original research article (pure mathematics: finite fields / algebraic coding, with a calibration of a published quantum-synchronizable-code construction)
- Current manuscript version: **v0 = BASELINE (unchanged)** — `02_MANUSCRIPT/RFDQSC_WORKING.tex` is identical to the supplied source
- Paper short name for file naming: `RFDQSC`
- Project mode: **M3 (full package; mathematics + Python code; no figures, no datasets)**

## Evidence
- Available: .tex (authoritative), compiled PDF (28 pp, derivative), .bib (25 entries, authoritative; 25/25 cited), sn-jnl.cls, sn-mathphys-num.bst, ESM_1.pdf, ESM_2.zip (= 17 Python scripts), verification summary, cover letter, checklist, metadata, declarations docx.
- Unavailable: previous final baseline; journal's original guidelines; the cited source papers (Li & Zhu 2022 [A]; Fujiwara–Tonchev–Wong 2013) — to be fetched from public literature in Phase 1; any dataset (none exists).
- Authoritative: manuscript = .tex; bibliography = `03_References_JAMC.bib`; code authority by function (g4_audit.py → 409,075-check claim; g2_*/g3_* → Thm A/B/C, Table 1, Class 2; audit_* → earlier toolkit, partly unrelated).
- Code status: executable (Python 3.11 + sympy + numpy). `g4_audit.py` launched in the background at Phase 0 to test reproducibility of the check counts; result will be recorded in Phase 6.
- Data status: none.
- Environment risk: **no LaTeX engine in the sandbox**; apt/CTAN/conda unreachable. Final compilation (Phase 14) needs a workaround (e.g. npm `texlive` pdfTeX-WASM tree) or author-side compilation. Recorded, not hidden.

## Phase status
See `COMPLETED_PHASES.txt`. PHASE 00–13 — COMPLETE; PHASE 14 — NOT STARTED.

## Major scientific findings (established only)
- Quoted worked values w/w0 for (143,3), (55,3), (225,23), (35,3), (5,3), (26,3), (82,37), (80,3) and w(2,q)=∞ reproduced by an independent definition-level coset search.
- Table 1 deficit arithmetic (22/74/74; 10/54/56; Δ = 12/20/18; splits 6+6, 10+10, 8+10) is internally consistent.
- Headline check count 409,075 equals the sum of the eight ESM_1 rows; Class 2 totals 31,742 / 31,716 equal the sum of the ESM_1 rows. (Arithmetic only; reproduction by running code is pending, Phase 6.)
- Phase 2: all lemmas, propositions and theorems re-derived; no mathematical error found; independent finite spot checks (Theorems A, B, C, 11.1(i)) agree with 0 mismatches. Theorem 11.1 remains conditional on [A]'s hypotheses (AD-004).
- Phase 3: no boundary failure (1,332 (q,N) cases, 234 even-N cases, 850 saturated pairs enumerated for N=2n). The authors' g4_audit.py was run to completion: 8 rows, total 409,075 checks, 0 failures (reproduced).
- Phase 4: exact integer arithmetic, deterministic (two identical runs). Table 1 and the Class 2 (ESM S2) tables reproduced by the authors' scripts. Hygiene: g2_test.py runs legacy tests at import (prints the 7 failures); README omits numpy; dead code; label mismatch.
- Phase 5: 29 quoted values traced, 0 mismatches; curated code package (04_CODE/curated) reproduces the originals' results; CODE_MAP.md added.
- Phase 6: V&V statement written (verification vs validation separated); reproducibility record and evidence hashes; ledger has no open reproduction/proof items (open: V061 citation; AD-004 rows; AD-003 rows).
- Phase 7: Table 1 fully re-verified; caption/cross-reference/width repaired; no figures needed.
- Phase 8: claims-vs-evidence table complete; workflow traces and defensive scope text removed; abstract made precise.

## Corrections made
Phase 1: FTW/XYY16/LM18 attribution (binary vs q-ary); search-trace phrasing replaced by hedged priority statement; gap sentence added; 'primary result' label removed. Phase 2: attainment of w added in §9.2. See CHANGELOG.

## Unresolved issues (routed)
Pandoc-conversion damage in the .tex (stars/emphasis, subscripts, no \label/\ref); internal-workflow wording in the paper (enumerator bug story, "literature search performed for this work", "Online Resource", "printed inconsistencies"); reconstructed Class-2 rule; source check of [A] Example 3 and FTW hypotheses; audit_* naming and unrelated scripts in the public code; placeholders.

## Author decisions
AD-001 (metadata/declarations) PENDING · AD-002 (code/data availability) PENDING · AD-003 (Class 2 retention) PENDING · AD-004 (access to [A]) PENDING · AD-005 (optional MathSciNet check) PENDING.

## Current authoritative manuscript
`02_MANUSCRIPT/RFDQSC_WORKING.tex` (= baseline v0) with `03_REFERENCES/RFDQSC_references.bib`.

## Next action
`NEXT PHASE: PHASE 14` — assemble final package; no TeX engine: deliver .tex/.bib/cls/bst/ESM and state clearly that the PDF must be compiled author-side.
