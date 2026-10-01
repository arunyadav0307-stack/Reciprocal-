# PHASE 08 — Structure and scientific communication

Status: COMPLETE. The paper keeps its structure (13 sections, theorem-driven); the changes remove workflow traces and defensive scope text, make the abstract precise, and align every claim with its evidence.

## 1. Claims vs evidence
| Claim (location) | Evidence | Strength |
|---|---|---|
| w(N,q) defined; w ≥ w0, may be strict or ∞ (§1.3, Prop 4.3) | proof; examples; 1,332 boundary cases | proved |
| Admissibility ⇔ 2-adic classes (Lemma 5.1) | proof (Phase 2); 99,981 checks | proved; known in substance, labelled so |
| Support reduction with exponent-1 helpers (Thm A) | proof; 1,342 independent + 39,968 checks | proved |
| Exact formula N=p^a r^b (Thm B) | proof; 567 independent + 195,405 checks | proved |
| w/w0 unbounded over pairs (N,q), q varying (Thm C) | proof (Dirichlet); 1,122 triples | proved; fixed-q not claimed |
| deg h ≥ w; K+2d(D) ≤ N+2−2w; Δ identity (§9–10) | proof; Singleton | proved; elementary, stated as such |
| w attained (g_C=h, g_D=1) (§9.2, added Phase 2) | proof | proved; degenerate pair |
| Class 1 of [A]: s ≥ 2w, Δ ≥ 2w (Thm 11.1) | proof under stated hypotheses; 532 pairs | proved, conditional on [A]'s hypotheses (AD-004) |
| Table 1 values (§11.3) | reproduced exactly | computed |
| Class 2 observations (§11.4) | reproduced; rule reconstructed | observation only (AD-003) |
| Novelty of w(N,q) (§1.3) | searches, no equivalent found | hedged "not aware of earlier work" |

No claim exceeds its evidence; the abstract, §1.4 (main results) and the conclusion are mutually consistent (same six results, same scope).

## 2. Edits made
1. Abstract: last two sentences now state the Class 1 result precisely (s ≥ 2w, excess ≥ w) and replace "stress-tested … with no failures" by "agree with 409,075 exact computational checks over finite ranges".
2. §1.5 scope paragraph rewritten positively and shortened (no "we claim no …" list; pointers to §12.2).
3. §11.1: sentence "printed inconsistencies are recorded explicitly rather than corrected silently" removed (workflow wording).
4. §11.3: statements about [A] reduced to what is needed: lower-bound remark; Example 3 uses the factor lists without m0 because a factor x−1 is incompatible with dual containment; dimensions and h of [A] are reproduced with this reading. The accusation-style wording ("prints … contradicts") is removed pending AD-004.
5. §11.4: "only partially legible in the available source" replaced by the neutral description "reconstructed from Example 3 and the parameter ranges stated in [A]".
6. §12.1: duplicate disclaimers turned into one positive scope sentence. §12.2: unverified details about [B] (N = 12p^s, powers of self-reciprocal factors) removed; only the structural statement remains. §12.3: process narrative (first enumerator, 7 spurious failures) replaced by a concise computational-scope statement. §12.4 "Literature and novelty scope" replaced by "Open directions" (the priority statement is in §1.3 only).
7. Conclusion: closing disclaimer shortened.
8. "Online Resource 1/2" → "supplementary information" (ESM_1 / ESM_2) throughout, including Data/Code availability placeholders.

## 3. Decisions
- AD-003 (Class 2): default applied — kept only as a short clearly-labelled remark in §11.4 (details in the supplement); the author may delete it without affecting any theorem.
- AD-004 ([A]): wording now independent of an assertion that [A] "misprints"; Table 1 column "d(D) [A]" remains and is flagged.
- AD-001 addition: the author's AI-use statement must reflect that AI-assisted tools were used in editing/auditing this manuscript; the placeholder is left for the author.

## 4. Remaining for later phases
Pandoc-damage repair (Phase 10); ESM_1 re-typesetting incl. S3 rewrite of the process narrative (Phase 10/14); reference/journal compliance (Phase 9); language pass (Phase 11).
