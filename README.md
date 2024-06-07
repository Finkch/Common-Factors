# Common-Factors

A module to rather quickly get a list of all common factors between a pair of numbers.

If `a` and `b` are two integers, then the first step is to find their greatest common denominator. Then, the prime factorisation of the greatest common denominator is determined. For each prime factor `f` and number of occurances `i`, a column vector whose members are of the form `f^r` for `r` belonging to `{0, 1, 2, ..., i}`. Finally, the common factors are found by applying the Kronecker product to reduce the set of column vectors to a single column vector.


## common_factors.py

The file that contains the necessary methods to compute the common factors between two numbers. It requires the libraries sympy and numpy to work.


### cfs(a: int, b: int) -> ndarray

Accepts two integers, `a` and `b`, and returns a column vector numpy array that contains all the common factors of `a` and `b`. This function sets up for `cfs_recursive`, which actually finds the common factors.


### cfs_recursive(pfs: dict, cfs: ndarray) -> ndarray

A recursive function first called by `cfs()` to find the common factors. `pfs` is a dictionary whose keys are prime factors and whose values are the occurance of its respective prime factor; items are popped from `pfs` in every step of recursion. `cfs` is the current numpy array of common factors.


## performance.py

A small file to test the performance of the algorithm.
