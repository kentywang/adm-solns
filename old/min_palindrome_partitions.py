from math import inf

# Min palindrome partitions

# 9:07 - 9:14, 9:16 memo
def partition_v1(s):
    n = len(s)
    memo = {}

    def go(i, j):
        if (i, j) in memo: return memo[(i, j)]
        if i == j: return 0
        if i+1 == j: return 0 if s[i] == s[j] else 1
        if go(i+1, j-1) == 0 and s[i] == s[j]: return 0
        memo[(i, j)] = 1 + min(go(i, j-1), go(i+1, j))
        return memo[(i, j)]

    return go(0, n-1)

# 9:56
def partition_v2(s):
    n = len(s)
    r = range(n)
    dp = [[inf for _ in r] for _ in r]

    for i in reversed(range(n)):
        for j in range(i, n):

            if i == j:
                dp[i][i] = 0  # seed/base cases
            elif i + 1 < len(s) and i + 1 == j and s[i] == s[j]:
                dp[i][j] = 0

            elif all([  # special case
                i + 1 < len(s),
                j - 1 >= 0,
                s[i] == s[j],
                dp[i + 1][j - 1] == 0
            ]):
                dp[i][j] = 0

            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i + 1][j])  # reducing formula

    # print(dp)
    return dp[0][n - 1]


assert partition_v2('abdbca') == 3
assert partition_v2('cddpd') == 2
assert partition_v2('pqr') == 2
assert partition_v2('ppp') == 0
assert partition_v2('pp') == 0
assert partition_v2('p') == 0
