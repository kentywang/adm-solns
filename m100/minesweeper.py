from itertools import product
from typing import List

"""
9:14 - 9:31 (planning, 17m)
- 9:57 (coding, 26m)
- 10:40 (break, debugging, optimizing)

1. if clicked is mine, change to x, record game end
2. click/reveal on empty nonadj -> recurse reveal on 8 neighbors
3. click/reveal on empty adj -> change to digit, no recurse

dfs/bfs to check neighbors. record which ones have been visited to not
infinitely loop
"""


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows = len(board)
        cols = len(board[0])
        directions = list(
            product([-1, 0, 1], repeat=2))  # need to save generator output, else won't have anything on next iter

        def adjcells(i, j):
            # only return adj cell within board bounds, and which arent self
            for x, y in directions:
                if x == y == 0:
                    continue
                if 0 <= i + x < rows and 0 <= j + y < cols:
                    yield (i + x, j + y)

        def reveal(i, j):
            if board[i][j] == 'M':
                board[i][j] = 'X'
                return

            if board[i][j] == 'E':
                adjs = list(adjcells(i, j))  # need to save generator output, else won't have anything on next iter
                mines = sum(1 for x, y in adjs if board[x][y] == 'M')  # O(1)
                if mines:
                    board[i][j] = str(mines)
                else:
                    # no mines, or adj mines, so recurse
                    board[i][j] = 'B'
                    for x, y in adjs:
                        reveal(x, y)

        reveal(click[0], click[1])

        return board


Solution().updateBoard([["E", "E", "E", "E", "E"],
                        ["E", "E", "M", "E", "E"],
                        ["E", "E", "E", "E", "E"],
                        ["E", "E", "E", "E", "E"]], [3, 0])
