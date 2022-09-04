from util import asserter


def rotateleft_v1(d, arr) -> list[int]:
    """
    Naive: Each popleft takes O(n), each append takes O(1), making it O(1) space, O(nm) time
    This algo: calculate new order in O(1), then construct it in O(n) time, for a total of
    O(1) space, O(n) time
    """
    n = len(arr)

    if n == 0:
        return arr

    m = d % n

    return arr[m:] + arr[:m]


asserter(lambda: rotateleft_v1(1, []), [])
asserter(lambda: rotateleft_v1(2, [1, 2]), [1, 2])
asserter(lambda: rotateleft_v1(4, [1, 2, 3, 4, 5]), [5, 1, 2, 3, 4])
