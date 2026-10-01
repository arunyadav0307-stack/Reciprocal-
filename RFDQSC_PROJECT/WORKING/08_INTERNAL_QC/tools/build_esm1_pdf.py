#!/usr/bin/env python3
"""Build ESM_1.pdf with PyMuPDF (no TeX engine is available). Content mirrors 02_MANUSCRIPT/supplementary/ESM_1.tex.
usage (from WORKING/): python3 08_INTERNAL_QC/tools/build_esm1_pdf.py"""
import pymupdf, os
OUT="02_MANUSCRIPT/supplementary/ESM_1.pdf"
def tbl(head,rows,widths=None):
    s='<table><tr>'+''.join(f'<th>{h}</th>' for h in head)+'</tr>'
    for r in rows: s+='<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>'
    return s+'</table>'
H='''
<h1>Supplementary information (ESM_1)</h1>
<p class="c"><b>Reciprocal-free divisors of prescribed order over finite fields and the saturation cost of cyclic quantum synchronizable codes</b></p>
<p class="c">[INSERT AUTHOR NAMES] — Corresponding author: [INSERT NAME, E-MAIL]<br/>Journal of Applied Mathematics and Computing</p>
<p>This file contains the proof of Lemma 2.3, the Class 2 observations of Sect. 11.4 and the table of computational checks of Sect. 12.3 of the main article. Section, lemma and theorem numbers refer to the main article. “Li–Zhu” denotes Z. Li and S. Zhu, Int. J. Theor. Phys. 61, 251 (2022). The Python code is provided as ESM_2.zip.</p>

<h2>S1. Proof of Lemma 2.3</h2>
<p><b>Lemma 2.3 (dual containment).</b> Let gcd(N,q) = 1, and let C be a cyclic code of length N over F<sub>q</sub> with generator polynomial g<sub>C</sub>. Then</p>
<p class="c">C<sup>⟂</sup> ⊆ C ⟺ g<sub>C</sub>(x) g<sub>C</sub><sup>*</sup>(x) | x<sup>N</sup> − 1.</p>
<p><b>Proof.</b> Write R<sub>N</sub> = F<sub>q</sub>[x]/(x<sup>N</sup> − 1) and x<sup>N</sup> − 1 = g<sub>C</sub> h<sub>C</sub>.</p>
<p><i>Step 1 (orthogonality as a polynomial condition).</i> For u, v ∈ R<sub>N</sub> put v̄(x) = Σ<sub>j</sub> v<sub>j</sub> x<sup>−j</sup> ∈ R<sub>N</sub>. The coefficient of x<sup>s</sup> in u(x) v̄(x) is Σ<sub>j</sub> u<sub>j+s</sub> v<sub>j</sub>, with indices modulo N. This is the inner product of v with the s-th cyclic shift of u. Since C is spanned by the cyclic shifts of g<sub>C</sub>,</p>
<p class="c">v ∈ C<sup>⟂</sup> ⟺ g<sub>C</sub>(x) v̄(x) = 0 in R<sub>N</sub>.</p>
<p><i>Step 2 (identification of C<sup>⟂</sup>).</i> Now g<sub>C</sub> v̄ = 0 in R<sub>N</sub> if and only if h<sub>C</sub> divides v̄ (as an element of R<sub>N</sub>). The map v ↦ v̄ is the ring automorphism of R<sub>N</sub> induced by x ↦ x<sup>−1</sup>. It carries ⟨h<sub>C</sub>⟩ onto ⟨h<sub>C</sub>(x<sup>−1</sup>)⟩ = ⟨h<sub>C</sub><sup>*</sup>⟩, because x<sup>deg h<sub>C</sub></sup> is a unit of R<sub>N</sub>. Hence C<sup>⟂</sup> = ⟨h<sub>C</sub><sup>*</sup>⟩.</p>
<p><i>Step 3 (comparison of ideals).</i> Since h<sub>C</sub><sup>*</sup> is a monic divisor of x<sup>N</sup> − 1, the inclusion C<sup>⟂</sup> ⊆ C holds if and only if g<sub>C</sub> | h<sub>C</sub><sup>*</sup>. Taking reciprocals, this is equivalent to g<sub>C</sub><sup>*</sup> | h<sub>C</sub>, and that is equivalent to g<sub>C</sub> g<sub>C</sub><sup>*</sup> | g<sub>C</sub> h<sub>C</sub> = x<sup>N</sup> − 1. ∎</p>

<h2>S2. Class 2 computational observations (Sect. 11.4)</h2>
<p>For the BCH class of Li–Zhu one has n = (q<sup>2m</sup> − 1)/(q − 1) and N = 2n. The observations below use an index rule reconstructed from</p>
<ul><li>the defining-set truncations printed in Example 3 of Li–Zhu;</li><li>the ranges 1 ≤ i ≤ δ − 2 and 1 ≤ j ≤ δ<sup>*</sup> − 2;</li><li>the upper limits for δ and δ<sup>*</sup> stated by Li–Zhu.</li></ul>
<p>“Saturated” means ord(h) = N under this reconstruction.</p>
'''+tbl(["(q, m)","N","ord<sub>N</sub>(q) = w<sub>0</sub> = w","tuples","saturated","ord(h) &lt; N","range of s (saturated)"],
 [["(3, 2)","80","4","75","75","0","8–24"],["(5, 2)","312","4","1,490","1,482","8","6–66"],["(7, 2)","800","4","10,269","10,263","6","8–124"],["(3, 3)","728","6","19,908","19,896","12","12–144"]])+'''
<p>In every saturated tuple observed, s &gt; w. These are computational observations under a reconstructed rule; they are not a theorem and they do not cover Class 2 exhaustively. The tuples with ord(h) &lt; N may be excluded by the exact hypotheses of Li–Zhu. The observed minimum s = 6 for (q, m) = (5, 2) is below 2w = 8, so the bound s ≥ 2w of Theorem 11.1 is not claimed for Class 2.</p>

<h2>S3. Computational checks (Sect. 12.3)</h2>
<p>The values w and w<sub>0</sub> were computed by a dynamic programme over the lcm-cover form (Proposition 4.2) and cross-checked against an independent brute force that enumerates sets of q-cyclotomic cosets directly, without using Proposition 4.2. The support-reduction enumerator for Theorem A allows distinct blocks to share a support, as in Sect. 6.6, where 45 and 75 both have support {3,5}.</p>
'''+tbl(["Check","Range (finite)","Checks","Failures"],[
 ["DP vs. independent coset brute force","15 values of q (even and odd), N &lt; 200","1,999","0"],
 ["Lemma 5.1","all prime powers q &lt; 128; odd m &lt; 5000","99,981","0"],
 ["Theorem A","all prime powers q &lt; 128; odd N &lt; 2000","39,968","0"],
 ["Formula (6.3) for w<sub>0</sub>","as for Theorem A","39,968","0"],
 ["Theorem B","all prime powers q &lt; 128; odd two-prime N &lt; 20000","195,405","0"],
 ["Theorem C(i)","all prime powers q &lt; 128; odd primes p &lt; r &lt; 400","30,079","0"],
 ["Theorem C(ii)","explicit triples (p, r, q) with p, r &lt; 400","594","0"],
 ["Theorem 11.1(i) and the factor-degree structure","odd q &lt; 128; primes n &lt; 400","1,081","0"],
 ["<b>Total</b>","","<b>409,075</b>","<b>0</b>"]])+'''
<p>The ranges include adversarial cases: repeated prime powers; three and four distinct primes; mixed 2-adic classes; blocks requiring helper primes; supports used by more than one block; and even q for Lemma 5.1 and Theorems A and B. The record is not an exhaustive verification over all inputs.</p>
<p><i>Instances from Li–Zhu.</i> Generator degrees, ord(h), dual containment and the exact d(D) were computed directly for the three examples. In Example 3 the factor m<sub>0</sub> = x − 1 printed in g<sub>1</sub> and g<sub>3</sub> is incompatible with dual containment and with the printed dimensions; the computations omit it (Sect. 11.3).</p>

<h2>S4. Code</h2>
<p>The Python scripts are provided as ESM_2.zip; see its README.</p>
'''
CSS='''
body{font-family:serif;font-size:10.5pt;line-height:1.35}
h1{font-size:15pt;text-align:center;margin-bottom:6pt}
h2{font-size:12pt;margin-top:14pt;margin-bottom:4pt}
p{margin:0 0 6pt 0;text-align:justify}
p.c{text-align:center}
table{border-collapse:collapse;width:100%;margin:6pt 0 8pt 0;font-size:9pt}
th{border-top:1px solid black;border-bottom:1px solid black;padding:2pt 3pt;text-align:left}
td{padding:2pt 3pt;border-bottom:0.3px solid #888}
ul{margin:0 0 6pt 14pt}
'''
FONTCSS='''
@font-face{font-family:serif;src:url(DejaVuSerif.ttf)}
@font-face{font-family:serif;font-weight:bold;src:url(DejaVuSerif-Bold.ttf)}
'''
arch=pymupdf.Archive("/usr/share/fonts/truetype/dejavu")
story=pymupdf.Story(html=H,user_css=FONTCSS+CSS,archive=arch)
W,Hh=pymupdf.paper_size("a4")
mb=pymupdf.Rect(60,60,W-60,Hh-60)
doc=pymupdf.DocumentWriter(OUT)
more=1;n=0
while more:
    dev=doc.begin_page(pymupdf.Rect(0,0,W,Hh)); more,_=story.place(mb); story.draw(dev); doc.end_page(); n+=1
doc.close()
d=pymupdf.open(OUT)
d.set_metadata({"title":"Supplementary information (ESM_1)","author":"[INSERT AUTHOR NAMES]","creator":"PyMuPDF (source: ESM_1.tex)"})
d.saveIncr()
print("pages",len(d))
