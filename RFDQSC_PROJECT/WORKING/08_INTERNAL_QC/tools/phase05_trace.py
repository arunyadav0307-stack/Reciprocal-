"""Phase 5: trace every number quoted in the manuscript text to a computation with the curated core (rfd_core.py)."""
import sys, math
sys.path.insert(0, __file__.rsplit('/', 3)[0] + '/04_CODE/curated')
from rfd_core import mo, wdp, wB, v2
w = lambda N, q: wdp(N, q); w0 = lambda N, q: wdp(N, q, False)
INF = math.inf
checks = [
 # (description, computed, quoted)
 ("w(143,3)", w(143,3), 8), ("w0(143,3)", w0(143,3), 8), ("ord_143(3)", mo(3,143), 15),
 ("w(55,3)", w(55,3), 20), ("w0(55,3)", w0(55,3), 9),
 ("w(225,23)", w(225,23), 32), ("w0(225,23)", w0(225,23), 26),
 ("o(3),o(5),o(9),o(25) for q=23", (mo(23,3),mo(23,5),mo(23,9),mo(23,25)), (2,4,6,20)),
 ("o(45),o(75),o(225) q=23", (mo(23,45),mo(23,75),mo(23,225)), (12,20,60)),
 ("w(35,3)", w(35,3), 12), ("w0(35,3)", w0(35,3), 10),
 ("o(5),o(7) q=3", (mo(3,5), mo(3,7)), (4,6)),
 ("o(11),o(13) q=3", (mo(3,11), mo(3,13)), (5,3)),
 ("w(5,3) = inf; w0(5,3)=o(5)=4", (w(5,3), w0(5,3)), (INF, 4)),
 ("w(2,q)=inf for q=3,5,7", tuple(w(2,q) for q in (3,5,7)), (INF,)*3),
 ("Table1 Ex1 w=w0=ord_N, N=26,q=3", (w(26,3), w0(26,3), mo(3,26)), (3,3,3)),
 ("Table1 Ex2 N=82,q=37", (w(82,37), w0(82,37), mo(37,82)), (5,5,5)),
 ("Table1 Ex3 N=80,q=3", (w(80,3), w0(80,3), mo(3,80)), (4,4,4)),
 ("N+2-2w", tuple(N+2-2*wv for N,wv in ((26,3),(82,5),(80,4))), (22,74,74)),
 ("Class2 N, ord_N: (3,2)", (2*((3**4-1)//2), mo(3,80)), (80,4)),
 ("Class2 (5,2)", (2*((5**4-1)//4), mo(5,312)), (312,4)),
 ("Class2 (7,2)", (2*((7**4-1)//6), mo(7,800)), (800,4)),
 ("Class2 (3,3)", (2*((3**6-1)//2), mo(3,728)), (728,6)),
 ("Class2 w=w0=ord_N", tuple((w(N,q)==w0(N,q)==mo(q,N)) for q,N in ((3,80),(5,312),(7,800),(3,728))), (True,)*4),
 ("Class2 tuple totals", (75+1490+10269+19908, 75+1482+10263+19896), (31742, 31716)),
 ("check-count sum", sum((1999,99981,39968,39968,195405,30079,594,1081)), 409075),
 ("Thm C(ii) smallest triple p=7,r=5: w, w0 (q=3)", (w(35,3), w0(35,3)), (12, 10)),
 ("Thm B Case IV (35,3) formula", wB(5,1,7,1,3), 12),
 ("t_3,t_5 for q=23", (v2(mo(23,3)), v2(mo(23,5))), (1, 2)),
]
bad = 0
for d, c, q in checks:
    ok = (c == q)
    bad += (not ok)
    print(("OK   " if ok else "FAIL ") + d, c if ok else (c, "!=", q))
print("traced values:", len(checks), "mismatches:", bad)
sys.exit(1 if bad else 0)
