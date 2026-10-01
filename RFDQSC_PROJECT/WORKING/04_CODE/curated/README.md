# Code for "Reciprocal-free divisors of prescribed order over finite fields and the saturation cost of cyclic quantum synchronizable codes"

Python 3 with `sympy` (tested with Python 3.11.2, sympy 1.14.0). All computations use exact integer arithmetic; no random numbers are used.

| File | Purpose | Paper reference |
|---|---|---|
| `rfd_core.py` | orders o(m), admissibility, w and w0 (lcm-cover dynamic programme, coset brute force), formulas of Theorems A and B | Prop. 4.2, Lemma 5.1, Thm A, Thm B |
| `poly_tools.py` | polynomial arithmetic over Z/q, order of x modulo f, factorisation of x^N-1, exact minimum distance of a cyclic code | Sect. 11.3 |
| `verify_theorems.py` | finite-range checks of Lemma 5.1, Theorems A, B, C(i), C(ii) and Theorem 11.1(i); about 4 minutes; 409,075 checks | Sect. 12.3 |
| `calibrate_examples.py` | Table 2 (generator degrees, ord(h), dual containment, exact d(D), K, Delta) | Sect. 11.3, Table 2 |
| `class2_observations.py` | Class 1 check and Class 2 counts under the reconstructed index rule; about 2 minutes | Sect. 11.4 |

Run each script from this directory, e.g. `python3 verify_theorems.py`. The computations are finite-range checks; they do not replace the proofs.
