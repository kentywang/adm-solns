# 695. Max Area of Island

"""
Array traversal approach:
Time: O(mn + mn) one full pass over matrix, within which we do a dfs traversal over each 1-value
cell, tracking if it's been seen before. If not, after top level dfs we increment a groups counter.
Space: O(mn)

DSU:
Time: O(mn α(mn))
Space: O(mn)
"""
from collections import defaultdict
from itertools import product
from typing import List

from util import asserter


class DSU:
    def __init__(self):
        self.roots = {}
        self.ranks = defaultdict(lambda: 1)

    def union(self, a, b):
        r1, r2 = self.find(a), self.find(b)
        # r1, r2 are now roots for a, b respectively

        if r1 == r2:
            return

        # weighed union
        if self.ranks[r1] > self.ranks[r2]:
            self.roots[r2] = r1  # smaller tree attaches to larger's root
            self.ranks[r1] += self.ranks[r2]
        else:
            self.roots[r1] = r2
            self.ranks[r2] += self.ranks[r1]

    def find(self, c):
        # wish we could use defaultdict for this, but alas
        if c not in self.roots:
            self.roots[c] = c

        i = self.roots[c]

        while i != self.roots[i]:
            # path compression
            self.roots[i] = self.roots[self.roots[i]]
            i = self.roots[i]

        # found the root when root's root is root
        return i


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        l = len(grid)
        w = len(grid[0])

        dsu = DSU()
        been = set()  # avoids double counting

        def valid_land_adjs(m, n):
            neighbors = [(m - 1, n), (m, n + 1), (m + 1, n), (m, n - 1)]
            return ((x, y) for x, y in neighbors if 0 <= x < l and 0 <= y < w and grid[x][y] and (x, y) not in been)

        for i, j in product(range(l), range(w)):
            if grid[i][j]:
                been.add((i, j))

                adjs = list(valid_land_adjs(i, j))

                if adjs:
                    for a, b in product([(i, j)], adjs):
                        dsu.union(a, b)

                else:  # 1 cell island, manual step
                    dsu.roots[(i, j)] = (i, j)
                    _ = dsu.ranks[(i, j)]

        return max(list(dsu.ranks.values()) + [0])


asserter(lambda: Solution().maxAreaOfIsland(
    [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
), 6)
