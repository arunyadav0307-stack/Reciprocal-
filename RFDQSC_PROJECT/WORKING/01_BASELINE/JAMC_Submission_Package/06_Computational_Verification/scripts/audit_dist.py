import itertools, numpy as np
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
