# An implementation of an algorithm to find all common factors.
# Source: https://math.stackexchange.com/questions/2576881/find-common-factors-of-any-two-numbers#:~:text=Step%201%3A%20Use%20the%20Euclidean,powers%20of%20(distinct)%20primes.
#
# Wow, I needed more lines of comments than code!
# What a nasty and beautiful little algorithm.

from sympy.ntheory import factorint
from sympy import gcd
from numpy import array, kron, ndarray


# Finds the common factors
def cfs(n: int, m: int) -> ndarray[int]:

    # Gets the greatest common denominator
    gcf = gcd(n, m)

    # Gets the prime factors of the gcd
    pfs = factorint(gcf)

    # 1 is always a common factor.
    # We need this to be a non-empty list for
    cfs = array([1], dtype='float64')

    # Recursively finds the common factors by performing
    # the Kronecker product on column matrices composed of
    # mixed radix numbers. In each matrix, there is one
    # base and it contains all values where the radix is
    # equal to or less than the occurances of that
    # base in the prime factorization of the greatest
    # common demoninator.
    #
    # Phew, that's a mouthful!
    return cfs_recursive(pfs, cfs)

# Recursively performs the Kronecker product
def cfs_recursive(pfs: dict, cfs: ndarray) -> ndarray[int]:
    
    # Base cases.
    # Return common factors when there are no
    # more items to perform the Kronecker on
    if len(pfs) == 0:
        return cfs
    
    # Removes an item from the dictionary, getting
    # a base a radix to create a new matrix
    factor, radix = pfs.popitem()

    # Get all items in a mixed radix matrix
    radices = array([factor ** i for i in range(radix + 1)])

    # By performing the Kronecker product on our existing
    # common factors column vector and the mixed radix 
    # matrix, we find more common factors.
    cfs = kron(cfs, radices)

    # Again!
    return cfs_recursive(pfs, cfs)