# Started 8/28
# Finished 8/29
from itertools import combinations
from random import randint


# Describe how to test whether a given set of tickets establishes sufficient
# coverage in the Lotto problem of Section 1.8 (page 22). Write a program to
# find good ticket sets.
def guar_win(numpool: int, slots: int, win_thresh: int):
    """
    - generate all possible tickets
    - check that each possibility has win_thresh number of overlapping
      elements with at least one of the passed tickets
    """

    def sufficient_overlap(a, b) -> bool:
        return len(a.intersection(b)) >= win_thresh

    def wrapper(*tickets: list[set[int]]):
        possib = frozenset(frozenset(c) for c in combinations(range(1, numpool + 1), slots))

        possibility_covered = [False] * len(possib)
        for i, p in enumerate(possib):
            possibility_covered[i] = any(sufficient_overlap(p, t) for t in tickets)

        return all(possibility_covered)

    return wrapper


def gen_tix_v1(numpool: int, slots: int, win_thresh: int) -> frozenset[frozenset[int]]:
    """
    - generate all possible tickets
    - generate all possible ticket subsets, filter subsets that don't cover
      fully, then choose smallest of the subsets
    """

    possib = frozenset(frozenset(c) for c in combinations(range(1, numpool + 1), slots))

    subsets = set()
    for subset_sz in range(len(possib) + 1):
        subsets.update(frozenset(c) for c in combinations(possib, subset_sz))

    gw = guar_win(numpool, slots, win_thresh)  # duplicates possibility generation. consider changing
    min_ss_seen = min(filter(lambda ss: gw(*ss), subsets), key=len)

    return min_ss_seen


def gen_tix_v2(numpool: int, slots: int, win_thresh: int) -> frozenset[frozenset[int]]:
    """
    - generate all possible tickets
    - randomly pick tickets from there until we've attained full coverage
    """

    def find_coverage_subset(t: frozenset[int]) -> set[frozenset[int]]:
        cs = set(frozenset(c) for c in combinations(t, win_thresh))  # {{2,4}, {2,5}, {3,4}}
        for _ in range(slots - win_thresh):
            exp_cs = set()
            for c in cs:
                rem_numpool = set(range(1, numpool + 1)).difference(c)  # nums not yet in this combo
                for next_num in rem_numpool:  # {{2,4,1}, {2,4,3}, ... }
                    exp_cs.add(frozenset({*c, next_num}))  # fan out for each c
            cs = exp_cs
        return cs

    possib = list(frozenset(c) for c in combinations(range(1, numpool + 1), slots))
    possibility_covered = set()
    subset = set()

    while len(possibility_covered) < len(possib):
        another_ticket = possib[randint(0, numpool - 1)]
        if another_ticket not in subset:
            subset.add(another_ticket)
            coverages = find_coverage_subset(another_ticket)  # i.e {1,2,3} -> 8 possible tickets covered
            possibility_covered.update(coverages)  # add to possibility covered

    return frozenset(subset)
