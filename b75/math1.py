# 48. Rotate Image
from typing import List

from util import asserter

"""
Time: O(n^2) (n * n/2)
Space: O(1)

Verdict: Always scared of this prob, but it turns out to be simpler than expected.
"""


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        start = 0
        end = n - 1

        while start < end:
            for i in range(end - start):
                a = matrix[start][start + i]
                b = matrix[start + i][end]
                c = matrix[end][end - i]
                d = matrix[end - i][start]

                # do the rotation within the variables
                a, b, c, d = d, a, b, c

                # reunion
                matrix[start][start + i] = a
                matrix[start + i][end] = b
                matrix[end][end - i] = c
                matrix[end - i][start] = d

            # finished rotating one layer, do the next inner layer
            start += 1
            end -= 1


def throwaway(mat):
    Solution().rotate(mat)
    return mat


asserter(lambda: throwaway([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]]),
         [[7, 4, 1],
          [8, 5, 2],
          [9, 6, 3]])

asserter(lambda: throwaway([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]),
         [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])
