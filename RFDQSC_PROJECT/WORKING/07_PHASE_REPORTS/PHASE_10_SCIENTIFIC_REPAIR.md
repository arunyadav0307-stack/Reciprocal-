# PHASE 10 — Integrated repair

Status: COMPLETE. Phases 2–6 found no mathematical or numerical error, so the repair is typographic and structural; no result, number or claim changed.

## Repairs (tex)
| Location | Defect | Repair |
|---|---|---|
| §2.2 reciprocal paragraph | emphasis ate the stars; literal braces/`\^{}` printed | rewritten: f*(x), (fg)* = f*g*, ord(f*) = ord(f), self-reciprocal |
| everywhere | `\(h\)*`, `g_C*` stars as text or binary operator | fragment-level `^{*}` (all occurrences) |
| Lemma 2.3 | consequence paragraph and the sentence "Without the semisimple hypothesis…" inside the italic lemma | statement only in the lemma; remark after it (reference in §4.1 still valid) |
| Prop 3.1 | itemize wrapping enumerate | one (a)/(b) enumerate; explanatory text after the statement |
| §3.1 | `GL\_\{deg h\}` | `\mathrm{GL}_{\deg h}(q)` |
| §6 | `{A\_1,…}`, `min\_\{…\}`, `{m\emph{1,…,m}s}` | proper math; (6.2), (6.3) as displays |
| Prop 9.1 proof | emphasis damage | rewritten |
| §7.1 | unnumbered longtable | numbered booktabs Table 1; calibration table is now Table 2 (`\ref`) |
| §11.3 | duplicated column definitions, clumsy sentence | tidied |
| preamble | longtable, calc, dead unicode hacks | removed; the 37 remaining hacks are functional and kept |

Operator names (ord, lcm, gcd, min, max, deg, supp, dim) are upright in all inline math.

## Checks
`tools/tex_lint.py`: 0 errors (environments, braces, math pairing, unicode coverage). A number-token diff against the Phase 9 source shows only the intended changes. Compilation was not possible; layout, page count and the Table 2 width are checked in Phase 14.

## Supplementary information
ESM_1 retyped (`ESM_1.tex`, `ESM_1.pdf`): S1 Step 3 restored; labels `[A]`/`[B]`, "Online Resource", "moved to meet the page limit" and the S3 enumerator narrative removed; all counts re-added (31,742 / 31,716; 409,075).

## Carried forward
Phase 11 language pass (grammar, ```` `` ' ```` quotes, a few clumsy sentences); Phase 14 compile (author-side) and ESM_2 composition (AD-006).
