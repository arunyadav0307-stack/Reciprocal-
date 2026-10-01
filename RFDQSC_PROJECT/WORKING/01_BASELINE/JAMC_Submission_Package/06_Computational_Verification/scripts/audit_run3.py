import warnings; warnings.filterwarnings("ignore")
import math, audit_run as ar
from audit_dist import mindist_H
ar.mindist=lambda g,N,q: mindist_H(g,N,q)
# cross-check with enumeration on small cases first
import itertools
from audit_run import mindist as _
print("q N w bound best=(K+2d,K,d) viol tight?")
for q,N in [(5,4),(3,8),(5,8),(7,6),(3,11),(3,13),(11,5),(7,3),(13,4),(13,6),(5,12),(7,12),(7,9),(11,8),(13,8),(13,9),(5,11),(11,7),(3,16),(7,15),(7,16),(11,10),(11,14),(3,20),(3,26),(13,12)]:
    r=ar.analyse(N,q)
    b=r['best']; bd=N+2-2*r['w']
    print(q,N,r['w'],bd,(b[0],b[1],b[2]),len(r['viol']),'TIGHT' if b[0]==bd else 'gap %d'%(bd-b[0]),flush=True)
