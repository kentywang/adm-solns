from util import asserter

"""
Brute force: find longest balanced in current orientation. Then rotate string, try again.
Rotate until all orientations tried. Return the longest of the longest.

O(n) for each orientation
n orientations

Time: O(n^2)
Space: O(n)
"""


def longest_balanced(parens: str) -> int:
    longest = 0

    # abcabc
    # abc
    #  bca
    #   cab

    extended_parens = parens + parens
    for i, _ in enumerate(extended_parens):
        longest = max(longest, longest_balanced_inner(extended_parens[i: i + len(parens)]))

    return longest


def longest_balanced_inner(parens: str) -> int:
    """
    If first char is a closing paren, returns 0.
    Otherwise, returns longest balanced parens starting on the first character.
    """
    stack = []
    curr = 0
    for i, p in enumerate(parens):
        if p == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
                if len(stack) == 0:
                    # we finished balancing a set of parens, so record this as the high water mark
                    curr = i + 1
            else:
                return max(0, curr)  # no longer unbalanced

    if stack:
        # something leftover on stack, so not balanced
        # return the high water mark
        return max(0, curr)

    return curr


asserter(lambda: longest_balanced_inner(")()"), 0)
asserter(lambda: longest_balanced_inner("()"), 2)
asserter(lambda: longest_balanced_inner("(())("), 4)
asserter(lambda: longest_balanced_inner("()()("), 4)

asserter(lambda: longest_balanced(")()(())()()))())))("), 12)
asserter(lambda: longest_balanced("(()"), 2)
asserter(lambda: longest_balanced(")("), 2)
asserter(lambda: longest_balanced("))"), 0)
asserter(lambda: longest_balanced(")))((("), 6)
asserter(lambda: longest_balanced("))()((("), 6)

#   For O(n) solution, I tried:
#     Double the string to capture the rotation/wrap, then do 1 pass over the double-length string to find
#     the longest continuous balanced piece.
#     But this fails on cases like () or ())(
