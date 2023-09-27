"""
Observations:
- we can tolerate more ( than ), but if end up with a surplus, we need to remove from the left until we are even
- we only consider parens within range. Reset left bound to right bound when we "zero out" our parens
- if we have a deficit of parens (-1), we need to immediately
- could keep two pointers [O(1)], or stack [O(n)]

Option 1: Mark indices of parens that we should skip, then build "view" of string without those parens
Time: O(n)
Space: O(n) (s)
- keep track of delta, ++ if "(" or -- if ")"
- skip over alpha chars
- when delta is 0 and we encounter a "(", we leave left index ptr and move right ptr until we can zero out the delta
- when we zero out, we move both left and right to right + 1
- left ptr is incremented whenever we decrement a positive delta
- if we get get negative delta (-1), zero it, mark index as skippable, and move left and right to right + 1
- if we end up with positive delta, mark left index as skippable, increment ptr, and decrease delta

Cases:
((((()      -> (), positive, remove left parens ()
()(         -> (), positive but zeroed earlier. So ignore those (mark index as skippable)
()())       -> ()() negative - remove from right immediately (mark index as skippable)
()(()       -> ()()
^^
(           -> None
)           -> None

Playground:
        abc((()
left           ^
right         ^
delta   2
skippable   XX
----------------
Result: abc(  )

        (a(b())c
left        ^
right           ^
delta   1
skippable   X
----------------
Result: (a(b ))c

12:58 - 13:21
Planning: 23min (multitasking) + 10min (from earlier)
13:21 - 13:47
Coding: 26min

Thoughts:
Tricky in that we need to have left skip to the next parens, not just any alphas.
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        left = right = 0
        delta = 0
        skippable = set()

        def nextleftparens(i) -> int:
            i += 1
            while i < n and s[i] != '(':
                i += 1
            return i

        while right < n:
            if s[right] == '(':
                if delta == 0:
                    left = right  # move left up to new set of parens
                delta += 1

            elif s[right] == ')':  # so when s[right] == ')':
                if delta == 0:  # can't have more closes than opens, so remove
                    skippable.add(right)
                else:  # delta is positive, so we close off leftmost parens.
                    left = nextleftparens(left)
                    delta -= 1

            # implicit else case here is if s[right] is alpha
            right += 1

        while delta:
            skippable.add(left)
            left = nextleftparens(left)
            delta -= 1

        return ''.join(char for i, char in enumerate(s) if i not in skippable)


"""
23:24 - 23:32
much simpler than first go
"""


class Solution:
    def minRemoveToMakeValid2(self, s: str) -> str:
        dels = []
        opens = []
        for i, ch in enumerate(s):
            if ch.isalpha():
                continue
            if ch == ')':
                if not opens:
                    dels.append(i)
                else:
                    opens.pop()
            else:
                opens.append(i)
        return [ch for i, ch in enumerate(s) if i not in dels + opens]


print(Solution().minRemoveToMakeValid(")((c)d()(l"))
print(Solution().minRemoveToMakeValid('((((()'))

print(Solution().minRemoveToMakeValid('lee(t(c)o)de)'))
