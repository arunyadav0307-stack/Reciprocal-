import math
from sympy import primerange, isprime, primitive_root, factorint
from sympy.ntheory.modular import crt
from g2_test import mo, w, w0
rows=[]; bad=0; cnt=0
P=[p for p in primerange(7,200) if p%4==3]
R=[r for r in primerange(5,200) if r%8==5]
for p in P:
    for r in R:
        if math.gcd((p-1)//2,(r-1)//4)!=1: continue
        gp,gr=primitive_root(p),primitive_root(r)
        base,mod=crt([p,r],[gp,gr]); base=int(base)
        q=base
        while not isprime(q): q+=p*r        # Dirichlet: a prime q in the class
        cnt+=1
        N=p*r; W=w(N,q); W0=w0(N,q)
        pred=(p-1)*(r-1)//2
        if W!=pred or W0!=p+r-2: bad+=1; print("FAIL",p,r,q,W,pred,W0)
        rows.append((p,r,q,W,W0,W/W0))
print(f"separation family: {cnt} (p,r,q) instances, failures {bad}")
rows.sort(key=lambda x:-x[5])
for x in rows[:6]: print("  p=%d r=%d q=%d  w=%d  w0=%d  ratio=%.1f"%x)
# counterexample hunt: hypotheses minus one (gcd condition dropped / same t)
viol=0
for p in P[:15]:
    for r in R[:15]:
        g=math.gcd((p-1)//2,(r-1)//4)
        if g==1: continue
        gp,gr=primitive_root(p),primitive_root(r)
        base,_=crt([p,r],[gp,gr]); q=int(base)
        while not isprime(q): q+=p*r
        if w(p*r,q)!=(p-1)*(r-1)//(2*g): viol+=1
print("gcd-condition dropped: w = lcm(p-1,r-1) still holds? violations:",viol)
