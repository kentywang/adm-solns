# 100. Same Tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Need to check all nodes.

Time: O(n)
Space: O(h) 
"""


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is not None:  # one none
            return False
        if q is None and p is not None:  # other none
            return False
        if p is None and q is None:  # both none
            return True
        if p.val != q.val:  # both something, but diff
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)  # both something, and same
