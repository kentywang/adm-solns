# 133. Clone Graph
from itertools import product
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Time: O(n)
        Space: O(n)

        Wow, this one became very elegant, but it took a while to realize to what I didn't
        actually need.
        """
        nodes = {}
        if not node:
            return None

        # a memo cache wouldn't work here because we eventually make recursive calls of f(x) within f(x) (as opposed to
        # fibonacci where we do calls of f(x-1) within f(x)
        def dfs(curr):
            if curr.val in nodes:
                return nodes[curr.val]

            res = Node(curr.val)
            nodes[curr.val] = res

            # fan out
            for curr_node, neighbor in product([curr], curr.neighbors):
                neighbor_clone = dfs(neighbor)
                res.neighbors += [neighbor_clone]

            return res

        return dfs(node)


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.neighbors = [n2, n3]
n2.neighbors = [n1, n3]
n3.neighbors = [n1, n2]

x = Solution().cloneGraph(n1)
print('done')
