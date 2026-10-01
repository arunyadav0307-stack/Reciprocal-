"""Class 1 check (w(2n,q) = ord_n(q) = ord_2n(q)) and Class 2 computational observations under the reconstructed index rule."""
import math
from sympy import primerange
from rfd_core import mo, wdp
from poly_tools import coset
w=lambda N,q: wdp(N,q)
w0=lambda N,q: wdp(N,q,False)
# Class 1: n odd prime, q odd prime power, gcd, -1 not in <q> mod 2n
bad=cnt=0
for q in [3,5,7,9,11,13,17,19,23,25,27,29,31,37,41,43,47,49]:
    for n in primerange(3,80):
        if q%n==0: continue
        N=2*n
        if not all(pow(q,k,N)!=N-1 for k in range(mo(q,N))): continue
        cnt+=1; o=mo(q,n)
        if w(N,q)!=o or mo(q,N)!=o: bad+=1; print("C1 FAIL",q,n)
print("class-1 instances:",cnt,"violations of w(2n,q)=ord_n(q)=ord_2n(q):",bad)
# Class 2 BCH: n=(q^{2m}-1)/(q-1), cosets mod 2n; index rules as printed in Ex.3
def lcmord(S,N): 
    L=1
    for i in S: L=L*(N//math.gcd(i,N))//math.gcd(L,N//math.gcd(i,N))
    return L
for q,m in [(3,2),(5,2),(7,2),(3,3)]:
    n=(q**(2*m)-1)//(q-1); N=2*n
    dmax=(q**m-1)//(q-1); dsmax=(q**(m+1)+q**m+q-3)//(2*(q-1))
    W=w(N,q) if N<1000 else None
    stats={}; minS=math.inf; cls3=0; tot=0
    for d in range(2,dmax+1):
      for i in range(1,d-1):
        c1={min(coset(2*k,N,q)) for k in range(0,d-1)}; c3={min(coset(2*k,N,q)) for k in range(0,d-i-1)}
        H1=c1-c3
        if not H1: continue
        for ds in range(2,dsmax+1):
          for j in range(1,ds-1):
            c2={min(coset(1+2*k,N,q)) for k in range(0,ds-1)}; c4={min(coset(1+2*k,N,q)) for k in range(0,ds-j-1)}
            H2=c2-c4
            if not H2: continue
            H=H1|H2; s=sum(len(coset(c,N,q)) for c in H)
            roots=set().union(*[coset(c,N,q) for c in H])
            tot+=1
            if lcmord(roots,N)!=N: cls3+=1; continue
            minS=min(minS,s); stats[s]=stats.get(s,0)+1
    print(f"class2 q={q} m={m} N={N} ord_N={mo(q,N)} w={W} w0={w0(N,q) if N<1000 else None} | instances={tot} ord(h)<N: {cls3} | min s={minS} | s-distribution={dict(sorted(stats.items()))}")
