from functools import cache
from math import inf

"""
Options:
1. Brute: Generate 2^n different configurations (2^n ops), filter to valid ones (k for each ops), return one with the fewest transmitters

O(2^n) space, O((2^n)*k) time (where k is number of transmitters)
"""


def hackerlandRadioTransmitters_dp(x, k):
    """
    2. DP recursive: Sort, then recurse to two branches per node, one where transmitter is installed and problem
    set is reduced, and another where transmitter isn't installed and problem set remains the same. Pick min
    of the branches

    O(n) space, O(2^n) time
    """

    def go(i, j, ct):
        # Base cases
        if i == len(x):
            return ct

        if j == len(x):
            return inf  # ran out of nodes to install on, but still have nodes that need reception

        # Option 1: don't install at current node j
        ops = [go(i, j + 1, ct)]

        # Option 2: install at current node j, then calculate how many nodes that moves us up
        # Can only install if it covers node i, otherwise we'd skip over a node
        if x[j] - k <= x[i]:
            while i < len(x) and x[i] <= x[j] + k:  # increment i until it is no longer under the umbrella
                i += 1
            ops.append(go(i, j + 1, ct + 1))

        return min(ops)

    x.sort()
    return go(0, 0, 0)


def hackerlandRadioTransmitters_dp_memo(x, k):
    """
    3. With DP memoization, we'll store what we pass to each recursive call, which should be
    - the node/index on a line graph from which we still need to solve (n possible options)
    - the node/index from which we're considering installing from (n possible options)
    - the transmitter count we've used so far

    O(n^3) space, same for time because each subproblem takes O(1) time to solve since all it takes
    is calling the min function on the return values from the recurisive calls.
 for _ in range(max_ct_needed)]

    """
    n = len(x)
    max_ct_needed = n
    memo = [[[None for _ in range(max_ct_needed)] for _ in range(n)] for _ in range(n)]

    def go(i, j, ct):
        if i < n and j < n and ct < max_ct_needed and memo[i][j][ct]:
            return memo[i][j][ct]

        # Base cases
        if i == n:
            return ct

        if j == n:
            return inf  # ran out of nodes to install on, but still have nodes that need reception

        # Option 1: don't install at current node j
        ops = [go(i, j + 1, ct)]

        # Option 2: install at current node j, then calculate how many nodes that moves us up
        # Can only install if it covers node i, otherwise we'd skip over a node
        if x[j] - k <= x[i]:
            i2 = i
            while i2 < n and x[i2] <= x[j] + k:  # increment i until it is no longer under the umbrella
                i2 += 1
            ops.append(go(i2, j + 1, ct + 1))

        memo[i][j][ct] = min(ops)
        return memo[i][j][ct]

    x.sort()
    return go(0, 0, 0)


def hackerlandRadioTransmitters_dp_builtin_cache(x, k):
    """Using builtin cache"""

    n = len(x)

    @cache
    def go(i, j, ct):
        # Base cases
        if i == n:
            return ct

        if j == n:
            return inf  # ran out of nodes to install on, but still have nodes that need reception

        # Option 1: don't install at current node j
        ops = [go(i, j + 1, ct)]

        # Option 2: install at current node j, then calculate how many nodes that moves us up
        # Can only install if it covers node i, otherwise we'd skip over a node
        if x[j] - k <= x[i]:
            i2 = i
            while i2 < n and x[i2] <= x[j] + k:  # increment i until it is no longer under the umbrella
                i2 += 1
            ops.append(go(i2, j + 1, ct + 1))

        return min(ops)

    x.sort()
    return go(0, 0, 0)
