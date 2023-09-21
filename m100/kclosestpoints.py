"""
17:57 - 18:23 (26m)
"""
from heapq import heappush, heappop


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # calc dist to origin for each pt   [O(n)]
        # throw into min-heap               [O(n)]
        # get k elements                    [O(k lg n)]
        heap = []

        for x, y in points:
            heappush(heap, (sqrt(x ** 2 + y ** 2), [x, y]))

        return [heappop(heap)[1] for _ in range(k)]
