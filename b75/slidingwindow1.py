# 121. Best Time to Buy and Sell Stock

"""
Brute force: Find all pairs of dates and calculate the difference of prices between first and second date. Choose
the positive max of the differences.

Time: O(n^2)
Space: O(1) (we can just keep the previous highest price diff as iterate through all pairs)

Optimal:

Time: O(n)
Space: O(1)

Uber elegant. I like it.
"""
from util import asserter


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        best_profit = 0
        lowest = prices[0]

        for p in prices:
            lowest = min(p, lowest)
            best_profit = max(best_profit, p - lowest)

        return best_profit


asserter(lambda: Solution().maxProfit([1, 5, 0, 1]), 4)
