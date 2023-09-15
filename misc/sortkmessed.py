"""
T: O(n lg k)
S: O(k)
"""
from heapq import heappush, heappop


def sort_k_messed_array(arr, k):
    heap = []
    i = 0
    w = len(arr)

    while len(heap) <= k:
        heappush(heap, arr[i])
        i += 1

    while heap:
        arr[i - k - 1] = heappop(heap)
        if i < w:
            heappush(heap, arr[i])
        i += 1

    return arr


print(sort_k_messed_array([1, 4, 5, 2, 3, 7, 8, 6, 10, 9], 2))
