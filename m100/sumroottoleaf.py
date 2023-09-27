# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

"""
21:21 - 21:58 (37m, deceptively tricky, need to watch out for double counting)

Plan: parent passes self down. Child mults parent's val by 10 before adding to self and passing down. Leaf accumulates sum in a global variable.

Time: O(n)
Space: O(h)

            4
        9       0
    5       1
"""


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(curr, acc):
            nonlocal res

            num = 10 * acc + curr.val

            if not curr.left and not curr.right:
                res += num
            else:
                if curr.left:
                    dfs(curr.left, num)
                if curr.right:
                    dfs(curr.right, num)

        dfs(root, 0)

        return res


print(Solution().sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3))))
