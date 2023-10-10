"""
10:26 - 11:06 (40m)
10:05? - 10:40 (35m)
(total: 75m)

{dec | int} [{e | E} {dec | int}]

Dec:
[+ | -] [{number}] . [{number}]

Int:
[+ | -] {number}

BCR:
- time O(n)
- space O(log10 n)

Test cases to try:
"2.2e+2.2"  -> true
".-4"       -> false
"+"         -> false
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        # setting i to -1 is signal to caller that consume failed from unexpected char
        def consume_dec_or_int(i):
            # consume +/-
            if i == -1 or i == len(s):
                return i

            # consume number
            i, had_integral = consume_opt_int(i)

            if i == -1:
                return i

            # tricky
            if i == len(s):
                return i if had_integral else -1

            if s[i] == '.':
                i += 1
                i, had_fractional = consume_opt_int(i, False)  # after dot, there was no num
                return i if had_fractional or had_integral else -1
            else:
                return i if had_integral else -1

        def consume_opt_int(i, allow_sign=True):
            advanced = False

            if i == -1 or i == len(s):
                return i, advanced

            if allow_sign and s[i] in ('+', '-'):
                i += 1

            while i < len(s) and s[i].isdigit():
                i += 1
                advanced = True
            return i, advanced

        def consume_e(i):
            if s[i] in ('E', 'e'):
                i += 1
            else:
                return False

            return consume_opt_int(i) == (len(s), True)

        i = consume_dec_or_int(0)

        # terminate early if not number
        if i == -1:
            return False

        if i < len(s):
            return consume_e(i)
        else:
            return True
