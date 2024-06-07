# Tests the speed of the algorithm
#
# On my machine, n = 20! * 6! and m = 21! * 6!
# with 1000 trials takes about 0.7s. Prior to
# using numpy arrays and np.kron, it took ~8.4s.

from common_factors import cfs
from time import time_ns as timer
from math import factorial

# A pair of large numbers with plenty of factors
n = factorial(20) * factorial(6)
m = n * 21

# Number of trails to perform
trials = 1000

# Ready, set, go!
start = timer()
for i in range(trials):
    cf = cfs(n, m)
end = timer()

# Prints results
print(f'Time taken:\t{(end - start) / 1e9}s')