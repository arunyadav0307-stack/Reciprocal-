"""Run from 04_CODE/curated (needs rfd_core). Second-round finite-range checks on ranges disjoint from verify_theorems.py (larger q and larger N).
Run: python3 verify_extension.py"""
import math, time
from sympy import factorint
from rfd_core import mo, v2, adm, wdp, admsupp, wA, w0A, wB
pp_hi=[x for x in range(128,257) if len(factorint(x))==1]
sub=[2,3,5,7,11,13,16,25]
R={}
def rec(k,ok,first=None):
    n,f,c=R.get(k,(0,0,None)); R[k]=(n+1,f+(0 if ok else 1),c if ok or c else first)
t0=time.time()
for q in pp_hi:                                   # Lemma 5.1, new q
    for m in range(3,3000,2):
        if math.gcd(m,q)==1: rec("Lemma 5.1 (q 128-256, m<3000)",adm(q,m)==admsupp([v2(mo(q,p)) for p in factorint(m)]),(q,m))
for q in sub:                                     # Lemma 5.1, larger m
    for m in range(5001,12001,2):
        if math.gcd(m,q)==1: rec("Lemma 5.1 (small q, 5000<m<12000)",adm(q,m)==admsupp([v2(mo(q,p)) for p in factorint(m)]),(q,m))
for q in pp_hi:                                   # Theorem A + w0 formula, new q
    for N in range(3,1200,2):
        if math.gcd(N,q)!=1: continue
        rec("Theorem A (q 128-256, N<1200)",wdp(N,q)==wA(N,q),(q,N)); rec("(6.3) (q 128-256, N<1200)",wdp(N,q,False)==w0A(N,q),(q,N))
for q in sub:                                     # Theorem A, larger N (includes many 3-4 prime N)
    for N in range(2001,3601,2):
        if math.gcd(N,q)!=1: continue
        rec("Theorem A (small q, 2000<N<3600)",wdp(N,q)==wA(N,q),(q,N)); rec("(6.3) (small q, 2000<N<3600)",wdp(N,q,False)==w0A(N,q),(q,N))
for q in pp_hi:                                   # Theorem B, new q
    for N in range(15,8000,2):
        F=factorint(N)
        if len(F)!=2 or math.gcd(N,q)!=1: continue
        (p,a),(r,b)=F.items(); rec("Theorem B (q 128-256, N<8000)",wdp(N,q)==wB(p,a,r,b,q),(q,N))
for q in sub:                                     # Theorem B, larger N
    for N in range(20001,30001,2):
        F=factorint(N)
        if len(F)!=2 or math.gcd(N,q)!=1: continue
        (p,a),(r,b)=F.items(); rec("Theorem B (small q, 20000<N<30000)",wdp(N,q)==wB(p,a,r,b,q),(q,N))
oddhi=[x for x in pp_hi if x%2]
from sympy import primerange
for q in oddhi:                                   # Thm 11.1(i), new q
    for n in primerange(3,400):
        if q%n==0: continue
        N=2*n
        if not adm(q,N): continue
        o=mo(q,n)
        degs={len({j*pow(q,k,N)%N for k in range(o+5)}) for j in range(1,N) if math.gcd(j,N) in (1,2)}
        rec("Theorem 11.1(i) (q 129-255 odd, n<400)",mo(q,N)==o and degs=={o} and wdp(N,q)==o and wdp(N,q,False)==o,(q,n))
print("time",round(time.time()-t0))
tot=0
for k,(n,f,c) in R.items(): print(f"{k}: tested {n}, failures {f}, first failure {c}"); tot+=n
print("TOTAL",tot)
