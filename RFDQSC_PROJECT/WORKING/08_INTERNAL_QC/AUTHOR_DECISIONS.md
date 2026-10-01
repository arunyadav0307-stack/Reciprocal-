# AUTHOR DECISIONS (cumulative)

Status values: PENDING / RESOLVED.

## AD-001 — Author, affiliation and declaration metadata · PENDING
1. Issue: all author names, affiliations, e-mail, ORCID, funding, competing interests, author contributions, acknowledgements and the AI-tool-use statement are placeholders.
2. Location: .tex title block and "Statements and Declarations"; files 07, 08.
3. Why it matters: mandatory for submission to JAMC / Springer Nature; cannot be invented.
4. Evidence: placeholders in package.
5. Options: author supplies the data (no scientific impact; independent work continues).
6. Information required: full names, affiliations, corresponding author, funding statement, competing-interest statement, contributions, truthful AI-use statement.

## AD-002 — Code / data availability wording and repository · PENDING
1. Issue: Code is provided only as a supplementary zip; no public repository link. Data availability says "reproducible with Online Resource 2 [AUTHOR TO CONFIRM]".
2. Location: Statements and Declarations; file 08.
3. Why: journal policy; also decides whether the scripts are released publicly (and under which curated names, see Phase 5).
4. Options: (a) supplementary zip only; (b) public repository (e.g. the existing GitHub repo or a Zenodo deposit).
5. Required: author choice and URL/DOI if (b).

## AD-003 — Retention of the "Class 2" computational observations · PENDING (decision expected at Phase 8; default: move out of the main text unless evidence improves)
1. Issue: §11.4 / ESM_1 §S2 rest on a *reconstructed* index rule for Li–Zhu Class 2 ("only partially legible in the available source").
2. Why: results derived from an uncertain reading of a source can mislead; not needed for any theorem.
3. Evidence: ESM_1 S2; `g3_class.py`.
4. Options: keep as clearly labelled observation; move entirely to supplementary; delete. If the published paper [A] can be obtained and the rule confirmed (Phase 1), the issue may be resolved without the author.
5. Required: author preference only if [A] cannot be checked.

Update (Phase 5): a curated code package is prepared in `04_CODE/curated/` (identical results). The author's choice in AD-002 now only concerns where it is released and whether the earlier exploratory scripts are shipped.

(No other decision is currently open. New entries will be appended; resolved entries are marked RESOLVED with the resolution.)

## AD-004 — Access to Li–Zhu (2022) [A] · PENDING
1. Issue: [A] is paywalled; its hypotheses (are h1 and h2 both nonconstant?), Example 3 printed `m0`, and printed d(D) values (3, 4, 3 vs recomputed exact 4, 6, 4) cannot be confirmed.
2. Location: §11 (Theorem 11.1, Table 1 discussion), ESM_1.
3. Why: any statement that [A] "misprints" something, and the scope of Theorem 11.1, depend on the source.
4. Options: (a) author supplies the PDF; (b) author confirms the statements; (c) default: soften/remove misprint assertions and keep Theorem 11.1 explicitly conditional on [A]'s hypotheses (decided in Phases 8/10).
5. Required: PDF or confirmation.

## AD-005 — Optional MathSciNet novelty check · PENDING (low priority)
1. Issue: Novelty of w(N,q) rests on web, zbMATH Open and arXiv searches; MathSciNet/Scopus not accessible.
2. Why: the manuscript says only "to our knowledge"; a database check by the author would support this.
3. Options: author runs a search (e.g. "order of a polynomial" + "reciprocal"/"self-reciprocal", "minimal degree" + "prescribed order") or accepts the hedged wording.
