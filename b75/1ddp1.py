# 70. Climbing Stairs

"""
Without caching, there will be a lot of repeated work.

Time: O(2^n) (inverse of log; see how similar the code looks to log?)
Space: O(n)

Caching should make it:

Time: O(n)
Space: O(n)

DP matrix approach:

Time: O(n)
Space: O(n)

Verdict: Definitely needed a refresher on DP.
"""


class Solution:
    # Top down approach
    def climbStairs(self, n: int) -> int:
        cache = {}

        def ways(steps_left):
            if 0 <= steps_left <= 2:
                return steps_left

            if steps_left not in cache:
                cache[steps_left] = ways(steps_left - 1) + ways(steps_left - 2)
            return cache[steps_left]

        return ways(n)

    # Bottom up approach
    def climbStairsDP(self, n: int) -> int:
        if 0 <= n <= 2:
            return n

        # index i means steps
        ways = [0] * (n + 1)
        ways[0] = 0  # dummy; only used so index number is aligned with n
        ways[1] = 1
        ways[2] = 2

        for i in range(3, len(ways)):
            ways[i] = ways[i - 1] + ways[i - 2]

        return ways[n]


print(Solution().climbStairs(4))
print(Solution().climbStairsDP(4))
