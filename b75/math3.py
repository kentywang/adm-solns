# 73. Set Matrix Zeroes
from typing import List

from util import asserter

"""
Iterate thru matrix, and identify the row and column indices that will be zeroed. Then in another pass, apply those 0s.

Time: O(mn)
Space: O(m + n)

Not the optimal solution though. That involves storing intermediate data within the array (along with one other var), I believe.
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0


def foo(mat):
    Solution().setZeroes(mat)
    return mat


asserter(lambda: foo([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]), [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])
