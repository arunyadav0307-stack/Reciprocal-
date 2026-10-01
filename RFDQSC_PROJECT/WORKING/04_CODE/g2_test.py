import math, itertools, random
from sympy import factorint, isprime, primerange
def mo(q,m):
    if m==1: return 1
    k,x=1,q%m
    while x!=1: x=x*q%m;k+=1
    return k
def adm_direct(q,m):   # -1 not in <q> mod m, m>=3
    if m<3: return False
    o=mo(q,m); x=1
    for _ in range(o):
        if x==m-1: return False
        x=x*q%m
    return True
def w_dp(N,q,allowed):
    divs=[m for m in range(2,N+1) if N%m==0 and allowed(m)]
    best={1:0}; ch=True
    while ch:
        ch=False
        for L,c in list(best.items()):
            for m in divs:
                L2=L*m//math.gcd(L,m); c2=c+mo(q,m)
                if c2<best.get(L2,math.inf): best[L2]=c2; ch=True
    return best.get(N,math.inf)
w  =lambda N,q: w_dp(N,q,lambda m:adm_direct(q,m))
w0 =lambda N,q: w_dp(N,q,lambda m:True)
v2=lambda n:(n&-n).bit_length()-1
# ---- Lemma 1: for odd m, admissible <=> NOT(all t_p equal and >=1)
def adm_2adic(q,m):
    ts={v2(mo(q,p)) for p in factorint(m)}
    return not (len(ts)==1 and min(ts)>=1)
# ---- Theorem 2 (support reduction, odd N): cover formula
def w_cover(N,q):
    F=factorint(N); P=list(F); k=len(P)
    t={p:v2(mo(q,p)) for p in P}
    def admI(I):
        ts={t[p] for p in I}; return not(len(ts)==1 and min(ts)>=1)
    supports=[I for r in range(1,k+1) for I in itertools.combinations(P,r) if admI(I)]
    best=math.inf
    # choose for each prime p its coverer support containing p; helpers = other primes of that support at exponent 1
    # enumerate families of distinct supports (small k)
    for r in range(1,k+1):
        for fam in itertools.combinations(supports,r):
            if set().union(*map(set,fam))!=set(P): continue
            # assign each prime to one support containing it
            opts=[[j for j,I in enumerate(fam) if p in I] for p in P]
            for asg in itertools.product(*opts):
                cost=0
                for j,I in enumerate(fam):
                    m=1
                    for p in I: m*= p**F[p] if asg[P.index(p)]==j else p
                    cost+=mo(q,m)
                best=min(best,cost)
    return best
# ---- Theorem 3 (two prime powers, odd N) closed form
def w_two(p,a,r,b,q):
    tp,tr=v2(mo(q,p)),v2(mo(q,r))
    opa,orb,op,orr=mo(q,p**a),mo(q,r**b),mo(q,p),mo(q,r)
    L=opa*orb//math.gcd(opa,orb); l=lambda x,y:x*y//math.gcd(x,y)
    if tp==tr and tp>=1: return math.inf
    if tp==0 and tr==0: return min(L,opa+orb)
    if tp==0: return min(L,opa+l(op,orb))
    if tr==0: return min(L,orb+l(orr,opa))
    return min(L,l(opa,orr)+l(op,orb))
qs=[3,5,7,9,11,13,17,19,23,25,27,29,31,37,41,43,47,49,53,59,61,64,81,121,125]
bad1=bad2=bad3=n1=n2=n3=0; sep=0
for q in qs:
    for m in range(3,3000,2):
        if math.gcd(m,q)!=1: continue
        n1+=1
        if adm_direct(q,m)!=adm_2adic(q,m): bad1+=1; print("L1 FAIL",q,m)
    for N in range(3,1200,2):
        if math.gcd(N,q)!=1: continue
        F=factorint(N)
        if len(F)<=3:
            n2+=1; a=w(N,q); b=w_cover(N,q)
            if a!=b: bad2+=1; print("T2 FAIL",q,N,a,b)
        if len(F)==2:
            (p,a_),(r,b_)=F.items(); n3+=1
            x=w(N,q); y=w_two(p,a_,r,b_,q)
            if x!=y: bad3+=1; print("T3 FAIL",q,N,x,y)
            if x<math.inf and x!=w0(N,q): sep+=1
print(f"Lemma1: {n1} (q,m) tested, failures {bad1}")
print(f"Thm2 (support reduction, <=3 primes): {n2} (q,N), failures {bad2}")
print(f"Thm3 (two-prime closed form): {n3} (q,N), failures {bad3}; cases w!=w0 among them: {sep}")
