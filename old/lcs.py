# Longest common substring

import time
import functools

class Timer:
    start_time = 0

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, *exc_info):
        print('Time (ms):', time.time() - self.start_time)


def expect(v1, v2):
    if v1 != v2:
        print(f'Failed, {v1} doesn’t match expected {v2}')

"""
Longest Common Substring

best time complexity is theoretically O(s + t)
"""
# 10:00 ~ 12:00 DFS, recursive, top-down, memo
def lcs(s, t):
    @functools.lru_cache(maxsize=None)
    def go(i, j, ct):
        """
        ct means longest seen til indices i, j

        O(3^(s+t)) time, O(s + t) space
        """
        if i == len(s) or j == len(t): return ct  # base case
        ct = go(i+1, j+1, ct+1) if s[i] == t[j] else ct  # early termination case
        return max(ct, go(i+1, j, 0), go(i, j+1, 0))  # problem reduction

    return go(0, 0, 0)

# 9:45 bottoms-up, grid
# 10:21 finish
def lcs2(s, t):
    """
    each cell represents lcs starting at s[i], s[j]

    O(st) time, O(st) space

    If we only stored in cells if characters match at index[i][j], we
    wouldn't be able to track multiple chains as we were summing it up
    to compare and determine which is the longest.

      abca
    b 0100
    c 0010
    a 1001
    b 0100
    c 0010

      abca
    b 0100
    c 0020
    a 1003
    b 0200
    c 0030
    """
    range_s = range(len(s))
    range_t = range(len(t))

    dp = [[0 for _ in range_t] for _ in range_s]
    longest = 0

    for i in range_s:
        for j in range_t:
            if s[i] == t[j]:
                if i - 1 >= 0 and j - 1 >= 0:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 1
                longest = max(longest, dp[i][j])

    # print(dp)
    return longest

# 10:21 - 10:37
def lcs3(s, t):
    """
    O(st) time, O(min(s, t)) space
    """
    shorter, longer = (s, t) if len(s) < len(t) else (t, s)
    range_shorter = range(len(shorter))
    range_longer = range(len(longer))

    dp = [0 for _ in range_shorter]
    longest = 0

    for i in range_longer:
        for j in reversed(range_shorter):
            if longer[i] == shorter[j]:
                dp[j] = dp[j - 1] + 1 if i - 1 >= 0 else 1
                longest = max(longest, dp[j])
            else:
                dp[j] = 0

    # print(dp)
    return longest


with Timer():
    expect(lcs('zxcv', 'zxcv'), 4)
    expect(lcs('zxcv', 'zxcvk'), 4)
    expect(lcs('i love beautiful chipmunks who fly', 'corgis are just chips in disguise'), 5)
    expect(lcs('abdca', 'cbda'), 2)
    expect(lcs('passport', 'ppsspt'), 3)
    expect(lcs('axbxcxd', 'abcd'), 1)

with Timer():
    expect(lcs2('zxcv', 'zxcv'), 4)
    expect(lcs2('zxcv', 'zxcvk'), 4)
    expect(lcs2('i love beautiful chipmunks who fly', 'corgis are just chips in disguise'), 5)
    expect(lcs2('abdca', 'cbda'), 2)
    expect(lcs2('passport', 'ppsspt'), 3)
    expect(lcs2('axbxcxd', 'abcd'), 1)

with Timer():
    expect(lcs3('zxcv', 'zxcv'), 4)
    expect(lcs3('zxcv', 'zxcvk'), 4)
    expect(lcs3('i love beautiful chipmunks who fly', 'corgis are just chips in disguise'), 5)
    expect(lcs3('abdca', 'cbda'), 2)
    expect(lcs3('passport', 'ppsspt'), 3)
    expect(lcs3('axbxcxd', 'abcd'), 1)
