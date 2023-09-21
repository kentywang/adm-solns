"""
 8:10 - 8:44 (34m)
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start time, if same start then sort by end time
        intervals.sort()

        # keep 1 pointer, check element after pointer until no more element there
        # check that next.start <= curr.end; if so, mergeable, so we set curr to None
        # and next to the merge ([curr.start, max(ends)]). move pointer up
        i = 0
        while i + 1 < len(intervals):
            if intervals[i + 1][0] <= intervals[i][1]:
                intervals[i + 1] = [
                    intervals[i][0],
                    max(intervals[i][1], intervals[i + 1][1])
                ]
                intervals[i] = None

            i += 1

        # pass thru the array one more time to only take the non-None intervals
        return list(itvl for itvl in intervals if itvl)
