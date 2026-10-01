"""Exact polynomial and coding tools over Z/q (q prime): modular polynomial arithmetic, order of x modulo f,
factorisation of x^N - 1, reciprocal polynomial, minimum distance of a cyclic code by parity-check column dependence."""
import itertools, math
from sympy import symbols, factor_list
x = symbols('x')

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]%1==0 and a[-1]==0: a.pop()
    return a or [0]

def pmul(a,b,q,m=None):
    r=[0]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        if ai:
            for j,bj in enumerate(b):
                r[i+j]=(r[i+j]+ai*bj)%q
    if m is not None:
        for i in range(len(r)-1,m-1,-1):
            r[i-m]=(r[i-m]+r[i])%q; r[i]=0
        r=r[:m]
    return trim(r)

def pmod(a,f,q):
    a=list(a); df=len(f)-1
    while len(a)-1>=df and any(a):
        if a[-1]==0: a.pop(); continue
        sh=len(a)-1-df; c=a[-1]
        for i,fc in enumerate(f):
            a[sh+i]=(a[sh+i]-c*fc)%q
        a.pop()
    return trim(a)

def xorder(f,q,maxit=100000):
    "order of x modulo monic irreducible f over Z/q"
    r=[0,1%q]; t=1
    if pmod(r,f,q)==[1]: return 1
    while t<maxit:
        r=pmod(pmul(r,[0,1%q],q),f,q); t+=1
        if r==[1]: return t
    return None

def recip(f,q):
    d=len(f)-1; inv=pow(f[0],-1,q)
    return [(c*inv)%q for c in f[::-1]]

def factors_of_xN_minus_1(N,q):
    c,fs=factor_list(x**N-1,modulus=q)
    out=[]
    for f,e in fs:
        P=f.as_poly(x)
        coeffs=[int(P.coeff_monomial(x**i))%q for i in range(P.degree()+1)]
        out.append((trim(coeffs),e))
    return out

def rank_mod(M,p):
    M=[list(r) for r in M]; rk=0; rows=len(M); cols=len(M[0]) if M else 0
    for c in range(cols):
        piv=next((i for i in range(rk,rows) if M[i][c]%p),None)
        if piv is None: continue
        M[rk],M[piv]=M[piv],M[rk]
        inv=pow(M[rk][c],-1,p); M[rk]=[v*inv%p for v in M[rk]]
        for i in range(rows):
            if i!=rk and M[i][c]%p:
                f=M[i][c]; M[i]=[(a-f*b)%p for a,b in zip(M[i],M[rk])]
        rk+=1
    return rk
def nullspace(G,p):
    k=len(G); N=len(G[0]); M=[list(r) for r in G]; pivs=[]; rk=0
    for c in range(N):
        piv=next((i for i in range(rk,k) if M[i][c]%p),None)
        if piv is None: continue
        M[rk],M[piv]=M[piv],M[rk]; inv=pow(M[rk][c],-1,p); M[rk]=[v*inv%p for v in M[rk]]
        for i in range(k):
            if i!=rk and M[i][c]%p:
                f=M[i][c]; M[i]=[(a-f*b)%p for a,b in zip(M[i],M[rk])]
        pivs.append(c); rk+=1
    free=[c for c in range(N) if c not in pivs]; basis=[]
    for fc in free:
        v=[0]*N; v[fc]=1
        for i,pc in enumerate(pivs): v[pc]=(-M[i][fc])%p
        basis.append(v)
    return basis
def mindist_H(g,N,p):
    k=N-(len(g)-1)
    if len(g)==1: return 1
    G=[[0]*i+list(g)+[0]*(N-i-len(g)) for i in range(k)]
    H=nullspace(G,p); r=len(H)
    cols=[[H[i][j] for i in range(r)] for j in range(N)]
    for s in range(1,r+2):
        for S in itertools.combinations(range(N),s):
            if rank_mod([cols[j] for j in S],p)<s: return s
    return r+1

def dcyc(g,N,p):
    k=N-(len(g)-1)
    G=[[0]*i+list(g)+[0]*(N-i-len(g)) for i in range(k)]
    H=nullspace(G,p); r=len(H); cols=[[H[i][j] for i in range(r)] for j in range(N)]
    for s in range(1,r+2):
        for S in itertools.combinations(range(1,N),s-1):
            if rank_mod([cols[0]]+[cols[j] for j in S],p)<s: return s
    return r+1

def coset(i,N,q):
    s=set(); j=i%N
    while j not in s: s.add(j); j=j*q%N
    return s
