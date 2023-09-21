from itertools import product
from typing import List

"""
10:13 - 10:37 (my soln)
- 10:41 (2nd simpler soln, after hint) (4m)
"""


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        Time: O(nm)
        Space: O(1)
        """
        n = len(matrix)
        m = len(matrix[0])

        def diagonal(i, j):
            while i < n and j < m:
                yield matrix[i][j]
                i += 1
                j += 1

        firstColDiagSame = all(
            diag == row[0] for rowIdx, row in enumerate(matrix) for diag in diagonal(rowIdx, 0)
        )

        if firstColDiagSame:
            firstRowDiagSame = all(
                diag == matrix[0][colIdx] for colIdx, _ in enumerate(matrix[0]) for diag in diagonal(0, colIdx)
            )

            return firstRowDiagSame

        return False

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        Time: O(nm)
        Space: O(1)
        """
        n = len(matrix)
        m = len(matrix[0])

        return all(
            matrix[i][j] == matrix[i - 1][j - 1]
            for i, j in product(range(n), range(m))
            if i - 1 >= 0 and j - 1 >= 0
        )


print(Solution().isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
