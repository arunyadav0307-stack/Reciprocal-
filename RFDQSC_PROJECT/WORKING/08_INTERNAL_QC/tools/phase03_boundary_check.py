"""Phase 3: boundary / limiting-case stress test (fresh code).
Parts
 1. Elementary boundary values: N=2, N=3, prime N, prime-power N, w=1, w<=ord_N(q), q even.
 2. Even N (Prop 4.2/4.3 are stated for all N): definition-level vs lcm-cover.
 3. Theorem C(ii) lower end and the p=3 remark.
 4. Full enumeration of ALL saturated dual-containing pairs (C,D) for N=2n, n odd prime, q prime odd:
    dimension K>=0, Singleton, s>=w, Theorem 11.1 (ii),(iii) when h1,h2 nonconstant, and what happens when one is constant.
Finite spot checks only."""
import itertools, math, sys
from math import gcd
import numpy as np
from sympy import Poly, symbols, GF, factor_list, primerange, factorint
sys.path.insert(0, __file__.rsplit('/',1)[0])
x = symbols('x')
fails = 0
def mord(q, m):
    if m == 1: return 1
    k, y = 1, q % m
    while y != 1: y = y*q % m; k += 1
    return k
def cosets(N, q):
    seen, out = set(), []
    for i in range(N):
        if i in seen: continue
        c, y = [], i
        while y not in c: c.append(y); y = y*q % N
        seen.update(c); out.append(frozenset(c))
    return out
