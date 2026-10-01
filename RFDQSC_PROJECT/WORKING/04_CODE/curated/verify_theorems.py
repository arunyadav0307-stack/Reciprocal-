"""Finite-range checks of Lemma 5.1, Theorems A, B, C and Theorem 11.1(i) against definition-level computations.
Run: python3 verify_theorems.py   (about 4 minutes). Output: one line per check family with the number of tests and failures."""
import math, itertools, time
from sympy import factorint, primerange, isprime, primitive_root
from sympy.ntheory.modular import crt
from rfd_core import mo, v2, adm, wdp, wcoset, admsupp, wA, w0A, wB
pp=[x for x in range(2,128) if len(factorint(x))==1]
oddq=[x for x in pp if x%2]
R={}
def rec(k,ok,first=None):
    n,f,c=R.get(k,(0,0,None)); R[k]=(n+1,f+(0 if ok else 1),c if ok or c else first)
t0=time.time()
# 0. independent coset brute force vs DP (N odd and even, small)
for q in [2,3,4,5,7,8,9,11,13,16,17,19,23,25,27]:
    for N in range(3,200):
        if math.gcd(N,q)!=1: continue
        b=wcoset(N,q)
        if b is None: continue
        rec("DP vs coset brute force",wdp(N,q)==b,(q,N))
# 1. Lemma 1
for q in pp:
    for m in range(3,5000,2):
        if math.gcd(m,q)==1: rec("Lemma 5.1",adm(q,m)==admsupp([v2(mo(q,p)) for p in factorint(m)]),(q,m))
# 2. Theorem A + w0 reduction
for q in pp:
    for N in range(3,2000,2):
        if math.gcd(N,q)!=1: continue
        W=wdp(N,q); rec("Theorem A",W==wA(N,q),(q,N)); rec("w0 partition formula",wdp(N,q,False)==w0A(N,q),(q,N))
# 3. Theorem B large range
for q in pp:
    for N in range(15,20000,2):
        F=factorint(N)
        if len(F)!=2 or math.gcd(N,q)!=1: continue
        (p,a),(r,b)=F.items(); rec("Theorem B",wdp(N,q)==wB(p,a,r,b,q),(q,N))
# 4. Theorem C (i) and (ii)
for q in pp:
    for p in primerange(3,400):
        for r in primerange(p+1,400):
            if q%p==0 or q%r==0: continue
            tp,tr=v2(mo(q,p)),v2(mo(q,r))
            if tp>=1 and tr>=1 and tp!=tr:
                rec("Theorem C(i)",wdp(p*r,q)==mo(q,p)*mo(q,r)//math.gcd(mo(q,p),mo(q,r)),(q,p,r))
for p in [x for x in primerange(7,400) if x%4==3]:
    for r in [x for x in primerange(5,400) if x%8==5]:
        if math.gcd((p-1)//2,(r-1)//4)!=1: continue
        q=int(crt([p,r],[primitive_root(p),primitive_root(r)])[0])
        while not isprime(q): q+=p*r
        ok=(wdp(p*r,q)==(p-1)*(r-1)//2 and wdp(p*r,q,False)==p+r-2 and mo(q,p)==p-1 and mo(q,r)==r-1)
        rec("Theorem C(ii) instances",ok,(p,r,q))
# 5. Theorem 2 (A class 1): ord_{2n}=ord_n, all Phi_n / Phi_2n factor degrees = o, w=w0=o
for q in oddq:
    for n in primerange(3,400):
        if q%n==0: continue
        N=2*n
        if not adm(q,N): continue
        o=mo(q,n)
        degs={len({j*pow(q,k,N)%N for k in range(o+5)}) for j in range(1,N) if math.gcd(j,N) in (1,2)}
        rec("Theorem 11.1 (i) and factor-degree structure",mo(q,N)==o and degs=={o} and wdp(N,q)==o and wdp(N,q,False)==o,(q,n))
print("time",round(time.time()-t0))
for k,(n,f,c) in R.items(): print(f"{k}: tested {n}, failures {f}, first failure {c}")
