"""
O(n^2) T/S
"""


def num_of_paths_to_dest(n):
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        # number of paths when no movement needed is 1, not 0, according to solns
        dp[i][0] = 1

    for i in range(1, n):
        for j in range(1, i + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

    return dp[n - 1][n - 1]


print(num_of_paths_to_dest(10))
