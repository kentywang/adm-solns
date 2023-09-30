"""
Planning    8:08 - 8:19
Coding      - 8:36 (28m)

Options:
- traverse full BST with BFS (O(n)), building a ll/arr, then trim to just the interval we want (O(n)), and then sum
- Just need to visit the roots/subroots that enclose the range (so either = or exceeds the range)
    - if within, explore all. recurse and pass curr node's sum to recursive call
    - if equal, no need to explore further. return acc sum including curr node
    - if exceeds, only explore the child side that is closer to the boundary. don't add self to running sum

Time: O(n)
Space: O(n) dfs
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(curr):
            if not curr:
                return 0

            val = curr.val

            # within; explore all
            if low <= val <= high:
                if val != high:
                    val += dfs(curr.right)
                if val != low:
                    val += dfs(curr.left)

                return val

            # exceeds range, explore one side
            if val < low:
                return dfs(curr.right)
            if high < val:
                return dfs(curr.left)

        return dfs(root)

    # ----------------------------------------------[7, 15], curr=32, val=

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(curr):
            if not curr:
                return 0

            val = curr.val
            acc = 0

            # explore if there might be a change a child is in range
            if low < val:
                acc += dfs(curr.left)
            if val < high:
                acc += dfs(curr.right)

            # within; add
            if low <= val <= high:
                acc += val

            return acc

        return dfs(root)


# 12:14 - 12:54 (40m, interrupted)
# Time: O(n)
# Space: O(h)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        acc = 0

        def dfs(curr):
            nonlocal acc

            if not curr:
                return

            if low <= curr.val <= high:
                acc += curr.val

            if curr.val < high:
                dfs(curr.right)

            if low < curr.val:
                dfs(curr.left)

        dfs(root)
        return acc


# 12:58 - 13:24 (Morris, O(1) space)
# Time: O(n)
# Space: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        acc = 0
        curr = root
        while curr:
            if low < curr.val and curr.left:
                pre = curr.left
                while pre.right and pre.right != curr:
                    pre = pre.right

                if pre.right:  # we set this before, so remove it now
                    pre.right = None
                else:
                    pre.right = curr
                    curr = curr.left
                    continue

            if low <= curr.val <= high:
                acc += curr.val
            if curr.val < high:
                curr = curr.right
            else:
                break

        return acc
