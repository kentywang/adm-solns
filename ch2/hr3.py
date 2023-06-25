#!/bin/python3
import sys

from util import asserter

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

mm = [[4, 9, 2],
      [3, 5, 7],
      [8, 1, 6]]


def identity(x):
    return x


def xflip(matrix):
    return [list(reversed(row)) for row in matrix]


def diagflip(matrix):
    width = len(matrix)
    return [[row[w] for row in matrix] for w in range(width)]


def get_3x3_mm_permutations():
    curr = mm
    permutation_ops = [identity, xflip, diagflip, xflip, diagflip, xflip, diagflip, xflip]
    for op in permutation_ops:
        curr = op(curr)
        yield curr


def diff_matrices(m1, m2):
    total = 0
    for m1_row, m2_row in zip(m1, m2):
        for m1_cell, m2_cell in zip(m1_row, m2_row):
            total += abs(m1_cell - m2_cell)
    return total


def formingMagicSquare(s):
    """
    Time: O(1)
    Space: O(1)
    """
    minimum_diff = sys.maxsize
    for mm_perm in get_3x3_mm_permutations():
        minimum_diff = min(diff_matrices(mm_perm, s), minimum_diff)
    return minimum_diff


asserter(lambda: formingMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 5]]), 1)
asserter(lambda: formingMagicSquare([[4, 8, 2], [4, 5, 7], [6, 1, 6]]), 4)
