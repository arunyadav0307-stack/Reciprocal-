"""Core routines for the reciprocal-free minimum-degree problem (exact integer arithmetic).

mo(q,m)      multiplicative order of q modulo m (o(m) in the paper)
adm(q,m)     m is admissible: -1 not in <q> mod m (m >= 3)
wdp(N,q)     w(N,q) by dynamic programming over the lcm-cover form (Proposition 4.2); useadm=False gives w0
wcoset(N,q)  w(N,q) by brute force over q-cyclotomic cosets (independent of Proposition 4.2)
wA(N,q)      right-hand side of Theorem A, formula (6.2);  w0A(N,q): formula (6.3), odd N
wB(p,a,r,b,q) Theorem B, N = p^a r^b
"""
import math, itertools, functools
from sympy import factorint, primerange, isprime, primitive_root, divisors
from sympy.utilities.iterables import multiset_partitions
@functools.lru_cache(None)
def mo(q,m):
    if m==1: return 1
    k,x=1,q%m
    while x!=1: x=x*q%m;k+=1
    return k
v2=lambda n:(n&-n).bit_length()-1
@functools.lru_cache(None)
def adm(q,m):
    if m<3: return False
    x=1
    for _ in range(mo(q,m)):
        if x==m-1: return False
        x=x*q%m
    return True
def wdp(N,q,useadm=True):
    ds=[m for m in divisors(N) if m>1 and (adm(q,m) if useadm else True)]
    best={1:0}
    for m in ds:                      # each divisor used at most once (set)
        new=dict(best)
        for L,c in best.items():
            L2=L*m//math.gcd(L,m); c2=c+mo(q,m)
            if c2<new.get(L2,math.inf): new[L2]=c2
        best=new
    return best.get(N,math.inf)
# independent brute force: subsets of cyclotomic cosets
def wcoset(N,q):
    seen=set(); cos=[]
    for i in range(N):
        if i in seen: continue
        c=set(); j=i
        while j not in c: c.add(j); j=j*q%N
        seen|=c; cos.append(frozenset(c))
    idx={c:k for k,c in enumerate(cos)}
    neg=[idx[frozenset((-j)%N for j in c)] for c in cos]
    cand=[k for k in range(len(cos)) if neg[k]!=k]
    order=[N//math.gcd(min(cos[k]),N) for k in range(len(cos))]
    best=math.inf
    if len(cand)>22: return None
    for r in range(1,len(cand)+1):
        for S in itertools.combinations(cand,r):
            Ss=set(S)
            if any(neg[k] in Ss for k in S): continue
            L=1
            for k in S: L=L*order[k]//math.gcd(L,order[k])
            if L==N: best=min(best,sum(len(cos[k]) for k in S))
    return best
def admsupp(ts): return not(len(set(ts))==1 and min(ts)>=1)
def wA(N,q):
    F=factorint(N); P=list(F); t={p:v2(mo(q,p)) for p in P}; best=math.inf
    for part in multiset_partitions(P):
        cost=0
        for A in part:
            rest=[p for p in P if p not in A]; bc=math.inf
            for r in range(len(rest)+1):
                for H in itertools.combinations(rest,r):
                    if admsupp([t[p] for p in list(A)+list(H)]):
                        m=math.prod(p**F[p] for p in A)*math.prod(H); bc=min(bc,mo(q,m))
            cost+=bc
        best=min(best,cost)
    return best
def w0A(N,q):
    F=factorint(N); P=list(F)
    return min(sum(mo(q,math.prod(p**F[p] for p in A)) for A in part) for part in multiset_partitions(P))
def wB(p,a,r,b,q):
    tp,tr=v2(mo(q,p)),v2(mo(q,r)); l=lambda x,y:x*y//math.gcd(x,y)
    A_,B_,op,orr=mo(q,p**a),mo(q,r**b),mo(q,p),mo(q,r); L=l(A_,B_)
    if tp==tr and tp>=1: return math.inf
    if tp==0 and tr==0: return min(L,A_+B_)
    if tp==0: return min(L,A_+l(op,B_))
    if tr==0: return min(L,B_+l(orr,A_))
    return min(L,l(A_,orr)+l(op,B_))
