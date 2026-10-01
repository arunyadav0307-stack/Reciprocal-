import warnings; warnings.filterwarnings("ignore")
import math, itertools, numpy as np
import audit_run as ar
from audit_lib import *
# bigger distance cap, chunked
def mindist(g,N,q,cap=3_000_000):
    k=N-(len(g)-1)
    if q**k>cap: return -1
    G=np.zeros((k,N),dtype=np.int64)
    for i in range(k): G[i,i:i+len(g)]=g
    best=N
    it=itertools.product(range(q),repeat=k); next(it)
    while True:
        chunk=list(itertools.islice(it,200000))
        if not chunk: break
        W=(np.array(chunk,dtype=np.int64)@G)%q
        best=min(best,int((W!=0).sum(1).min()))
    return best
ar.mindist=mindist
print("q N w bound best(K,d) viol")
for q,N in [(3,13),(3,16),(5,11),(5,12),(7,9),(7,12),(11,5),(11,7),(11,8),(13,6),(13,8),(13,9),(3,20),(3,26)]:
    r=ar.analyse(N,q)
    b=r['best']
    print(q,N,r['w'],N+2-2*r['w'] if r['w']<math.inf else '-', (b[0],b[1],b[2]) if b else '-',len(r['viol']),flush=True)
