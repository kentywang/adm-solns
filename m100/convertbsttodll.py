"""
17:10 - 17:20   (10m) planning
- 17:15         (15m) coding
-
Simple approach (i.e. don't do 2 things at once)
- IOT to build globally defined array (O(n) : O(h))
- iterate pairwise to connect each node (O(n))
- connect head and tail, then return head
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        5
    3       7
        4
"""
from itertools import pairwise, chain


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        node_list = []

        def in_order_dfs(curr):
            if not curr:
                return

            in_order_dfs(curr.left)
            node_list.append(curr)
            in_order_dfs(curr.right)

        def build_ll():
            for a, b in pairwise(chain(node_list, [node_list[0]])):
                a.right = b
                b.left = a

        in_order_dfs(root)
        build_ll()

        return node_list[0]
# ------------------------------------------  [3-4-5-7]
