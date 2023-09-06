# 920 · Meeting Rooms
from typing import (
    List,
)

from util import asserter


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


"""
Brute force: check each pair of meetings for overlap (if A.start < B.start, there's overlap if B.start < A.end)
Time: O(n^2)
Space: O(1)

Option 2: Sort by start time, check each adjacent pairs for overlap
Time: O(n lg n)
Space: O(1)

Theoretical optimal:
Time: O(n)
Space: O(1)
"""


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x[0])

        for i in range(len(intervals) - 1):
            (a_start, a_end) = intervals[i]
            (b_start, b_end) = intervals[i + 1]
            if b_start < a_end:
                return False

        # for (a_start, a_end), (b_start, b_end) in pairwise(intervals):
        #     if b_start < a_end:
        #         return False

        return True


asserter(lambda: Solution().can_attend_meetings([(0, 30), (5, 10), (15, 20)]), False)
asserter(lambda: Solution().can_attend_meetings([(5, 8), (8, 15)]), True)
