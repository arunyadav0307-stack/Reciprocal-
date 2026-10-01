import warnings; warnings.filterwarnings("ignore")
import math
import audit_run as ar
def mulord(q,m):
    k=1;x=q%m
    while x!=1%m: x=x*q%m;k+=1
    return k
def adm(q,m):  # order-m factors admissible (squarefree): m>=3 and -1 not in <q> mod m
    if m<=2: return False
    return (m-1) not in {pow(q,i,m) for i in range(mulord(q,m))}
def w_dp(N,q):
    divs=[m for m in range(1,N+1) if N%m==0]
    best={1:0}
    for _ in range(len(divs)):
        for L,c in list(best.items()):
            for m in divs:
                if adm(q,m):
                    L2=L*m//math.gcd(L,m); c2=c+mulord(q,m)
                    if c2<best.get(L2,math.inf): best[L2]=c2
    return best.get(N,math.inf)
mism=0; partial=[]; cnt=0
for q in [3,5,7,11,13]:
    for N in range(3,25):
        if math.gcd(N,q)!=1: continue
        r=ar.analyse(N,q,dist=False); cnt+=1
        wd=w_dp(N,q)
        if wd!=r['w']: mism+=1; print("MISMATCH",q,N,wd,r['w'])
        if r['nDC']>1 and r['maxord']<N: partial.append((q,N,r['nDC'],r['maxord']))
print(f"DP vs brute-force w over {cnt} (q,N): mismatches={mism}")
print("Cases with nontrivial dual-containing codes but NO saturation (maxord<N):")
for p in partial: print("  q=%d N=%d  #DC gens=%d  max ord(h)=%d"%p)
