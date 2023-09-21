"""
8:56 - 9:26 (30m)
18:12 - 18:28 (16m)
Planning
Not optimal solution, but let's see if I can even code it
Coding
- 18:55 (27m with debugging)

delta   10121   positive, so left remove index 2, (the first/only in queue)
        ()(()
queue   (

delta   101212
        ()(a()(
          (   (      save index, try both removes

delta   10-2+0-1
        ()))(()
          XX

())(
closed 1
open 1

-
- dfs w/ memo to deal with uniqueness constraint
- check if valid during each dfs pass [O(n)]
- for each removal, branch, passing in curr total removes. branching dfs should return minimum given that string
- no more dfs if already valid
- pruning:
    -
    - only do a removal if it lowers our imbalance (right remove closing if negative, left remove opening if positive)
    - if adjacent braces of the same type (i.e. no letters in between them), we can consider just 1 removal for all of them since they're not unique.
    -

After reading hint:
- okay, we calculate number of invalid parens (aka min number to delete), then blind dfs until we reach that number (not caring if the variations are valid), where we then calculate if its valid or not. if valid, bubble the permutation up to the topi

- I feel like the possibilities are too varied to be comprehensively considered in 1hr.
- eg. (a)())() 's 2nd parens looks valid, but is a valid way to remove it if you consider the full output

# validity check:
# +1 invalid if any closing on without an opening on the stack
# +1 invalid if an opening at the end

- brute force (so no pruning), we consider every subset where each parens is removed.
    - memoed:
        Time O(2^k) where k is number of parens
        Space O(n * 2^k)? n, being string length since we pass it in
"""


class Solution:
    """
    √
        ()(()
l           1
r

        ()))(()
l              1
r          2
    """

    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = set()

        @cache  # wonder if this works when we don't have a return
        def dfs(str, l, r):
            if l == r == 0:
                res.add(str)
                return

            # go thru all variations where 1 removal happens
            i = 0
            while i < len(str):
                if l and str[i] == '(':
                    dfs(str[:i] + str[i + 1:], l - 1, r)
                elif r and str[i] == ')':
                    dfs(str[:i] + str[i + 1:], l, r - 1)
                i += 1

        def parenErrors(str):
            opensToDelete = 0
            closedsToDelete = 0

            for c in str:
                if c == '(':
                    opensToDelete += 1
                elif c == ')':
                    if opensToDelete == 0:
                        closedsToDelete += 1
                    else:
                        opensToDelete -= 1

            return opensToDelete, closedsToDelete

        opensToDelete, closedsToDelete = parenErrors(s)

        dfs(s, opensToDelete, closedsToDelete)

        return list(res)
