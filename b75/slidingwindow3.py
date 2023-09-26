from collections import defaultdict

"""
Time: O(n)
Space: 
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


print(Solution().characterReplacement("ABAB", 2))
print(Solution().characterReplacement("ABCDE", 1))
print(Solution().characterReplacement("AABABBA", 1))
print(Solution().characterReplacement("ABBB", 2))
