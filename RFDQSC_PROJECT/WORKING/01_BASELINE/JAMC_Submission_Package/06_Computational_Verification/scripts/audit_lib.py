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
