"""
18:33 - 18:43 (10m)

        01234
        cbafg

- assign index value to each letter in order
    - make hashmap of letter to index
- sort s according to index [O(n lg n)]
    - letters not in the order list? can be any index
- space: O(len(order))
"""


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {letter: i for i, letter in enumerate(order)}
        return ''.join(
            sorted((letter for letter in s), key=lambda e: d.get(e, -1)))  # some arbitrary default val if not in dict
