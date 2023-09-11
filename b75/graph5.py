# 3651 · Number of Connected Components in an Undirected Graph
from typing import List

from util import asserter


class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """

    def count_components(self, n: int, edges: List[List[int]]) -> int:

        # O(V)
        adjlist = {v: set() for v in range(n)}

        # O(E)
        for v1, v2 in edges:
            adjlist[v1].add(v2)

        checked = set()
        groups = 0

        def dfs(i):
            if i in checked:
                return

            checked.add(i)

            for v in adjlist[i]:
                dfs(v)

        # O(V + E)
        for v in adjlist:
            if v not in checked:
                dfs(v)
                groups += 1

        return groups


asserter(lambda: Solution().count_components(6, [[0, 1], [1, 2], [2, 3], [4, 5]]), 2)
asserter(lambda: Solution().count_components(3, [[0, 1], [0, 2]]), 1)
