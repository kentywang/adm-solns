from random import randint

from profilerv2 import ProfilerV2
from util import asserter

"""
Obs: 
- Smaller number is one with fewest digits, e.g. 33 < 333
- If equal number of digits, smaller is one with smaller leading number, e.g. 123 < 223
- If leading number is equal, smaller is one with next digit being smaller, e.g. 123 < 124

Our plan is to remove 1 digit at a time, which should yield the same
result as if we remove all the digits at once iff we don't need to backtrack.

To pick each digit to remove, we remove the leading digit if it's bigger than
the subsequent digit. If isn't, try on the next digit, ad nauseum.

Theoretically, this can be O(n) space, O(n) time.

O(n) time because we don't need to restart from scratch after remove a digit,
if we save the largest digit traversed but unremoved.

But actually, we're trying to find order for all digit in terms of when it should be removed.
And that essentially means sorting it. And sorting takes O(n^2) to O(n lg n) time.

EDIT: Optimal answer is O(n) using a stack. Not implemented.
"""


class IndexAndValue:
    def __init__(self, i, val):
        self.i = i
        self.val = val

    def __gt__(self, other):
        if self.i < other.i and self.val > other.val:
            return True
        return False


def removekdigits(num: str, k: int) -> str:
    """
    O(n lg n) time
    """
    idxandvals = [IndexAndValue(i, v) for i, v in enumerate(num)]
    ordered = sorted(idxandvals)


asserter(lambda: removekdigits("1429", 1), '129')
asserter(lambda: removekdigits("1112", 2), '11')
asserter(lambda: removekdigits("112", 1), '11')  # test equal values are deprioritized to higher-valued latter digits
asserter(lambda: removekdigits("9", 1), '0')
asserter(lambda: removekdigits("3529", 2), '29')
asserter(lambda: removekdigits("1491", 1), '141')
asserter(lambda: removekdigits("1432219", 3), '1219')
asserter(lambda: removekdigits("10200", 1), '200')
asserter(lambda: removekdigits("10", 2), '0')

with ProfilerV2(removekdigits, var='n', start=4000, mapper=lambda x: ''.join(str(randint(0, 9)) for _ in range(x))) as (
        f, n):
    f(n, 3200)

n = ''.join(str(randint(0, 9)) for _ in range(16000))
with ProfilerV2(removekdigits, var='k', start=2000) as (f, k):
    f(n, k)
