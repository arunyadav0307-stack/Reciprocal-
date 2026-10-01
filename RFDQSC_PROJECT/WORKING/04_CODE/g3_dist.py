import itertools
from audit_dist import nullspace, rank_mod
def dcyc(g,N,p):
    k=N-(len(g)-1)
    G=[[0]*i+list(g)+[0]*(N-i-len(g)) for i in range(k)]
    H=nullspace(G,p); r=len(H); cols=[[H[i][j] for i in range(r)] for j in range(N)]
    for s in range(1,r+2):
        for S in itertools.combinations(range(1,N),s-1):
            if rank_mod([cols[0]]+[cols[j] for j in S],p)<s: return s
    return r+1