def brute(N, q, rf):
    cs = cosets(N, q); n = len(cs)
    info = []
    for c in cs:
        i = min(c); neg = frozenset((-v) % N for v in c)
        info.append((len(c), N//gcd(i, N), neg == c, neg))
    idx = {c: k for k, c in enumerate(cs)}
    best = [math.inf]
    order = sorted(range(n), key=lambda k: info[k][0])
    def rec(pos, chosen, cost, l):
        if cost >= best[0]: return
        if l == N: best[0] = cost; return
        if pos == n: return
        k = order[pos]
        if not rf or (not info[k][2] and idx[info[k][3]] not in chosen):
            chosen.add(k); rec(pos+1, chosen, cost+info[k][0], l*info[k][1]//gcd(l, info[k][1])); chosen.discard(k)
        rec(pos+1, chosen, cost, l)
    rec(0, set(), 0, 1)
    return best[0]
def inadm(m, q):
    if m <= 2: return True
    y = 1
    for _ in range(mord(q, m)):
        y = y*q % m
        if y == m-1: return True
    return False
def check(c, msg):
    global fails
    if not c: fails += 1; print("FAIL", msg)

# ---- Part 1
cnt = 0
for q in [2,3,4,5,7,8,9,11,13,16,25,27]:
    # N = 2
    if q % 2: check(brute(2, q, True) == math.inf and brute(2, q, False) == 1, f"N=2 q={q}")
    for N in range(3, 200):
        if gcd(N, q) != 1: continue
        if len(cosets(N, q)) > 18: continue
        w, w0 = brute(N, q, True), brute(N, q, False)
        cnt += 1
        o = mord(q, N)
        check(w0 <= w, f"w0<=w {q} {N}")
        check((w == math.inf) == inadm(N, q), f"finiteness<->admissible {q} {N}")
        if w < math.inf: check(1 <= w <= o, f"1<=w<=o {q} {N}")
        if N > 2: check((w == 1) == ((q-1) % N == 0), f"w=1 iff N|q-1 {q} {N}")
        check(w0 <= o, f"w0<=o {q} {N}")
        if w < math.inf: check(2*w <= N, f"2w<=N (K>=0 compatibility) {q} {N} {w}")
        if N == 3: check(w == (1 if q % 3 == 1 else math.inf), f"N=3 {q}")
        f = factorint(N)
        if len(f) == 1:  # prime power
            check(w0 == o, f"prime power w0=o {q} {N}")
            check(w == (math.inf if inadm(N, q) else o), f"prime power w {q} {N}")
print("part1 cases:", cnt, "fails so far:", fails)

# ---- Part 2: even N, lcm-cover (Prop 4.2) vs definition level
def lcm_cover(N, q, rf):
    divs = [d for d in range(2, N+1) if N % d == 0 and (not rf or not inadm(d, q))]
    best = math.inf
    for k in range(1, len(divs)+1):
        for S in itertools.combinations(divs, k):
            l = 1
            for d in S: l = l*d//gcd(l, d)
            if l == N: best = min(best, sum(mord(q, d) for d in S))
    return best
c2 = 0
for q in [3,5,7,9,11,13]:
    for N in range(4, 130, 2):
        if gcd(N, q) != 1 or len(cosets(N, q)) > 18 or len([d for d in range(2, N+1) if N % d == 0]) > 14: continue
        c2 += 1
        check(brute(N, q, True) == lcm_cover(N, q, True), f"even lcm-cover rf {q} {N}")
        check(brute(N, q, False) == lcm_cover(N, q, False), f"even lcm-cover {q} {N}")
print("part2 even-N cases:", c2, "fails so far:", fails)

# ---- Part 3
for q in [3, 5, 7, 11, 13, 17, 19]:
    for r in primerange(5, 200):
        if r % 8 != 5 or gcd(r, q) != 1 or q % 3 != 2: continue
        if mord(q, 3) == 2 and mord(q, r) == r-1 and len(cosets(3*r, q)) <= 18:
            check(brute(3*r, q, True) == r-1 and brute(3*r, q, False) == r-1, f"p=3 remark {q} {r}")
# p=7, r=5 lower end
for q in primerange(2, 400):
    if q in (5, 7): continue
    if mord(q, 7) == 6 and mord(q, 5) == 4:
        check(brute(35, q, True) == 12 and brute(35, q, False) == 10, f"p=7,r=5 q={q}")
print("part3 done; fails so far:", fails)

# ---- Part 4
def tof(poly, p): return [int(c) % p for c in Poly(poly, x, modulus=p).all_coeffs()]
def recip(c, p):  # c: highest-degree first, monic, c[-1]!=0
    a = c[::-1]; inv = pow(a[0] if False else c[-1], -1, p)
    return [(v*inv) % p for v in a]
def pmul(a, b, p):
    r = [0]*(len(a)+len(b)-1)
    for i, u in enumerate(a):
        for j, v in enumerate(b): r[i+j] = (r[i+j]+u*v) % p
    return r
def mindist(gD, N, p, limit=3000000):
    B = len(gD)-1; k = N-B
    if k == 0: return None
    if p**k > limit: return None
    low = gD[::-1]
    G = np.zeros((k, N), dtype=np.int64)
    for i in range(k): G[i, i:i+B+1] = low
    best = N
    # enumerate messages with first nonzero coordinate equal to 1 (scalar multiples give same weight)
    for lead in range(k):
        rest = k-lead-1
        if rest == 0:
            msgs = np.zeros((1, k), dtype=np.int64); msgs[0, lead] = 1
        else:
            tail = np.array(list(itertools.product(range(p), repeat=rest)), dtype=np.int64)
            msgs = np.zeros((len(tail), k), dtype=np.int64); msgs[:, lead] = 1; msgs[:, lead+1:] = tail
        cw = (msgs @ G) % p
        best = min(best, int((cw != 0).sum(axis=1).min()))
    return best
n4 = n4s = n4c = nd = n4low = 0
for p in [3, 5, 7, 11, 13]:
    for n in [3, 5, 7, 11, 13, 17]:
        if p % n == 0: continue
        N = 2*n
        o = mord(p, n)
        facs = [tof(f, p) for f, _ in factor_list(x**N-1, modulus=p)[1]]
        facs = [f for f in facs]
        m = len(facs)
        if m > 12: continue
        dfac = []
        for f in facs:
            deg = len(f)-1
            # order: smallest e | N with f | x^e-1
            e = next(e for e in range(1, N+1) if N % e == 0 and Poly(x**e-1, x, modulus=p).rem(Poly(f, x, modulus=p)).is_zero)
            rf = recip(f, p)
            dfac.append((deg, e, facs.index(rf) if rf in facs else None))
        # which factors divide x^n-1 (orders | n) vs x^n+1
        side = ['c' if N//1 and n % d[1] == 0 else 'n' for d in dfac]
        w = brute(N, p, True)
        for state in itertools.product((0, 1, 2), repeat=m):  # 0 not in C, 1 in C\D, 2 in D
            C = {i for i in range(m) if state[i] >= 1}
            if any(dfac[i][2] in C for i in C): continue   # g_C g_C* | x^N-1  <=> no factor and its reciprocal both in C (and none self-recip)
            H = [i for i in range(m) if state[i] == 1]
            if not H: continue
            l = 1
            for i in H: l = l*dfac[i][1]//gcd(l, dfac[i][1])
            if l != N: continue                           # saturated only
            s = sum(dfac[i][0] for i in H); B = sum(dfac[i][0] for i in range(m) if state[i] == 2)
            gC = sum(dfac[i][0] for i in C)
            K = N-2*gC
            n4 += 1
            check(K >= 0, f"K>=0 {p} {n}")
            check(s >= w, f"s>=w {p} {n}")
            h1 = [i for i in H if side[i] == 'c']; h2 = [i for i in H if side[i] == 'n']
            check(len(h2) >= 1, "ord(h)=N forces a factor on the negacyclic side")
            if h1 and h2:
                n4c += 1
                check(s >= 2*o and w == o, f"Thm 11.1(ii) {p} {n} s={s} o={o}")
                if True:
                    gD = [1]
                    for i in range(m):
                        if state[i] == 2: gD = pmul(gD, facs[i], p)
                    d = mindist(gD, N, p)
                    if d is not None:
                        nd += 1
                        Delta = (N+2-2*w)-(K+2*d)
                        check(d <= B+1, "Singleton"); check(Delta == 2*(s-w)+2*(B+1-d), "identity 10.1")
                        check(Delta >= 2*w, f"Thm 11.1(iii) {p} {n}")
            else:
                n4s += 1
                check(s >= w, "s>=w")
                if s < 2*o: n4low += 1
print(f"part4: saturated dual-containing pairs enumerated={n4}; both sides nonconstant={n4c} (with exact d(D): {nd}); h1 constant={n4s} (of which s<2w: {n4low})")
if n4s: print("  (pairs with h1 constant exist: there s may equal w, so the hypothesis 'both nonconstant' is essential to s>=2w)")
print("TOTAL FAILS:", fails)
sys.exit(1 if fails else 0)
