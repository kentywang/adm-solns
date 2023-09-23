"""
Planning    14:10 - 14:19 (9m)
Coding      14:21 - 14:31 (10m)

0 node -> 0
1 node -> that node

    2
3               yields [2,3]

        2       yields [2,4,5]
    3       4
      5

      [2,3,4,null,5,null,null]
lvl1   ^
lvl2     ^ ^
lvl3          ^   ^  ^    ^

Plan 1:
- Build IOT array of node values
- for each level in BT as repr by array, get the rightmost value
- Time O(n), space O(n)

Plan 2:
- BFS
- Time: O(n) space O(n/2)

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    """
        2       yields [2,4,5]
    3       4
      5

    """

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([(root, 0)])
        res = []

        while q:
            node, lvl = q.popleft()

            if lvl == len(res):
                # this is the first time we're at this lvl, so array needs expanding
                res.append(node.val)
            else:  # we're overwriting an existent value on this level with a righter one
                res[lvl] = node.val

            if node.left:
                q.append((node.left, lvl + 1))
            if node.right:
                q.append((node.right, lvl + 1))

        return res

# ----------------------------------------------------
