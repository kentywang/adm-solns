from collections import defaultdict
from typing import List

"""
simple approach:
Time: O(n *n)
Space: O(n)

We want this approach:
generate_letter_combination_hash_table(strs)
O((c lg c) * n) or O(n) when we know string length is always <=100
type anagram_hash = int
dict[anagram_hash, list[str]] 

"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for w in strs:
            anagrams[''.join(sorted(w))].append(w)

        return list(v for v in anagrams.values())
