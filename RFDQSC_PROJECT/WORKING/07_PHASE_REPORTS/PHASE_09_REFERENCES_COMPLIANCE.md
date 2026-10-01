# PHASE 09 — References and journal compliance

Status: COMPLETE.

## 1. Reference verification
All 25 bibliography entries were checked against Crossref in one filter query (25 of 25 DOIs returned). Authors, titles, journal, volume, issue, pages or article number, and year match for every entry; no bib field was changed. Lidl–Niederreiter: Crossref gives 1996-10-24 and zbMATH gives 1996, so 1996 stays (V061 closed; the copyright year of the print edition cannot be confirmed independently). Journal titles already follow LTWA-style abbreviations.

Cited keys and bib keys are the same 25 keys. The reference list holds published works only.

## 2. Corrections
| Item | Action |
|---|---|
| Keys `A`, `B` | Renamed `LZ22`, `DMLHW20` in the bib and in every `\cite` (including `\cite{A,B}`) |
| `\bibliography{03_References_JAMC}` | Now `\bibliography{RFDQSC_references}`, the working bib name; the final name is set in Phase 14 |
| Header comment "Compile with XeLaTeX or LuaLaTeX …" | Replaced by a neutral build sequence; no engine is available here, so no compile claim is made |
| Zhang–Ge arXiv:1508.00974 | Stays an in-text mention (the author's checklist, item 13: the list takes only published or accepted works); no entry added |

## 3. Compliance check (against the author's checklist, no journal rules invented)
| Item | State |
|---|---|
| Abstract 150–250 words | 229 words (math counted as one word); no citations in it |
| Keywords 4–6 | 6 |
| MSC | 11T06 (primary), 11T71, 94B15, 81P70, 11A07 |
| Numbered citations, `sn-mathphys-num` | in place |
| Statements and Declarations before the references | present; contents are placeholders (AD-001) |
| Supplementary information | wording is "supplementary information (ESM_1/ESM_2)" |
| Flat upload | to be assembled in Phase 14 (tex, bib, cls, bst, PDF) |
| Title page fields | placeholders (AD-001) |

## 4. Carried forward
- `\newunicodechar` hacks (about 50) and Pandoc damage: Phases 10/11/14. Page count and Table 1 width: Phase 14, when a compile is possible.
- The supplied cover letter repeats wording the manuscript no longer uses; it is re-issued in Phase 14 (AD-006).
- ESM_2 is to be the curated code package (AD-006).
