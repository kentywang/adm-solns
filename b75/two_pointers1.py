# 125. Valid Palindrome
from util import asserter


class Solution:
    """
    Time: O(n)
    Space: O(1)

    Verdict: trickier than usual palindrome question because of ignored non-alphanumerics.
    Kinda strange that I have to do another invariant validation within the while loop.
    """

    def isPalindrome(self, s: str) -> bool:
        l = len(s)

        left = 0
        right = l - 1

        while left < right:
            while left < l - 1 and not s[left].isalnum():
                left += 1

            while right > 0 and not s[right].isalnum():
                right -= 1

            if left < right and s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


asserter(lambda: Solution().isPalindrome('racecar'), True)
asserter(lambda: Solution().isPalindrome(':r:'), True)
asserter(lambda: Solution().isPalindrome(':ar:'), False)
asserter(lambda: Solution().isPalindrome('h:a:ah'), True)
asserter(lambda: Solution().isPalindrome('h:ab:ah'), True)
asserter(lambda: Solution().isPalindrome('h:axa:ah'), False)
asserter(lambda: Solution().isPalindrome('::'), True)
asserter(lambda: Solution().isPalindrome('.,'), True)
