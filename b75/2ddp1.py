# 62. Unique Paths
from util import asserter


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Time: O(mn)
        Space: O(m,n) but we can reduce to O(min(m,n))
        """
        dp = [[0] * n for _ in range(m)]

        # set 1st row, 1st col 0
        for j in range(n):
            dp[0][j] = 1

        for i in range(m):
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


asserter(lambda: Solution().uniquePaths(3, 7), 28)
