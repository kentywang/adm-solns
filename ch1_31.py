# Started 8/28
# Finished ___
from itertools import combinations

from profiler import profile


# Describe how to test whether a given set of tickets establishes sufficient
# coverage in the Lotto problem of Section 1.8 (page 22). Write a program to
# find good ticket sets.
def guar_win(numpool: int, slots: int, win_thresh: int):
    """
    - generate all possible tickets
    - check that each possibility has win_thresh number of overlapping
      elements with at least one of the tickets
    """

    def sufficient_overlap(a: set[int], b: set[int]):
        return len(a.intersection(b)) >= win_thresh

    def wrapper(*tickets):
        possib = list(set(c) for c in combinations(range(1, numpool + 1), slots))

        possibility_covered = [False] * len(possib)
        for i, p in enumerate(possib):
            possibility_covered[i] = any(sufficient_overlap(p, t) for t in tickets)

        return all(possibility_covered)

    return wrapper


@profile
def gen_tix(numpool: int, slots: int, win_thresh: int):
    pass
