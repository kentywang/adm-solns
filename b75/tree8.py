from heapq import heappush, heappop
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Option 1: O(n + k lg n), space O(n)
- heapify O(n)
- pop k elements O(k lg n)

Option 2: O(n) (imba) or O(k lg n), space O(lg n)
- traverse to min element O(lg n) or O(n)
- traverse to next in order successor O(k lg n) or O(1)
"""


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        h = []

        def makeheap(node):
            """
            in order traversal for faster heap inserts
            """
            if node:
                makeheap(node.left)
                heappush(h, node.val)
                makeheap(node.right)

        makeheap(root)

        while k:
            val = heappop(h)
            k -= 1

        return val
