"""
Planning
20:40 - 21:41 (61m)

Verdict: harder than it should've been. Missed the optimal soln

Observations:

Options:
- BF
    - for every pair of digits, we can save the value after swapping and see if it was
      bigger than the best
    - T: O(n^2) or O(log (n^2))
    - S: O(1)
- sort the numbers, then for each digit from hi to lo, try a swap if the sorted is bigger
    - need to keep indices on sorted value so we can know which index to swap with
    - also should sort secondarily based on highest index first
ex:
            999816
sorted      988641

    - T: O(n lg log) or O((log n) lg (log n))
    - S: O(n)
"""

from collections import namedtuple

Digit = namedtuple('Digit', ['num', 'index'])


class Solution:
    def maximumSwap(self, num: int) -> int:
        numsStr = [digit for digit in str(num)]
        biggestPossNum = sorted((Digit(digit, i) for i, digit in enumerate(numsStr)), reverse=True)

        i = j = 0
        while i < len(numsStr) and j < len(numsStr):
            m = biggestPossNum[j].num
            k = biggestPossNum[j].index

            # we shouldn't ever swap to something earlier in the list with our sorting
            if k < i:
                j += 1
                continue

            # increment both ptrs if value is already at the place it should be
            if numsStr[i] == m and i < k:
                i += 1
                continue

            if i == k:  # nothign to swap since same index
                i += 1
                j += 1
                continue

            if numsStr[i] < m:
                numsStr[i], numsStr[k] = numsStr[k], numsStr[i]
                return int(''.join(numsStr))

        return num
