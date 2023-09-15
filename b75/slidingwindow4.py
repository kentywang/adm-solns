from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        T: O(n + m)
        S: O(1)
        """
        tcount = Counter(t)
        scount = Counter(s)

        def valid(win):
            """
            O(26 * 2) = O(1)
            """
            for char in tcount:
                if win[char] < tcount[char]:
                    return False
            return True

        # basic validation that our strings as valid for the subsequent steps
        if not valid(scount):
            return ''

        window = defaultdict(lambda: 0)
        i = 0
        j = 0

        # initializing window
        while not valid(window):
            window[s[j]] += 1
            j += 1

        min_window = i, j

        # shrinking window from left
        while j < len(s) or window[s[i]] >= tcount[s[i]]:
            if window[s[i]] <= tcount[s[i]]:
                # growing the window on the right until we find a replacement for the left side
                while j < len(s) and s[j] != s[i]:
                    window[s[j]] += 1
                    j += 1

                # now contract the left
                if j < len(s):
                    window[s[j]] += 1
                    j += 1
                else:
                    break

            window[s[i]] -= 1
            i += 1

            if j - i < min_window[1] - min_window[0]:
                min_window = i, j

        return s[min_window[0]: min_window[1]]


x = Solution().minWindow('ADOBECODEBANC', 'ABC')
print(x)
