# 54. Spiral Matrix
from typing import List

from util import asserter

"""
Time: O(mn)
Space: O(mn) (for return array)

Verdict: Pretty easy, actually.
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        res = []

        while left <= right:
            # traverse top
            res += [matrix[top][i] for i in range(left, right + 1)]
            top += 1

            if top > bottom:
                break

            # traverse right
            res += [matrix[i][right] for i in range(top, bottom + 1)]
            right -= 1

            if left > right:
                break

            # reverse traverse bottom
            res += [matrix[bottom][i] for i in range(right, left - 1, -1)]
            bottom -= 1

            if top > bottom:
                break

            # reverse traverse left
            res += [matrix[i][left] for i in range(bottom, top - 1, -1)]
            left += 1

        return res


asserter(lambda: Solution().spiralOrder([[1]]), [1])
asserter(lambda: Solution().spiralOrder([[1, 2]]), [1, 2])
asserter(lambda: Solution().spiralOrder([[1], [2]]), [1, 2])
asserter(lambda: Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]),
         [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
