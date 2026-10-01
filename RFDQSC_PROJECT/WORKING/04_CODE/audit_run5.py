import warnings; warnings.filterwarnings("ignore")
import math, itertools
from audit_lib import *
from audit_dist import mindist_H
def ppow(f,e,q):
    r=[1]
    for _ in range(e): r=pmul(r,f,q)
    return r
def ceil_log(e,p):
    k=0
    while p**k<e: k+=1
    return k
print("== R2 / C3: ord(f^e) vs ord(f)*p^ceil(log_p e); and defect s(f)")
bad=0; tot=0
for q in [3,5,7]:
    for N in range(2,13):
        if math.gcd(N,q)!=1: continue
        for f,_ in factors_of_xN_minus_1(N,q):
            of=xorder(f,q)
            # defect: is f^2 | x^{ord f}-1 ?
            X=[q-1]+[0]*(of-1)+[1]
            s_def = pmod(X,ppow(f,2,q),q)==[0]
            for e in range(1,q*q+2):
                o=xorder(ppow(f,e,q),q,maxit=10**5)
                pred=of*q**ceil_log(e,q)
                tot+=1; bad+=(o!=pred)
                if s_def: print("DEFECT FOUND",q,f)
print(f"  instances={tot}  mismatches={bad}  (any defect found would be printed above)")

print("\n== R3: claimed equivalence 'dual-containing <=> g*g^* = 0 mod x^N-1'")
q,N=5,4; g=[1]   # C = whole space: dual-containing trivially
print("  g=1: C=F_5^4, C^perp={0} subset C: TRUE; g*g^* mod x^4-1 =",pmul(g,recip(g,q),q,m=N),"-> not 0: equivalence FALSE")
g=[3,1]  # x-2
gg=pmul(g,recip(g,q),q,m=N)
print("  g=x-2 (dual-containing, verified in App.A): g*g^* mod x^4-1 =",gg)

print("\n== R7 counterexample: q=3, N=8")
for f,_ in factors_of_xN_minus_1(8,3):
    print("   factor",f,"deg",len(f)-1,"order",xorder(f,3),"self-recip",recip(f,3)==f)
print("  <3> mod 8 =",sorted({pow(3,i,8) for i in range(4)}),"; -1=7 in it?",7 in {pow(3,i,8) for i in range(4)})

print("\n== R9 family: splitting regime, g_C zeros zeta^1..zeta^A, g_D zeros zeta^2..zeta^A")
def fam(q,N,A):
    # primitive N-th root in F_q (q prime)
    z=next(a for a in range(2,q) if pow(a,N,q)==1 and all(pow(a,N//r,q)!=1 for r in range(2,N+1) if N%r==0 and all(r%s for s in range(2,r))))
    S=[pow(z,i,q) for i in range(1,A+1)]
    inv={pow(s,-1,q) for s in S}
    dc = not (set(S)&inv) and 1 not in S and q-1 not in S
    gC=[1]
    for s in S: gC=pmul(gC,[(-s)%q,1],q)
    gD=[1]
    for s in S[1:]: gD=pmul(gD,[(-s)%q,1],q)
    K=N-2*A; dB=mindist_H(gD,N,q); dP=mindist_H(gC,N,q)
    return dc,K,dB,dP
for q,N in [(11,10),(13,12),(13,6),(7,6)]:
    for A in range(1,N//2+1):
        dc,K,dB,dP=fam(q,N,A)
        print(f"  q={q} N={N} A={A}: dual-containing={dc} K={K} d_bit={dB} (claim {A}) d_phase={dP} (claim {A+1}) K+2d_bit={K+2*dB} vs N={N}")
