# 417. Pacific Atlantic Water Flow
from itertools import product, chain
from typing import List

from util import asserter

coord = tuple[int, int]

"""
Graph direction goes from low height to high, because we can easily mark each node traversed as flowing, rather than
have to possibly discard nodes if it was the other way around.

Time: O(mn)
Space: O(mn)

Verdict: Was hard for me. I thought I had it in the bag, but then realized I didn't account for water flow that wasn't
the straight to the shores (i.e. we could have spiral water flow). At least I (re)learned a bunch about generators, iterators,
and iterables. 
"""


class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        height = len(heights)
        width = len(heights[0])

        pacifics: set[coord] = set()
        atlantics: set[coord] = set()

        flows: dict[coord, set[coord]] = {}

        def graph():
            """
            Time: O(mn)
            Space: O(mn) (max 4 edges per node means linear to node count, i.e. mn)
            """
            for i in range(height):
                for j in range(width):
                    flows[(i, j)] = set(
                        (y, x) for y, x in adjs(i, j) if heights[i][j] <= heights[y][x])  # not dfs, so no loop

        def adjs(i, j):
            coords = []
            if i > 0:
                coords.append((i - 1, j))
            if i < height - 1:
                coords.append((i + 1, j))
            if j > 0:
                coords.append((i, j - 1))
            if j < width - 1:
                coords.append((i, j + 1))
            return coords

        def mark_shore(is_pacific):
            """
            Time: O(m + n)
            """
            if is_pacific:
                top = product([0], range(width))
                left = product(range(1, height), [0])
                pacifics.update(chain(top, left))

            bot = product([height - 1], range(width))
            right = product(range(height - 1), [width - 1])
            atlantics.update(chain(bot, right))

        def find_flows(ocean):
            """
            Time: O(mn) since we don't allow repetitions
            """
            been = set()

            def dfs(yx):
                if yx in been:
                    return
                been.add(yx)

                for kl in flows[yx]:
                    dfs(kl)

            for ij in ocean:
                dfs(ij)

            ocean.update(been)

        graph()

        mark_shore(True)
        mark_shore(False)

        find_flows(pacifics)
        find_flows(atlantics)

        return [[y, x] for y, x in (pacifics & atlantics)]


asserter(lambda: sorted(Solution().pacificAtlantic([
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]])), sorted([[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]))

x = Solution().pacificAtlantic([[1, 1], [1, 1], [1, 1]])
print('done')
