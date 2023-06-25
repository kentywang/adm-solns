from itertools import zip_longest

from util import asserter


def int_list(x: int) -> list[int]:
    """
    Time: O(log n) because base 10 digits
    Space: O(log n) ''
    """
    remainders = []
    dividend = x

    while dividend != 0:
        remainder = dividend % 10
        dividend //= 10
        remainders.append(remainder)

    return remainders


def carry_ops(a: int, b: int) -> int:
    """
    Time: O(log n)
    Space: O(log n), but could probably be O(1) if int_list was streamed
    """
    carries = 0
    currently_carrying = 0
    # convert number to array of nums using modulo (reverse order is preferred)
    a_list, b_list = int_list(a), int_list(b)
    # zip arrays to compare
    for x, y in zip_longest(a_list, b_list):
        if x is None:
            x = 0
        if y is None:
            y = 0
        if x + y + currently_carrying >= 10:
            carries += 1
            currently_carrying = 1
        else:
            currently_carrying = 0
    return carries


asserter(lambda: int_list(1), [1])
asserter(lambda: int_list(100), [0, 0, 1])
asserter(lambda: int_list(123), [3, 2, 1])
asserter(lambda: carry_ops(123, 456), 0)
asserter(lambda: carry_ops(555, 555), 3)
asserter(lambda: carry_ops(123, 594), 1)
asserter(lambda: carry_ops(1, 999), 3)
