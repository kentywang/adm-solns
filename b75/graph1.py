# 200. Number of Islands
from typing import List

from util import asserter


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Time: O(mn) (thanks, memobama)
        Space: O(mn)
        """
        been = set()  # memoizes. only for tracking islands, not water (no necessary)
        islands = 0

        def dfs(y, x, continuation=False):
            if not (0 <= y < len(grid)): return  # OOB
            if not (0 <= x < len(grid[0])): return  # OOB
            if grid[y][x] == '0': return  # water
            if (y, x) in been: return  # already seen

            # ok, this is new territory. Mark it
            been.add((y, x))

            if not continuation:
                # we know it's a new island because if it wasn't,
                # our last non-continuation dfs traverse would have reached it
                nonlocal islands
                islands += 1

            dfs(y - 1, x, True)
            dfs(y, x + 1, True)
            dfs(y + 1, x, True)
            dfs(y, x - 1, True)

        for i, _ in enumerate(grid):
            for j, _ in enumerate(grid[0]):
                dfs(i, j)

        return islands


asserter(lambda: Solution().numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]]), 1)

asserter(lambda: Solution().numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]]), 3)
