"""
Coding      7:29 - 7:58 (29m)

Sloppy logic, but it worked! Really nice, interesting problem.

[[0,30],[5,10],[15,20]]

[[2,4], [7,10]]

Time: O(n lg n)
Space: O(n)
"""
from collections import namedtuple
from heapq import heappush, heappop

Meeting = namedtuple('Meeting', ['start', 'end'])


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort by start time
        intervals = sorted(Meeting(*mtng) for mtng in intervals)  # O(n lg n)
        best = 1
        h = []

        for meeting in intervals:
            # we can't add curr meeting into heap until it "begins".
            # keep removing from heap until we start overlapping with the curr meeting
            # each removal is like skipping in time to that meeting's end time
            while h and h[0] <= meeting.start:
                heappop(h)
            # add interval
            else:
                heappush(h, meeting.end)  # queue by end time
                best = max(best, len(h))

        return best
