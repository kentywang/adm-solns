# 39. Combination Sum
from typing import List

"""
For each distinct value, branch through the possible next values until reaching the target.
Backtrack happens automatically by discontinuing recursion down a branch.
The sorted candidates list means we can ignore earlier branching into smaller integers than the integer we start from,
saving us from having to dedupe.

Time: O( len(candidates)^(target / min(candidates)) )
Space: O( target / min(candidates) )
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # We assume candidates is sorted.
        res = []
        length = len(candidates)

        def branch(acc, total, starting_idx):
            if total == target:
                res.append(acc)
            elif total < target:
                for i in range(starting_idx, length):
                    c = candidates[i]
                    branch(acc + [c], total + c, i)

        for i, c in enumerate(candidates):
            branch([c], c, i)

        return res


print(Solution().combinationSum([2, 3, 6, 7], 7))
print(Solution().combinationSum([2, 5, 8], 10))
print(Solution().combinationSum([2], 1))
