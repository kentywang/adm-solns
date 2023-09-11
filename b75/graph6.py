# 178 · Graph Valid Tree
from typing import List

from util import asserter

"""
essentially, does a cycle exist?
"""


class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        """
        :param n: An integer
        :param edges: a list of undirected edges
        :return: true if it's a valid tree, or false
        """
        adjlist = {v: set() for v in range(n)}
        for a, b in edges:
            adjlist[a].add(b)
            adjlist[b].add(a)

        # if we checked a node, in a valid tree we'll never see it again
        checked = set()  # to check for cycles.

        def dfs(i, prev=None):
            if i in checked - {prev}:  # prevent counting prev node connection as cycle
                return False  # cycle detected

            checked.add(i)
            return all(dfs(v, i) for v in adjlist[i] if v != prev)

        return dfs(0) and n == len(checked)


asserter(lambda: Solution().valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]), True)
asserter(lambda: Solution().valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]), False)
