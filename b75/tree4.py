# 572. Subtree of Another Tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
My approach: utilized isSameTree from earlier, since that's what we're checking.

ChatGPT estimates:
Time: O(nm)

In the worst case, you will call isSameTree for each node in the root tree, and for each call, you may have to 
traverse the entire subRoot tree to check if it's the same tree. This results in O(m * n) comparisons.

Space: O(max(m, n))

There are faster algorithms that I should look into for this, but I won't do it yet.
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

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSameTree(root, subRoot):
            return True

        # take care of none cases here
        if root is None and subRoot is not None: return False  # no root
        if root is not None and subRoot is None: return True  # no subroot
        if root is None and subRoot is None: return True  # both none

        # Don't need these, because isSubtree will check these as part of their execution
        # return self.isSameTree(root.left, subRoot) or self.isSameTree(root.right, subRoot) or \

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
