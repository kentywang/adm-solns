# 242. Valid Anagram

class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def isAnagram(self, s: str, t: str) -> bool:
        letter_set = {}

        if len(s) != len(t):
            return False

        for c in s:
            if c in letter_set:
                letter_set[c] += 1
            else:
                letter_set[c] = 1

        for c in t:
            if c in letter_set:
                if letter_set[c] == 0:
                    return False
                letter_set[c] -= 1
            else:
                return False

        return True
