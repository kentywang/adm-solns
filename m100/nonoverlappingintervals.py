"""
21:54 - 23:13 (79m with hints)

Observations:
- Don't think O(n^2) would even be enough for a brute force soln
- Sorting will help us notice overlap quickly
- We should delete the largest intervals to maximize impact.
- Sort by earliest start time, then by latest end time
    - compare pairwise, if overlap, remove 1st since it should have bigger overlap

- Okay, I think exhaustive is the better approach.

    [[1,3],[1,2],[2,3]] expect 1

Verdict: I went with exhaustive DFS memo approach, but it turned out the
soln was just to remove the later-ending interval at each comparison, so
it's just a O(n lg n) soln.
"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        prev_end = float("-inf")
        dels = 0

        for start, end in intervals:
            if start < prev_end:
                # prefer deleting interval w later end
                prev_end = min(prev_end, end)
                dels += 1
            else:
                prev_end = end

        return dels


print(Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [-100, -2], [5, 7]]))
