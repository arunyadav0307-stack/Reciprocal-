import warnings; warnings.filterwarnings("ignore")
import math, itertools, audit_run as ar
from audit_lib import *
from audit_dist import mindist_H
def lcm(a,b): return a*b//math.gcd(a,b)
def frontier(N,q):
    fl=factors_of_xN_minus_1(N,q); fs=[f for f,_ in fl]
    idx={tuple(f):i for i,f in enumerate(fs)}
    ords=[xorder(f,q) for f in fs]; deg=[len(f)-1 for f in fs]
    rec=[idx[tuple(recip(f,q))] for f in fs]; n=len(fs)
    DC=[[i for i in range(n) if m>>i&1] for m in range(1<<n)
        if all(rec[i]!=i and not (m>>rec[i]&1) for i in range(n) if m>>i&1)]
    best={}  # d -> max K
    cache={}
    for S in DC:
        A=sum(deg[i] for i in S); K=N-2*A
        for r in range(1,len(S)+1):
            for T in itertools.combinations(S,r):
                L=1
                for i in T: L=lcm(L,ords[i])
                if L!=N: continue
                rest=tuple(sorted(i for i in S if i not in T))
                if rest not in cache:
                    g=[1]
                    for i in rest: g=pmul(g,fs[i],q)
                    cache[rest]=mindist_H(g,N,q)
                d=cache[rest]
                best[d]=max(best.get(d,-10**9),K)
    return best
print("q N w | d: maxK_observed / R8_bound  (gap)")
for q,N in [(5,4),(7,6),(11,5),(13,4),(13,6),(11,10),(13,12),(3,8),(5,8),(7,12),(5,12),(3,13),(7,9),(7,16),(3,16),(3,20),(11,14),(3,26)]:
    r=ar.analyse(N,q,dist=False); w=r['w']
    b=frontier(N,q)
    s=[]
    for d in sorted(b):
        bd=N+2-2*w-2*d
        s.append(f"d={d}:{b[d]}/{bd}({bd-b[d]})")
    print(q,N,w,'|',' '.join(s),flush=True)
