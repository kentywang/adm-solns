from collections.abc import Generator
from itertools import zip_longest

from util import asserter


def digits(x: int) -> Generator[int]:
    """
    Time: O(log n) because base 10 digits
    Space: O(1)
    """
    dividend = x

    while dividend != 0:
        remainder = dividend % 10
        dividend //= 10
        yield remainder


def carry_ops(a: int, b: int) -> int:
    """
    Time: O(log n)
    Space: O(1)
    """
    carries = 0
    currently_carrying = 0
    # convert number to array of nums using modulo (reverse order is preferred)
    a_digits, b_digits = digits(a), digits(b)
    # zip arrays to compare
    for x, y in zip_longest(a_digits, b_digits):
        if (x if x else 0) + (y if y else 0) + currently_carrying >= 10:
            carries += 1
            currently_carrying = 1
        else:
            currently_carrying = 0
    return carries


asserter(lambda: list(digits(1)), [1])
asserter(lambda: list(digits(100)), [0, 0, 1])
asserter(lambda: list(digits(123)), [3, 2, 1])
asserter(lambda: carry_ops(123, 456), 0)
asserter(lambda: carry_ops(555, 555), 3)
asserter(lambda: carry_ops(123, 594), 1)
asserter(lambda: carry_ops(1, 999), 3)
