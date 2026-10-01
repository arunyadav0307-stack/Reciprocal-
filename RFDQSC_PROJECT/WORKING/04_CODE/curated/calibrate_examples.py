"""Calibration of the three examples of Li and Zhu (Table 2 of the paper): generator degrees, ord(h), dual containment, exact d(D), K, Delta.
Example 3 is evaluated twice: with the factor list as printed (including m0 = x - 1) and without m0."""
import math, itertools, warnings; warnings.filterwarnings("ignore")
from poly_tools import pmul, pmod, xorder, recip, factors_of_xN_minus_1, trim, mindist_H, dcyc, coset
from rfd_core import mo, wdp
w=lambda N,q: wdp(N,q)
w0=lambda N,q: wdp(N,q,False)
class Ext:  # F_q[x]/(f), elements = coefficient lists
    def __init__(s,f,q): s.f,s.q=f,q
    def mul(s,a,b): return pmod(pmul(a,b,s.q),s.f,s.q)
    def pw(s,a,e):
        r=[1]
        while e:
            if e&1: r=s.mul(r,a)
            a=s.mul(a,a); e>>=1
        return r
def minpolys(N,q):
    fs=[f for f,e in factors_of_xN_minus_1(N,q)]
    f1=[f for f in fs if xorder(f,q)==N][0]; E=Ext(f1,q)
    def m(i):
        P=[[1]]  # poly over ext: list of ext elems, low->high
        for j in coset(i,N,q):
            r=E.pw([0,1],j); neg=[(-c)%q for c in r]
            new=[[0]]*(len(P)+1)
            for k,c in enumerate(P):
                new[k]=trim([(a+b)%q for a,b in itertools.zip_longest(new[k],E.mul(c,neg),fillvalue=0)])
                new[k+1]=trim([(a+b)%q for a,b in itertools.zip_longest(new[k+1],c,fillvalue=0)])
            P=new
        return [ (c[0] if c else 0) for c in P]
    return m
def prod(ps,q):
    r=[1]
    for p in ps: r=pmul(r,p,q)
    return r
deg=lambda f:len(trim(f))-1
ex=[("A-Ex1",3,13,[2,4],[2],[1,5],[1]),
    ("A-Ex2",37,41,[2,4],[2],[1,3],[1]),
    ("A-Ex3 (printed g1,g3 incl. m0)",3,40,[0,2,4],[0,2],[1,3,5],[1,3]),
    ("A-Ex3 (without m0)",3,40,[2,4],[2],[1,3,5],[1,3])]
for name,q,n,g1,g3,g2,g4 in ex:
    N=2*n; m=minpolys(N,q)
    uniq=lambda L:{min(coset(i,N,q)):i for i in L}.values()
    gC=prod([m(i) for i in uniq(g1+g2)],q); gD=prod([m(i) for i in uniq(g3+g4)],q)
    A,B=deg(gC),deg(gD); h=prod([m(i) for i in uniq(set(g1+g2)-set(g3+g4))],q)
    Dd=dcyc(gD,N,q)
    # dual-containing test: gC*recip(gC) | x^N-1 (simple roots)
    xN=[q-1]+[0]*(N-1)+[1]
    dc = not any(pmod(xN,pmul(gC,recip(gC,q),q),q))
    W,W0,O=w(N,q),w0(N,q),mo(q,N)
    K=N-2*A; oh=xorder(h,q)
    print(flush=True,end="");print(f"{name}: q={q} N={N} A={A} B={B} s={A-B} deg h={deg(h)} ord(h)={oh} K={K} dD={Dd} dualcont={dc} | w={W} w0={W0} ord_N={O} | R8rhs={N+2-2*W} K+2dD={K+2*Dd} Delta={N+2-2*W-K-2*Dd}")
