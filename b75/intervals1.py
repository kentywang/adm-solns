# 57. Insert Interval
import sys
from typing import List

from profilerv2 import ProfilerV2


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Time: O(n^2)
        Space: O(1)

        Why do I always make things more complicated than it needs to be? Is it the pursuit of
        minimal space usage?
        """
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals

        s1, s2 = newInterval

        # add dummy at end
        intervals.append([sys.maxsize, sys.maxsize])

        for i, (a1, a2) in enumerate(intervals):
            # no overlap, is in front
            # if on dummy, this will insert at end
            # this case will also allow merged segment to be inserted
            if s1 <= s2 < a1 <= a2:
                intervals.insert(i, [s1, s2])

                intervals.pop()
                return intervals

            # completely inside one existing, no-op
            if a1 <= s1 <= s2 <= a2:
                intervals.pop()
                return intervals

            # no overlap, is in back
            if a1 <= a2 < s1 <= s2:
                continue

            # remaining cases involve overlap, so merge the intervals
            while s1 <= a1 <= s2 or s1 <= a2 <= s2:
                s1, s2 = [min(a1, s1), max(a2, s2)]
                intervals.pop(i)
                a1, a2 = intervals[i]  # this is the next interval

            intervals.insert(i, [s1, s2])

            intervals.pop()
            return intervals

    def insert2(
            self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """
        Online solution
        """
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res


# asserter(lambda: Solution().insert([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])
# asserter(lambda: Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]), [[1, 2], [3, 10], [12, 16]])
# asserter(lambda: Solution().insert([[1, 5]], [2, 7]), [[1, 7]])


with ProfilerV2(Solution().insert2, var='n', start=100, step=(lambda x: x * 10), reps=1,
                mapper=lambda x: list([y, y + 1] for y in range(0, x, 2))) as (f, n):
    f(n, [~sys.maxsize + 1, sys.maxsize - 1])

with ProfilerV2(Solution().insert, var='n', start=100, step=(lambda x: x * 10), reps=1,
                mapper=lambda x: list([y, y + 1] for y in range(0, x, 2))) as (f, n):
    f(n, [~sys.maxsize + 1, sys.maxsize - 1])

"""
Interesting, same space complexity. I expected online solution to be worse. I guess compiler optimization. 
"""
