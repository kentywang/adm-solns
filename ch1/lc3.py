from itertools import islice, permutations, zip_longest
from math import ceil


def is_valid(ls):
    return all(
        (i == 0 or ls[i - 1] > v) and (i == len(ls) - 1 or v < ls[i + 1])
        for i, v in islice(enumerate(ls), 0, len(ls), 2))


def wiggle_sort_v1(nums: list[int]) -> None:
    """
    Brute force: generate all permutations in O(n!) time and space
    """
    for p in permutations(nums, len(nums)):
        if is_valid(p):
            nums[:] = list(p)
            return


def wiggle_sort_v2(nums: list[int]) -> None:
    """
    Sort and partition the sides, then interleave them
    O(n log n) time, O(n) space (maybe possible to do in O(1) space)
    """
    nums.sort()

    # make sure 1st partition is bigger or equal to 2nd because the number of
    # small values must be equal or greater than the number of large values
    p1_end = ceil(len(nums) / 2) - 1

    # we must reverse both partitions to ensure adjacent elements on a sorted list
    # don't remain adjacent after merging. Kinda hard to understand, but very important.
    p1 = nums[p1_end:: -1]
    p2 = nums[len(nums) - 1: p1_end: -1]

    newnums = [q for p in zip_longest(p1, p2) for q in p]

    if len(nums) % 2 == 1:
        newnums.pop()  # because it's a None from the zip_longest

    nums[:] = newnums


def wiggle_sort_lc1(nums: list[int]) -> None:
    """
    Sort and partition the sides, then interleave them
    O(n log n) time, O(n) space
    """
    nums.sort()

    p1_end = ceil(len(nums) / 2) - 1
    newnums = [None] * len(nums)

    j = 0
    for i, v in enumerate(nums[p1_end:: -1]):
        newnums[j] = v
        j += 2

    j = 1
    for i, v in enumerate(nums[len(nums) - 1: p1_end: -1]):
        newnums[j] = v
        j += 2

    nums[:] = newnums

# In order to achieve O(n) time + O(1) space, we need to answer two questions:
#
# How to find median in O(n)+O(1)
# How to re-order the odd-even indexes "in-place" using O(1) memory.

# Three knowledge pre-requisitions:
#
# Quick select to find median in O(n) time on average, O(n^2) in worst case. Taking O(1) memory.
# "Median of medians" alogrithm to improve quick select, making the time complexity "deterministic O(n)" rather than "average O(n)".
# Virtual indexing technology to achieve in-place wiggle sort based on median value found above.
