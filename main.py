from profiler import profile


@profile
def partition(s):
    """
    chip
    :param s:
    :return:
    """
    from math import inf

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


def main():
    assert partition('abdbca') == 3
    assert partition('cddpd') == 2
    assert partition('pqr') == 2
    assert partition('ppp') == 0
    assert partition('pp') == 0
    assert partition('p') == 0


if __name__ == '__main__':
    main()
