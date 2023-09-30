"""
Planning:   20:18 - 20:55   (37m)
Coding:     - 21:03         (8m)
One timer!

Observations:
- a group is where each member share the same letter distance between each char
- all 1-char strings all under the 1-char group
- if the subsequent letter's order is earlier, then keep adding 26 to it until it's later for easy dist calc
    - would lead to more and more adding as we have a longer list, so not efficient.

- regardless of if order difference is positive or negative, modding it by 26 would yield the distance.

Sandbox
------------------
0   25  dist: (0 + 25) % 26 = 25
a   z

b   a   dist: (1 + 25) % 26 = 0
1   0
------------------
a   b   d   a   z   a   dist: [1,2]
0   1   3   26  51  52
            ^   ^   ^
adds of 26: 1   1   2
------------------
a   b   d   a   z   a   dist: [1,2]
0   1   3   0  51  52
            ^   ^   ^
adds of 26: 1   1   2
------------------

Option 1:
- for each string, find the distance in order value between each pair of adjacent elements, apply this formula:
    [order(b) - order(a)] % 26
- check for existence of that sequence in the table (as a hashable tuple as the key), and add the string to its value (an array) if exists, otherwise create a new one
- Time: O(n)
- Space: O(n) (at most a new different hash key for each string)
"""
from collections import defaultdict
from itertools import pairwise
from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strings:
            t = tuple((ord(b) - ord(a)) % 26 for a, b in pairwise(string))
            groups[t].append(string)

        return list(groups.values())


# 10:42 - 10:52
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dists = defaultdict(list)
        for s in strings:
            dist = tuple(
                (ord(c2) - ord(c1)) if ord(c2) > ord(c1) else (ord(c2) - ord(c1) + 26)
                for c1, c2 in pairwise(s)
            )
            dists[dist].append(s)

        return dists.values()
