# 79. Word Search
from typing import List

from util import asserter

"""
Time: O(wmn) (upper limit worst case where each starting is potential word until the last character is reached)
Space: O(w^2) (max hash set size is w, stack height max is w, each hash set underneath is w-1, w-2, ..., 3, 2, 1) 
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])
        word_length = len(word)

        def dfs(y, x, i, been):
            if i == word_length:
                return True
            # close off branches that go to previous visited or nonexistent cells
            if (y, x) not in been and 0 <= y < height and 0 <= x < width:
                if board[y][x] == word[i]:
                    return any([
                        dfs(y + 1, x, i + 1, been | {(y, x)}),
                        dfs(y, x + 1, i + 1, been | {(y, x)}),
                        dfs(y - 1, x, i + 1, been | {(y, x)}),
                        dfs(y, x - 1, i + 1, been | {(y, x)}),
                    ])

        # first, check that the full set of chars in the word are present in the matrix
        hashtbl = {}  # alternatively: just do hashtbl = Counter(word)
        for c in word:
            if c in hashtbl:
                hashtbl[c] += 1
            else:
                hashtbl[c] = 1

        for row in board:
            for c in row:
                if c in hashtbl:
                    hashtbl[c] -= 1

        for c in hashtbl:
            if hashtbl[c] > 0:
                return False  # some char(s) in word is not on board

        # now do the actual work
        return any(dfs(i, j, 0, set()) for i in range(height) for j in range(width))


asserter(lambda: Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"), True)
asserter(lambda: Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"), True)
