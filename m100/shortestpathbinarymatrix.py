"""
Coding      20:45 - 21:20 (35m)
Debugging   21:20 - 22:00 (40m)

Directional BFS     Beats 87.38%of users with Python3
Time:   O(mn)
Space:  O(mn)
"""
from collections import deque
from itertools import product, filterfalse
from typing import List

from util import asserter


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # edge case when start or end is 1
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        if n == 1:
            return -1 if grid[0][0] else 1

        seen1 = dict()
        seen2 = dict()

        # add all 8 possible vectors around neighbor
        adj_directions = list(filterfalse(lambda x: x == (0, 0), product([-1, 0, 1], repeat=2)))

        def neighbors(x, y, seen):
            # get neighbor coords from adding vectors to passed coord
            direction_coords = [(a + p, b + q) for (a, b), (p, q) in product([(x, y)], adj_directions)]
            # filter for validity, if open, and if already seen
            return ((a, b) for a, b in direction_coords
                    if 0 <= a < n
                    and 0 <= b < n
                    and grid[a][b] == 0
                    and (a, b) not in seen)

        startq = deque([(0, 0, 1)])
        endq = deque([(n - 1, n - 1, 1)])
        seen1[(0, 0)] = 1
        seen2[(n - 1, n - 1)] = 1

        while startq and endq:
            i, j, visited1 = startq.popleft()
            u, v, visited2 = endq.popleft()

            for a, b in neighbors(i, j, seen1):
                if (a, b) in seen2:
                    return visited1 + seen2[(a, b)]

                startq.append((a, b, visited1 + 1))
                seen1[(a, b)] = visited1 + 1

            for a, b in neighbors(u, v, seen2):
                if (a, b) in seen1:
                    return visited2 + seen1[(a, b)]

                endq.append((a, b, visited2 + 1))
                seen2[(a, b)] = visited2 + 1
        return -1


asserter(lambda: Solution().shortestPathBinaryMatrix([[0]]), 1)
asserter(lambda: Solution().shortestPathBinaryMatrix([[0, 0], [0, 0]]), 2)
asserter(lambda: Solution().shortestPathBinaryMatrix([[0, 1], [1, 0]]), 2)
asserter(lambda: Solution().shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]), 4)
asserter(lambda: Solution().shortestPathBinaryMatrix([[0, 0, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 0]]), 4)
