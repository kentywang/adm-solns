class Solution:
    """
    T: O(n)
    S: O(n)
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        subset = set()
        best = 0

        while j < len(s):
            while s[j] in subset:
                # contract the left side
                subset.remove(s[i])
                i += 1

            # grow the right side
            subset.add(s[j])
            j += 1

            best = max(best, j - i)  # or len(subset)

        return best
