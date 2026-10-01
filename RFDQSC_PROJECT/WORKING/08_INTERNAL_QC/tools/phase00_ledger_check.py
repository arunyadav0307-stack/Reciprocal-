"""Phase 0 quick independent recomputation of the small worked values quoted in the manuscript.
Definition-level implementation (no theorem used): w(N,q) over sets of q-cyclotomic cosets mod N
with no coset C and its negative -C both chosen, lcm of orders = N, cost = sum of |C|."""
import math, itertools
def cosets(N,q):
    seen=set(); out=[]
    for i in range(N):
        if i in seen: continue
        c=[];j=i
        while j not in c: c.append(j); j=j*q%N
        seen|=set(c); out.append(frozenset(c))
    return out
def w_def(N,q,reciprocal_free=True):
    cs=cosets(N,q); idx={c:k for k,c in enumerate(cs)}
    neg=[idx[frozenset((-j)%N for j in c)] for c in cs]
    ordr=[N//math.gcd(min(c) if min(c)>0 else 0,N) if any(c) else 1 for c in cs]
    cand=[k for k in range(len(cs)) if ordr[k]>1 and (not reciprocal_free or neg[k]!=k)]
    # DP over candidates: state = (lcm, chosen-set-of-negatives) is exponential; use direct DFS with pruning
    best=[math.inf]
    def rec(i,chosen,L,cost):
        if cost>=best[0]: return
        if L==N: best[0]=cost; return
        for k in range(i,len(cand)):
            c=cand[k]
            if reciprocal_free and (neg[c] in chosen): continue
            rec(k+1,chosen|{c},L*ordr[c]//math.gcd(L,ordr[c]),cost+len(cs[c]))
    rec(0,frozenset(),1,0)
    return best[0]
def o(q,m):
    k,x=1,q%m
    while x!=1%m: x=x*q%m; k+=1
    return k
checks=[("w(143,3)",143,3,8,True),("w0(143,3)",143,3,8,False),("w(55,3)",55,3,20,True),("w0(55,3)",55,3,9,False),
("w(225,23)",225,23,32,True),("w0(225,23)",225,23,26,False),("w(35,3)",35,3,12,True),("w0(35,3)",35,3,10,False),
("w(26,3)",26,3,3,True),("w(82,37)",82,37,5,True),("w(80,3)",80,3,4,True),("w(5,3)",5,3,math.inf,True),("w0(5,3)",5,3,4,False),("w(2,q) q=3",2,3,math.inf,True)]
for name,N,q,claim,rf in checks:
    v=w_def(N,q,rf); print(f"{name:14s} claimed={claim!s:5s} recomputed={v!s:5s} {'OK' if v==claim else 'MISMATCH'}")
print("ord_80(3)",o(3,80),"ord_26(3)",o(3,26),"ord_82(37)",o(37,82),"o(225,23)",o(23,225), "o(143,3)",o(3,143))
# Table 1 arithmetic
for ex,(N,w,B,s,K,dD,Dl) in {"Ex1":(26,3,6,6,2,4,12),"Ex2":(82,5,10,10,42,6,20),"Ex3":(80,4,8,8,48,4,18)}.items():
    print(ex,"N+2-2w=",N+2-2*w,"K+2d=",K+2*dD,"Delta=",N+2-2*w-K-2*dD,"claimed",Dl,"2(s-w)=",2*(s-w),"2(B+1-d)=",2*(B+1-dD))
print("sum of check counts:",1999+99981+39968+39968+195405+30079+594+1081)
print("class2 tuples:",75+1490+10269+19908,"saturated:",75+1482+10263+19896)
