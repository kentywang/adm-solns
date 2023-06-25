#!/bin/python3

import itertools
import math

from profilerv2 import ProfilerV2
from util import asserter


#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#

# Edit: Looks like a better approach would be backtracking, or even better, DP
# I think the idea is to decompose the problem using the observation that the number
# of ways 10 can be summed to using values 1^2, 2^2, 3^2 is equal to the sum of
# the number of ways 10 is summed to using values 1^2, 2^2 and the number of ways
# 10-3^2 is summed to using values 1^2, 2^2.
# i.e. f(10,3^2) = f(1,2^2) + f(10,2^2) = 1 + 0
def powerSum(X, N):
    # O(2^(X^(1/N))) time (number of subsets), O(X^(1/N)) space (if streaming in the subsets)
    numsets = 0
    for ss in subsets(X, N):
        if sum(y ** N for y in ss) == X:
            numsets += 1
    return numsets


def subsets(X, N):
    fullset = range(1, math.floor(X ** (1 / N)) + 1)
    for subsetlen in fullset:
        for comb in itertools.combinations(fullset, subsetlen):
            yield comb


asserter(lambda: powerSum(10, 2), 1)
asserter(lambda: powerSum(100, 2), 3)
asserter(lambda: powerSum(100, 3), 1)

with ProfilerV2(powerSum, var='n', start=1, step=(lambda x: x * 4), count=5, reps=10) as (f, n):
    f(n, 2)

with ProfilerV2(powerSum, var='k', start=1, step=(lambda x: x + 1), count=5, reps=1) as (f, k):
    f(20, k)
