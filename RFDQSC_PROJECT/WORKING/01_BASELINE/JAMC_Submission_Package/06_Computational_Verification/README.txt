Online Resource 2 (ESM_2) - Python verification code
Article: Reciprocal-free divisors of prescribed order over finite fields and the saturation cost of cyclic quantum synchronizable codes
Journal: Journal of Applied Mathematics and Computing. Authors: [INSERT]. Corresponding author: [INSERT]

Requirements: Python 3, sympy.
audit_lib.py      core routines (orders, cyclotomic cosets, w and w0 by lcm-cover DP and brute force)
audit_run*.py     verification runs (Lemma 5.1, Theorems A, B, C, 11.1)
audit_dist.py     exact minimum distance by parity-check rank (Sect. 11.3)
g*_*.py           gate-specific checks (Theorem C, calibration of [A], Class 2 observations)
The computations are a finite stress test; they do not replace the proofs.
