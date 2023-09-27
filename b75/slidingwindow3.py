from collections import defaultdict

"""
Time: O(n)
Space: O(1
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(lambda: 0)
        getMostCommon = lambda: max(window.items(), key=lambda x: x[1])

        i = 0
        best = 0

        # keep j steadily moving forward. increment i as needed to shrink
        # window
        for j in range(len(s)):
            window[s[j]] += 1

            most_common_letter, count = getMostCommon()
            # 1 + j + i is the window size
            while 1 + j - i - count > k:
                # decr removed letter's count
                window[s[i]] = max(0, window[s[i]] - 1)
                most_common_letter, count = getMostCommon()
                i += 1

            # we now are within k ops, so our window is valid
            best = max(1 + j - i, best)

        return best

    """
    Online soln
    - Optimizes using knowledge that right pointer's letter incrementing means it's the only one that can become
    the most freq character at any moment.
    - Similarly, we don't need a nested while loop since we know we'll always remove a letter that's not the most 
    common when we do the check "(r - l + 1) - maxf > k"
    - Finally, we don't need to save the best, since our window doesn't need to be 1:1 with our valid substring. The
    longest valid substring could've been in the past, but our window (dist b/w j and i) still stays its expanded size 
    even when we encounter prolonged sequences of characters not the same as our most common. This is kinda hard to
    wrap my head around. 
    """

    def characterReplacementOnline(self, s: str, k: int) -> int:
        count = {}

        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

        return (r - l + 1)


print(Solution().characterReplacement("ABAB", 2))
print(Solution().characterReplacement("ABCDE", 1))
print(Solution().characterReplacement("AABABBA", 1))
print(Solution().characterReplacement("ABBB", 2))
print(Solution().characterReplacementOnline("AAAAAAAAAAABCDEF", 0))
