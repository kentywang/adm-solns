"""
18:55 - 19:14 (19m)

O(lg n)
O(lg n)
"""
from functools import cache


class Solution:
    def myPow(self, x: float, n: int) -> float:
        @cache
        def myPowRecur(power):
            if power == 0:
                return 1
            if power == 1:
                return x
            return myPowRecur(power // 2) * myPowRecur(power - (power // 2))

        if x == 0:
            return 0

        negative_n = n < 0
        n = abs(n)

        res = myPowRecur(n)

        return res if not negative_n else (1 / res)

    def binaryExp(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        # Handle case where, n < 0.
        if n < 0:
            n = -1 * n
            x = 1.0 / x

        # Perform Binary Exponentiation.
        result = 1
        while n != 0:
            # If 'n' is odd we multiply result with 'x' and reduce 'n' by '1'.
            if n % 2 == 1:
                result *= x
                n -= 1
            # We square 'x' and reduce 'n' by half, x^n => (x^2)^(n/2).
            x *= x
            n //= 2

        return result


print(Solution().binaryExp(2, 7))
