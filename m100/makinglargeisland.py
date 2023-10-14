from itertools import product
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dsu(n):
            parent = list(range(n))
            rank = [1] * n

            def find(x):
                while x != parent[x]:
                    parent[x] = parent[parent[x]]  # Path compression
                    x = parent[x]
                return x

            def union(x, y):
                if (a := find(x)) != (b := find(y)):  # union by rank
                    if rank[a] < rank[b]:
                        parent[a] = b
                        rank[b] += rank[a]
                    else:
                        parent[b] = a
                        rank[a] += rank[b]

            return find, union, rank

        n = len(grid)
        find, union, rank = dsu(n ** 2)

        for i, j in product(range(n), repeat=2):
            if grid[i][j]:
                for u, v in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= u < n and 0 <= v < n and grid[u][v]:
                        union(i * n + j, u * n + v)

        m = 0
        for i, j in product(range(n), repeat=2):
            if not grid[i][j]:
                # adjacent elemnts can have the same parent that's why we are using set
                t = set()
                c = 1
                for u, v in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= u < n and 0 <= v < n and grid[u][v]:
                        t.add(find(u * n + v))
                for x in t:
                    c += rank[x]
                if c > m:
                    m = c

        for i in range(n * n):
            m = max(m, rank[find(i)])
        return m
