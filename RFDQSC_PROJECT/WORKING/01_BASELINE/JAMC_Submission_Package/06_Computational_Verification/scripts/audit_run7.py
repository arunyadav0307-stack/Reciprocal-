import math
from audit_run6 import w_dp, mulord, adm
cnt=0; strict=[]
for q in [3,5,7,9,11,13,17,19,23,25,27]:
    for N in range(3,301):
        if math.gcd(N,q)!=1 or not adm(q,N): continue
        cnt+=1; w=w_dp(N,q); o=mulord(q,N)
        if w<o: strict.append((q,N,w,o))
print("admissible (q,N) checked:",cnt,"; cases w < ord_N(q):",len(strict))
for s in strict[:12]: print("  q=%d N=%d w=%d ord_N(q)=%d"%s)
