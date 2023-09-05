# 20. Valid Parentheses
from util import asserter


class Solution:
    """
    Time: O(n)
    Space: O(n)

    Verdict: Not as elegant as I expected this algo to be able to become. Needed to add in checks against both unbalanced to the opens
    and unbalanced to the closeds.
    """

    def isValid(self, s: str) -> bool:
        stack = []
        for t in s:
            if is_open_parens_type(t):
                stack.append(t)
            else:
                if not stack:
                    return False  # because unbalanced (more closeds)

                top = stack.pop()
                if parens_type(top) != parens_type(t):
                    return False  # because interleaved paren types is invalid

        if stack:
            return False  # because unbalanced (more opens)

        # empty stack, so balanced
        return True


def is_open_parens_type(x):
    return x == '(' or x == '{' or x == '['


def parens_type(x):
    if x == '(' or x == ')':
        return 'PARENS'
    if x == '{' or x == '}':
        return 'BRACES'
    if x == '[' or x == ']':
        return 'BRACKETS'


asserter(lambda: Solution().isValid('()'), True)
asserter(lambda: Solution().isValid('(){}[]'), True)
asserter(lambda: Solution().isValid('(())'), True)
asserter(lambda: Solution().isValid('(()())'), True)
asserter(lambda: Solution().isValid('[)'), False)
