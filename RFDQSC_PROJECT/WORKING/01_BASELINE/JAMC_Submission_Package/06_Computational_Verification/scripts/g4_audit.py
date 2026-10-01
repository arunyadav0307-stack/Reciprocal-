import math, itertools, functools, time
from sympy import factorint, primerange, isprime, primitive_root, divisors
from sympy.ntheory.modular import crt
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
        if math.gcd(m,q)==1: rec("Lemma 1",adm(q,m)==admsupp([v2(mo(q,p)) for p in factorint(m)]),(q,m))
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
        rec("Theorem 2 (i)-(ii) structure",mo(q,N)==o and degs=={o} and wdp(N,q)==o and wdp(N,q,False)==o,(q,n))
print("time",round(time.time()-t0))
for k,(n,f,c) in R.items(): print(f"{k}: tested {n}, failures {f}, first failure {c}")
