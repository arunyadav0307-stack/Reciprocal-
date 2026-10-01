"""Phase 2 independent check (written fresh; does not reuse the authors' scripts).
Definition-level search over q-cyclotomic cosets compared with
 (a) Theorem A  (support reduction, helpers to exponent 1),
 (b) Theorem B  (four-case table),
 (c) Theorem C(ii) closed form,
 (d) Theorem 11.1(i) value for N = 2n.
This is a finite spot check, not a proof or an exhaustive verification."""
import itertools, math, sys
from math import gcd
from sympy import factorint, primerange, isprime, primitive_root

def mord(q, m):
    if m == 1: return 1
    k, x = 1, q % m
    while x != 1:
        x = x*q % m; k += 1
    return k

def cosets(N, q):
    seen, out = set(), []
    for i in range(N):
        if i in seen: continue
        c, x = [], i
        while x not in c:
            c.append(x); x = x*q % N
        seen.update(c); out.append(frozenset(c))
    return out

def brute(N, q, reciprocal_free):
    cs = cosets(N, q)
    info = []
    for c in cs:
        i = min(c)
        order = N // gcd(i, N)
        neg = frozenset((-x) % N for x in c)
        info.append((len(c), order, neg == c, neg))
    idx = {c: k for k, c in enumerate(cs)}
    # orders per coset; need lcm = N. Exhaustive DFS with bound.
    n = len(cs)
    best = [math.inf]
    order_list = sorted(range(n), key=lambda k: info[k][0])
    def rec(pos, chosen, cost, l):
        if cost >= best[0]: return
        if l == N:
            best[0] = cost; return
        if pos == n: return
        k = order_list[pos]
        # option: take
        ok = True
        if reciprocal_free:
            if info[k][2]: ok = False
            elif idx[info[k][3]] in chosen: ok = False
        if ok:
            chosen.add(k)
            rec(pos+1, chosen, cost+info[k][0], l*info[k][1]//gcd(l, info[k][1]))
            chosen.discard(k)
        rec(pos+1, chosen, cost, l)
    rec(0, set(), 0, 1)
    return best[0]

def admissible(m, q):
    if m <= 2: return False
    x = 1
    for _ in range(mord(q, m)):
        x = x*q % m
        if x == m-1: return False
    return True

def thmA(N, q):
    P = sorted(factorint(N)); a = factorint(N)
    def c(A):
        rest = [r for r in P if r not in A]
        nA = math.prod(p**a[p] for p in A)
        best = math.inf
        for k in range(len(rest)+1):
            for H in itertools.combinations(rest, k):
                m = nA*math.prod(H)
                if admissible(m, q): best = min(best, mord(q, m))
        return best
    def parts(s):
        if not s: yield []; return
        f, rest = s[0], s[1:]
        for p in parts(rest):
            yield [[f]]+p
            for i in range(len(p)):
                yield p[:i]+[[f]+p[i]]+p[i+1:]
    return min(sum(c(A) for A in pt) for pt in parts(P))

def w0A(N, q):
    P = sorted(factorint(N)); a = factorint(N)
    def parts(s):
        if not s: yield []; return
        f, rest = s[0], s[1:]
        for p in parts(rest):
            yield [[f]]+p
            for i in range(len(p)):
                yield p[:i]+[[f]+p[i]]+p[i+1:]
    return min(sum(mord(q, math.prod(p**a[p] for p in A)) for A in pt) for pt in parts(P))

def t(p, q):
    o = mord(q, p); v = 0
    while o % 2 == 0: o//=2; v+=1
    return v

def thmB(p, a, r, b, q):
    op, orr = mord(q, p**a), mord(q, r**b); op0, or0 = mord(q, p), mord(q, r)
    L = math.lcm(op, orr); tp, tr = t(p, q), t(r, q)
    if tp == tr >= 1: w = math.inf
    elif tp == tr == 0: w = min(L, op+orr)
    elif tp == 0: w = min(L, op + math.lcm(op0, orr))
    elif tr == 0: w = min(L, orr + math.lcm(op, or0))
    else: w = min(L, math.lcm(op, or0)+math.lcm(op0, orr))
    return w, min(L, op+orr)

fails = 0; n_def = 0; n_B = 0
INF = math.inf
for q in [2,3,4,5,7,8,9,11,13]:
    for N in range(3, 400):
        if gcd(N, q) != 1 or N % 2 == 0: continue
        if len(cosets(N, q)) > 18: continue
        w = brute(N, q, True); w0 = brute(N, q, False)
        n_def += 1
        if w != thmA(N, q) or w0 != w0A(N, q) or w0 != w0A(N,q):
            fails += 1; print("A/def mismatch", q, N, w, thmA(N, q), w0, w0A(N, q))
        f = factorint(N)
        if len(f) == 2:
            (p, a), (r, b) = sorted(f.items())
            tw, tw0 = thmB(p, a, r, b, q); n_B += 1
            if (tw, tw0) != (w, w0):
                fails += 1; print("B mismatch", q, N, (tw, tw0), (w, w0))
print("definition-level cases:", n_def, " Theorem B cases:", n_B, " failures:", fails)

# Theorem A / B with larger N (formula-vs-formula only, no brute force)
nAB = 0
for q in [2,3,5,7,11,13,16,17,19,23]:
    for N in range(3, 3000, 2):
        if gcd(N, q) != 1: continue
        f = factorint(N)
        if len(f) == 2:
            (p, a), (r, b) = sorted(f.items())
            if thmB(p, a, r, b, q) != (thmA(N, q), w0A(N, q)):
                fails += 1; print("A vs B", q, N)
            nAB += 1
print("Theorem A vs B formula comparisons:", nAB, " failures:", fails)

# Theorem C(ii) family
nC = 0
for p in primerange(7, 120):
    if p % 4 != 3: continue
    for r in primerange(5, 120):
        if r % 8 != 5 or r == p: continue
        if gcd((p-1)//2, (r-1)//4) != 1: continue
        for q in primerange(2, 400):
            if q in (p, r): continue
            if mord(q, p) == p-1 and mord(q, r) == r-1:
                nC += 1
                N = p*r
                wv, w0v = thmB(p, 1, r, 1, q)
                if (wv, w0v) != ((p-1)*(r-1)//2, p+r-2):
                    fails += 1; print("C(ii) mismatch", p, r, q, wv, w0v)
                if N < 400 and len(cosets(N, q)) <= 18 and brute(N, q, True) != wv:
                    fails += 1; print("C(ii) brute mismatch", p, r, q)
print("Theorem C(ii) triples:", nC, " failures:", fails)

# Theorem 11.1 (i): N = 2n, q odd, n odd prime, -1 not in <q> mod 2n
nT = 0
for q in [3,5,7,9,11,13,17,19,23,25,27,29,31,37]:
    for n in primerange(3, 120):
        if q % n == 0: continue
        if not admissible(2*n, q): continue
        o = mord(q, n)
        if mord(q, 2*n) != o:
            fails += 1; print('ord_2n != ord_n', q, n)
        if len(cosets(2*n, q)) <= 18:
            wd, w0d = brute(2*n, q, True), brute(2*n, q, False)
            nT += 1
            if (wd, w0d) != (o, o):
                fails += 1; print("11.1(i) mismatch", q, n, wd, w0d, o)
print("Theorem 11.1(i) definition-level cases:", nT, " total failures:", fails)
sys.exit(1 if fails else 0)
