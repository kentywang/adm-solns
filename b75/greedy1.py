# 53. Maximum Subarray
from itertools import islice
from typing import List

from util import asserter


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)

        Verdict: Ugly, not proud of this one
        """
        acc = 0  # when disjoint, should be nonnegative; when joint, will be always negative
        curr_max = nums[0]
        disjoint = False

        for num in islice(nums, 1, None):
            merged = (acc + num) if disjoint else (curr_max + acc + num)
            best = max(curr_max, merged, num)
            if curr_max == best:
                if acc >= 0:
                    # the earlier parts of the acc are worth keeping because they are nonnegative
                    # and possibly link to the curr_max
                    acc += num
                else:
                    if disjoint:
                        # discard earlier parts of the acc because they'll lower our max
                        acc = max(num, 0)
                    else:
                        if curr_max + acc < 0:
                            # disjoin since lowers max
                            acc = max(num, 0)
                            disjoint = True
                        else:
                            acc += num
            else:
                # either merged or num is the max
                acc = 0
                curr_max = best
                disjoint = False

        return curr_max

    # Online solution
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        total = 0

        for n in nums:
            total += n
            res = max(res, total)
            total = max(0, total)
        return res


asserter(lambda: Solution().maxSubArray([8, -19, 5, -4, 20]), 21)
asserter(lambda: Solution().maxSubArray([2, -1, 1, 1]), 3)
