"""
stable
"""
from heapq import heappush, heappop

from util import asserter


def absSort(arr):
    heap = []

    for element in arr:
        absval = abs(element)
        sign = 0 if element < 0 else 1

        heappush(heap, (absval, sign))

    res = []
    while heap:
        absval, sign = heappop(heap)
        res.append(absval if sign == 1 else (absval * -1))

    return res


asserter(lambda: absSort([2, -7, -2, -2, 0]), [0, -2, -2, 2, -7])
