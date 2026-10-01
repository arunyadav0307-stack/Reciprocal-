import itertools, math, warnings, sys
warnings.filterwarnings("ignore")
from audit_lib import *
import numpy as np

def lcm(a,b): return a*b//math.gcd(a,b)
def polyprod(fs,q):
    r=[1]
    for f in fs: r=pmul(r,f,q)
    return r
def mindist(g,N,q,cap=200000):
    k=N-(len(g)-1)
    if k==0: return None
    if q**k>cap: return -1
    G=np.zeros((k,N),dtype=np.int64)
    for i in range(k): G[i,i:i+len(g)]=g
    best=N
    msgs=np.array(list(itertools.product(range(q),repeat=k))[1:],dtype=np.int64)
    W=(msgs@G)%q
    return int((W!=0).sum(1).min())

def analyse(N,q,dist=True):
    fl=factors_of_xN_minus_1(N,q)
    assert all(e==1 for _,e in fl)
    fs=[f for f,_ in fl]
    idx={tuple(f):i for i,f in enumerate(fs)}
    ords=[xorder(f,q) for f in fs]
    rec=[idx[tuple(recip(f,q))] for f in fs]
    selfrec=[rec[i]==i for i in range(len(fs))]
    n=len(fs)
    res=dict(N=N,q=q,ords=ords,deg=[len(f)-1 for f in fs],selfrec=selfrec)
    # admissible (dual-containing) generator subsets: criterion e_f+e_f* <= 1
    DC=[]
    for mask in range(1<<n):
        S=[i for i in range(n) if mask>>i&1]
        if all(not (mask>>rec[i]&1) or rec[i]==i and False for i in S) and all(rec[i]!=i for i in S):
            DC.append(S)
    res['nDC']=len(DC)
    # w: min degree of subset of some DC set with lcm of orders = N
    w=math.inf; maxord=1
    for S in DC:
        for r in range(1,len(S)+1):
            for T in itertools.combinations(S,r):
                L=1
                for i in T: L=lcm(L,ords[i])
                maxord=max(maxord,L)
                if L==N: w=min(w,sum(res['deg'][i] for i in T))
    res['w']=w; res['maxord']=maxord
    # R8 brute force
    best=None; viol=[]
    if dist and w<math.inf:
        for S in DC:
            A=sum(res['deg'][i] for i in S); K=N-2*A
            for r in range(1,len(S)+1):
                for T in itertools.combinations(S,r):   # T = factors of h
                    L=1
                    for i in T: L=lcm(L,ords[i])
                    if L!=N: continue
                    gD=polyprod([fs[i] for i in S if i not in T],q)
                    d=mindist(gD,N,q)
                    if d==-1: continue
                    val=K+2*d
                    if val>N+2-2*w: viol.append((S,T,K,d))
                    if best is None or val>best[0]: best=(val,K,d,[fs[i] for i in S],[fs[i] for i in T])
    res['best']=best; res['viol']=viol
    return res

if __name__=="__main__":
    rows=[]
    for q in [3,5,7,11,13]:
        for N in range(3,17):
            if math.gcd(N,q)!=1: continue
            r=analyse(N,q,dist=True)
            b=r['best']
            rows.append((q,N,r['nDC'],r['maxord'],r['w'],(N+2-2*r['w']) if r['w']<math.inf else '-',b[0] if b else '-',len(r['viol'])))
            print(*rows[-1],flush=True)
