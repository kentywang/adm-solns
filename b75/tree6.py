from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Cases to consider:
- no nodes -> []
- 1 node -> [[<node>]]
- incomplete (levels not filled) -> skip them [[<2>], [<3>]]
- complete, balanced

Plan:
Best case time: O(n)

- BFS (O(~n/2) space)
  - for each node, we tell it to push its value to the list of result list at given index
  - if it has child(ren), create new list as next element of result list
  - queue the children and their indices

"""


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = [[]]
        queue = deque([(0, root)])

        while queue:
            i, curr = queue.popleft()

            res[i].append(curr.val)

            if curr.right or curr.left:
                # prevents children on same level from initializing next array
                if len(res) - 1 == i:
                    res.append([])  # add new list to represent children's level (i + 1)

                if curr.left:
                    queue.append((i + 1, curr.left))
                if curr.right:
                    queue.append((i + 1, curr.right))

        return res
