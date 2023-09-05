# 226. Invert Binary Tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Time: O(n)
Space: O(h) (h can be n if imba, lg n if balanced)

Verdict: Easier than expected.
"""


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        return root
