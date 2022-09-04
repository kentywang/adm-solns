from util import asserter


def kangaroo_v1(x1, v1, x2, v2):
    """
    Brute-force: Calculate positional diff between the 'roos after each
    jump. If the diff is 0, return True. If the diff starts growing or stays same,
    ne'er the twain shall meet, so return False.

    O(?) time, O(1) space
    """
    diff = abs(x1 - x2)

    while True:
        if x1 == x2:
            return True

        prev_diff = diff
        x1 += v1
        x2 += v2
        diff = abs(x1 - x2)

        if diff >= prev_diff:
            return False


def kangaroo_v2(x1, v1, x2, v2):
    """
    Roos can be considered lines on grid, where y is the x-position
    and x is time. Whereas a line is y = mx + b where m is slope, our
    roo is vt + x. When we make the two lines equal and solve for x,
    we find the intersection point. Similarly we can do the same for
    the roos, and if we can obtain a t and also make sure it's an integer
    (because this is discrete, not continuous), then we can return True.

    O(1) space, O(1) time
    """
    try:
        t: float = (x2 - x1) / (v1 - v2)
    except ZeroDivisionError:
        return False
    return t.is_integer() and t > 0


asserter(lambda: kangaroo_v1(2, 1, 1, 2), True)
asserter(lambda: kangaroo_v1(2, 1, 1, 0), False)
asserter(lambda: kangaroo_v1(2, 1, 1, 4), False)

asserter(lambda: kangaroo_v2(2, 1, 1, 2), True)
asserter(lambda: kangaroo_v2(2, 1, 1, 0), False)
asserter(lambda: kangaroo_v2(2, 1, 1, 4), False)
