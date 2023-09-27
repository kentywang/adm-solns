"""
8:24
Observations:
- deleting a character means moving the pointer forward/back
- it means two branching calls to check scenario where either side's character is deleted

abca
 ^^

Unusual cases:
- 'abca' -> True
- 'bbx' -> True
- 'xbb' -> True
- 'xb' -> True

Usual cases:
- 'aba'
- 'a'
- 'bb'
- 'acd' -> False


Option 1:

#1. start and end indices
#2. go into subfunction call isPalindrome(i, j, used_delete)
#3. if mismatch encounteder, call's return is either isPalindrome(i, j+1, True) or isPalindrome(i+1, j, True)
#4. if another mismatch encountered in recursive call, since used_delete is True, we can't delete again, return False

Time: O(n)
Space: O(1)

Planning: 12min

8:36
Coding: 11min
8:47

One timer!
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(i, j, used_delete):
            while i <= j:
                if s[i] != s[j]:
                    if used_delete:
                        return False
                    return isPalindrome(i + 1, j, True) or isPalindrome(i, j - 1, True)
                i += 1
                j -= 1
            return True

        return isPalindrome(0, len(s) - 1, False)


# --------------------------------------

"""
20:58 - 21:10 (12m)

    rabcecar
       ^
         ^
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return palindrome(i + 1, j) or palindrome(i, j - 1)
            i += 1
            j -= 1
        return True
