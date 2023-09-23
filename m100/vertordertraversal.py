from collections import deque
from itertools import chain
from typing import Optional, List

"""
18:03 - 17:02 (59m)

offset              -1  0   1   2
adj offest          0   1   2   3

                        3
                    9       20

                        15,5    7

                    [9][3,15][20][7]

1. find min max offsets [O(n)]
2. use diff to predefine result array size
3. use -1 * min offset to define where to start appending root,
    passing that offset onward to children
    - need to keep track of height per node, ultimately sorting on that
    in conjunction with the offset (aka sorting by x,y coords) 
4. flatten each subarray
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def find_bounds(curr, x, h):
            if not curr:
                return float("inf"), float("-inf"), h  # so they don't count
            lmin, lmax, lh = find_bounds(curr.left, x - 1, h + 1)
            rmin, rmax, rh = find_bounds(curr.right, x + 1, h + 1)
            return min(x, lmin, rmin), max(x, lmax, rmax), max(lh, rh)

        treemin, treemax, height = find_bounds(root, 0, 0)
        res = [[[] for _ in range(height)] for _ in range(treemax - treemin + 1)]
        q = deque([(root, -1 * treemin, 0)])

        while q:
            curr, x, y = q.popleft()
            if curr:
                res[x][y].append(curr.val)

                q.append((curr.left, x - 1, y + 1))
                q.append((curr.right, x + 1, y + 1))

        for i, col in enumerate(res):
            for coord in col:
                coord.sort()
            res[i] = list(chain.from_iterable(col))

        return res


print(Solution().verticalTraversal(TreeNode(1, left=TreeNode(2))))
