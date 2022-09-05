from functools import cache


def threenplusone(n):
    """
    O(1) space, unknown time (because its termination is unproven)
    """
    cycles = 0
    while True:
        cycles += 1
        if n == 1:
            return cycles
        if n % 2 == 1:
            n = 3 * n + 1
        else:
            n = n // 2


def threenplusone_recur_bad_memo(n):
    """
    Caching will work only within run yet will have
    nothing to cache, as each number is only encountered
    once.

    unknown time, space complexity
    (because its termination is unproven)
    """

    @cache
    def go(cycles, x):
        cycles += 1
        if x == 1:
            return cycles
        return go(
            cycles,
            3 * x + 1 if x % 2 else x // 2
        )

    return go(0, n)


@cache
def go2(cycles, x):
    """
    Outside of parent function so as to allow for caching across
    different parent function calls, which is what the problem
    requires.
    """
    cycles += 1
    if x == 1:
        return cycles
    return go2(
        cycles,
        3 * x + 1 if x % 2 else x // 2
    )


def threenplusone_recur_good_memo(n):
    """
    unknown time, space complexity
    (because its termination is unproven)
    """
    return go2(0, n)


def maxcyclelen(i, j):
    """
    O(1) space, assuming max() iterates its argument incrementally
    O(j-i) space otherwise

    O((j-i) * ?) time, where ? is depth of recursion
    """
    return max(threenplusone(x) for x in range(i, j + 1))


def maxcyclelen_bad_memo(i, j):
    """
    O((j-i) * ?) space, where ? is depth of recursion
    O((j-i) * ?) time, where ? is depth of recursion
    """
    return max(threenplusone_recur_bad_memo(x) for x in range(i, j + 1))


def maxcyclelen_memo(i, j):
    """
    O((j-i) * ?) space, where ? is depth of recursion
    O((j-i) * ?) time, where ? is depth of recursion

    But should perform better, timewise compared to no memo or bad memo
    """
    return max(threenplusone_recur_good_memo(x) for x in range(i, j + 1))
