"""
T: O(n)
S: O(n) (imba) O(lg n) (balanced)
A: One timer!
"""


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lbound, rbound):
            if not node:
                return True

            if not lbound < node.val < rbound:
                return False

            return dfs(node.left, lbound, node.val) and dfs(node.right, node.val, rbound)

        return dfs(root, -2 ** 31 - 1, 2 ** 31)
