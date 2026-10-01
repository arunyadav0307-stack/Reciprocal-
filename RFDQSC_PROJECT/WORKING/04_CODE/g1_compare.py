# Compare w (admissibility-constrained) with the classical unconstrained
# w0(N,q) = min{ sum ord_m(q) : m|N, lcm = N } = min degree of a poly of order N
#         = min n s.t. GL_n(F_q) has an element of order N  (gcd(N,q)=1)
import math
def mo(q,m):
    k,x=1,q%m
    while x!=1%m: x=x*q%m;k+=1
    return k
def adm(q,m): return m>=3 and (m-1) not in {pow(q,i,m) for i in range(mo(q,m))}
def cover(N,q,allowed):
    divs=[m for m in range(1,N+1) if N%m==0 and allowed(m)]
    best={1:0}; changed=True
    while changed:
        changed=False
        for L,c in list(best.items()):
            for m in divs:
                L2=L*m//math.gcd(L,m); c2=c+mo(q,m)
                if c2<best.get(L2,math.inf): best[L2]=c2; changed=True
    return best.get(N,math.inf)
tot=diff=0; ex=[]
for q in [3,5,7,9,11,13,17,19,23,25,27]:
    for N in range(3,301):
        if math.gcd(N,q)!=1 or not adm(q,N): continue
        w=cover(N,q,lambda m:adm(q,m)); w0=cover(N,q,lambda m:True)
        tot+=1
        if w!=w0: diff+=1; ex.append((q,N,w0,w))
print(f"admissible (q,N): {tot};  w != w0 in {diff} cases")
for e in ex[:10]: print("  q=%d N=%d  w0=%d  w=%d"%e)
