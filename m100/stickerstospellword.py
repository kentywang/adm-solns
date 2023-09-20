"""
20:40 - 21:44 (basic plan for solution, 64m)
Fully finished at 22:12 (92m total)

Just a few minor typos/bugs, but it otherwise worked the first time! Wow.

Observations:
- find minimum items that sum to character counts of target

-----------
thehat
t: 2
h: 2
e: 1
a: 1

- with
t: 1
h: 1
e: 1
a: 1

- with
t: 0
h: 0
e: 1
a: 1

- example
all 0s



------------

- calculate character count distribution for target, store in tuple [O(k)]
- calculate distribution for all words [O(nk)]
- √ don't store irrelevant letters
- √ cull less useful words (if its counts are strictly lower than some other word's) [O(n^2)]
- exhaustive search by dfsing, passing in remaining counts to zero out and curr min (memoize on that)
- within dfs, if word doesn't lower any counts, abandon that path
- O(n^n) time yikes
- O(n^n) space too?
"""
from functools import cache
from itertools import combinations
from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:

        # calc tgt letter counts
        letterToIdx = {}  # use for mapping letter to index
        idx = 0
        for ch in target:
            if ch not in letterToIdx:
                letterToIdx[ch] = idx
                idx += 1

        # create tuple to represent counts
        tgt_tup = [0] * len(letterToIdx)
        for ch in target:
            tgt_tup[letterToIdx[ch]] += 1
        tgt_tup = tuple(tgt_tup)

        # calc sticker letter counts by word, store in set
        stickerset = set()
        for s in stickers:
            tup = [0] * len(letterToIdx)
            for ch in s:
                if ch in letterToIdx:  # store only tgt chars
                    tup[letterToIdx[ch]] += 1
            stickerset.add(tuple(tup))

        # cull worse stickers
        remove = set()
        for tup1, tup2 in combinations(stickerset, 2):
            # letterwise compare
            if all(a >= b for a, b in zip(tup1, tup2)):
                remove.add(tup2)
        stickerset -= remove

        @cache
        def dfs(rem_cts, best):
            # base case: when we have met all letter requirements
            if not any(rem_cts):
                return best

            lowest = float("inf")  # handles "solution" DNE case
            for st in stickerset:
                updated = tuple(max(t2 - t1, 0) for t1, t2 in zip(st, rem_cts))
                # don't dfs down this path with this sticker any further
                # since we've exhausted its usefulness
                if updated == rem_cts:
                    continue

                recur_soln = dfs(updated, best + 1)
                lowest = min(lowest, recur_soln)

            return lowest

        ans = dfs(tgt_tup, 0)
        return -1 if ans == float("inf") else ans


print(Solution().minStickers(["with", "example", "science"], "thehat"))
