# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
18:45 - 20:00   (75m)
One timer

            5
        3       7
    1       4,6     8

    4.5

If tgt is 3
[1, 2, 3, 4, 5]
-3 2 1 0
If tgt is -1
-1 -2

- We want 4, 5 to be considered, then return 4 since smaller
- If ask was 4.6, we'd want only 5 to be considered

O(n)
- Naive: IOT, recursive generator to get next node. We keep curr and prev, keep going
    until diff between target and curr is 0 (return curr), or when diff goes up (return prev). If we run out of nodes, last node is the closest, so return it
    - Cons: wasted traversals down branches we don't care about (e.g if target is all the way in the end)

O(h) : O(h)
- where we'd insert a node in a BST is where the target could be. Between that and a parent
    node are the two values we need to consider. Keep the closest parent node value (compare
    during each dfs, and when base case, compare between parent node and leaf for the closer, and if equidistant, the smaller)

                6
            3       8

                tgt:7

                1
            tgt: -1
"""


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def dfs(curr, closest):
            if not curr:
                return closest

            if curr.val == target:
                return curr.val

            if abs(curr.val - target) < abs(closest - target):
                closest = curr.val
            elif abs(curr.val - target) == abs(closest - target):
                closest = min(curr.val, closest)

            if curr.val > target:
                return dfs(curr.left, closest)
            return dfs(curr.right, closest)

        return dfs(root, root.val)
# ------------------------------------> 1
