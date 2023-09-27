from collections import deque

"""
Observations:
                            3
                        9       8
                    4       01      7
                X       XX2    5XX      3

   4    9    30      8


elements    1   1   3   3   5   3   3   1   1  
offset      -4  -3  -2  -1  0   1   2   3   4
index       0   1   2   3   4   5   6   7   8

                            3
                        3       3
                    3
                3
                -3  -2  -1  0   1
                0   1   2   3   4

Width: 3 + 1 + 1 = 5, but root's column is at index 3 

- If we go down a subtree, we can track our delta wrt original root node
    - left tree => root_offset - 1
    - right tree => root_offset + 1
- These can be used as the indices of a list we append to
- We can calculate length of the result list necessary by finding the leftmost and rightmost and adding 1 in each iteration. The full width is then left + right + 1
- We still need to know the 

Cases:
- no nodes
- unbalanced tree (e.g. a linked list)

Option 1:
#1. calculate width by traversing to ends of tree. Need to know both left and right. Width is right - left + 1
#2. Bootstrap bfs starting offset value by -left to have indices properly aligned
#3. Recurse
#4. No return

Time complexity: O(n + n + n) => O(n)
Space complexit: O(h)

Best theoretical TC: O(n)
BTSC: O(1)

Planning: 20min
Coding: 9min + 37min for fixing (46min)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        leftdist = rightdist = 0

        def dfs_dists(node, offset):
            nonlocal leftdist
            nonlocal rightdist

            if not node:
                leftdist = min(leftdist, offset + 1)
                rightdist = max(rightdist, offset - 1)
                return

            dfs_dists(node.left, offset - 1)
            dfs_dists(node.right, offset + 1)

        dfs_dists(root, 0)
        leftdist = leftdist * -1  # for easier usage

        res = [[] for _ in range(leftdist + rightdist + 1)]

        bfsq = deque([(root, leftdist)])
        while bfsq:
            node, index = bfsq.popleft()

            if node:
                res[index].append(node.val)

                bfsq.append((node.left, index - 1))
                bfsq.append((node.right, index + 1))

        return res

    # 20:40 - 20:54

    def verticalOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        vals = defaultdict(list)

        def bfs(curr, col):
            if curr:
                vals[col].append(curr.val)
                q.append((curr.left, col - 1))
                q.append((curr.right, col + 1))

        q = deque([(root, 0)])
        while q:
            bfs(*q.popleft())

        colVals = vals.items()
        mincolvals = min(colVals)
        res = [[]] * (max(colVals)[0] - mincolvals[0] + 1)

        for col, vals in colVals:
            res[col - mincolvals[0]] = vals

        # online soln just does below, calcing min_column/max_column during the bfs phase
        # return [columnTable[x] for x in range(min_column, max_column + 1)]
        return res
# -------------------------------> move me! (option (⌥) + up/down)
