import math, itertools
from sympy import factorint
from sympy.utilities.iterables import multiset_partitions
from g2_test import mo, v2, w, w0, adm_direct, w_two
def w_cover(N,q):
    F=factorint(N); P=list(F)
    t={p:v2(mo(q,p)) for p in P}
    admI=lambda I: not(len({t[p] for p in I})==1 and min(t[p] for p in I)>=1)
    best=math.inf
    for part in multiset_partitions(P):           # blocks A_j = primes covered at full power
        cost=0
        for A in part:
            rest=[p for p in P if p not in A]; bc=math.inf
            for r in range(len(rest)+1):
                for H in itertools.combinations(rest,r):   # helpers at exponent 1
                    I=list(A)+list(H)
                    if admI(I):
                        m=1
                        for p in A: m*=p**F[p]
                        for p in H: m*=p
                        bc=min(bc,mo(q,m))
            cost+=bc
        best=min(best,cost)
    return best
qs=[3,5,7,9,11,13,17,19,23,25,27,29,31,37,41,43,47,49,53,59,61,64,81,121,125]
n=bad=0
for q in qs:
    for N in range(3,2000,2):
        if math.gcd(N,q)!=1: continue
        if len(factorint(N))>4: continue
        n+=1; a=w(N,q); b=w_cover(N,q)
        if a!=b: bad+=1; print("FAIL",q,N,a,b)
print(f"Thm2 corrected (odd N<2000, <=4 primes): {n} cases, failures {bad}")
