from util import asserter


def isbalanced(parens: str) -> tuple[bool, int | None]:
    stack = []
    for i, p in enumerate(parens):
        if p == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                # nothing left to pop, return index as it's wrong
                return False, i
    if stack:
        # something leftover on stack, so not balanced
        # return the top
        return False, stack[-1]
    return True, None


asserter(lambda: isbalanced("((())())()"), (True, None))
asserter(lambda: isbalanced(")()("), (False, 0))
asserter(lambda: isbalanced("())"), (False, 2))
asserter(lambda: isbalanced("()("), (False, 2))
asserter(lambda: isbalanced("((()"), (False, 1))
