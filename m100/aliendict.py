"""
Coding: 12:28 - 13:42 (74m)
Verdict: lots of edge cases.

Observations:
- n^2 pair of words
- each first word in pair must be lexicographically less (or equal?) than second
- we can compare charwise to establish letter order
    - if same char, no new info
    - can only compare up to length of shorter word
    - for each diff, add to letters adjacency list [O(26+25+...+2+1) space for valid adjlist, O(26^2) for worst case invalid]
    - we can only derive one useful comparison from a pair of words

Time: O(k*n^2) adjlist building, then O(1) once adjlist exists to attempt topological sort

"""
from collections import deque
from itertools import combinations, zip_longest
from typing import List

from util import asserter


class CyclicException(Exception):
    pass


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {}

        # can't derive order from just 1 word, return their chars
        if len(words) == 1:
            return ''.join(set(words[0]))

        for word_pair in combinations(words, 2):  # ordered lexicographically

            # we can only derive one useful comparison from a pair of words
            diff_found = False

            for char_a, char_b in zip_longest(*word_pair):

                # we need to put any char we encounter in our adjlist (hence zip_longest)
                if char_a and char_a not in adj:
                    adj[char_a] = set()
                if char_b and char_b not in adj:
                    adj[char_b] = set()

                    # terminate early, can't have longer string preceding a shorter one when all their chars match
                if char_a and not char_b and not diff_found:
                    return ''

                if (
                        not diff_found
                        and char_a
                        and char_b
                        and char_a != char_b
                ):
                    adj[char_a].add(char_b)
                    diff_found = True

        # Topological sort
        order = deque([])
        visited = set()
        visiting = set()

        def dfs(v):
            if v in visited:
                return  # just a subchain we've already explored, no-op
            
            if v in visiting:
                raise CyclicException  # cyclical since we retraversed an ongoing chain

            visiting.add(v)

            if v in adj:
                for cxn in adj[v]:
                    dfs(cxn)

            order.appendleft(v)
            visiting.remove(v)
            visited.add(v)

        try:
            for cxn in adj:
                dfs(cxn)
        except CyclicException:
            return ""

        return ''.join(order)


asserter(lambda: Solution().alienOrder(["wrt", "wrf", "er", "ett", "rftt"]), 'wertf')
asserter(lambda: Solution().alienOrder(["z", "x", "z"]), '')
