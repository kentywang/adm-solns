from collections import deque
from heapq import heappush, heappop

from misc.datastructs import Heap


def selectionsort(nums):
    """
    unstable (unless using LL), in-place
    """
    for i in range(0, len(nums)):
        curr_min = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[curr_min]:
                curr_min = j
        nums[i], nums[curr_min] = nums[curr_min], nums[i]

    return nums


def selectionsortV2(nums):
    for i, _ in enumerate(nums):
        k, _ = min(((j, nums[j]) for j in range(i, len(nums))), key=lambda x: x[1])
        nums[i], nums[k] = nums[k], nums[i]

    return nums


def bubblesort(nums):
    """
    stable, in-place
    """
    for i in range(len(nums), 0, -1):
        for j in range(i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


def insertionsort(nums):
    """
    stable, in-place
    """
    for i in range(1, len(nums)):
        j = i
        val = nums[j]

        while j >= 1 and nums[j - 1] > val:
            j -= 1

        while j < i:
            nums[j], val = val, nums[j]
            j += 1

        nums[i] = val

    return nums


def heapsort(xs):
    """
    unstable, but can be done in-place (this doesn't though)
    """
    h = []
    for x in xs:
        heappush(h, x)

    return list(heappop(h) for _ in range(len(h)))
    # while h:
    #     yield heappop(h)


def myheapsort(xs):
    """
    unstable, but can be done in-place (this doesn't though)
    """
    h = Heap()
    d = deque()

    for x in xs:
        h.push(x)

    for _ in xs:
        d.appendleft(h.pop())

    return d


# 17:18 - 17:42 (24m, while looking at previous code for Lomuto)


def quickselect(xs, k):
    def partition(i, j):
        pivot = j
        slow = i
        for fast in range(i, j):
            if xs[fast] < xs[pivot]:
                xs[fast], xs[slow] = xs[slow], xs[fast]
                slow += 1

        xs[pivot], xs[slow] = xs[slow], xs[pivot]
        return slow

    i, j = 0, len(xs) - 1

    while True:
        p = partition(i, j)

        if p == k:
            return xs[p]
        if k < p:
            j = p - 1
        else:  # p < k
            i = p + 1


print(quickselect([3, 7, 2, 5, 1, 6, 1, 2, 8], 8))

print(quicksort([3, 7, 2, 5, 1, 6, 1, 2, 8]))

# with ProfilerV2(selectionsort, var='n', start=100,
#                 mapper=lambda x: random.sample(range(0, x), x)
#                 ) as (f, n):
#     f(n)
#
# with ProfilerV2(selectionsortV2, var='n', start=100,
#                 mapper=lambda x: random.sample(range(0, x), x)
#                 ) as (f, n):
#     f(n)
#
# with ProfilerV2(bubblesort, var='n', start=100,
#                 mapper=lambda x: random.sample(range(0, x), x)
#                 ) as (f, n):
#     f(n)
#
# with ProfilerV2(insertionsort, var='n', start=100,
#                 mapper=lambda x: random.sample(range(0, x), x)
#                 ) as (f, n):
#     f(n)
#
# with ProfilerV2(heapsort, var='n', start=100,
#                 mapper=lambda x: random.sample(range(0, x), x)
#                 ) as (f, n):
#     f(n)
#
# with ProfilerV2(myheapsort, var='n', start=100,
#                 mapper=lambda x: random.sample(range(0, x), x)
#                 ) as (f, n):
#     f(n)
#
# with ProfilerV2(quicksort, var='n', start=100,
#                 mapper=lambda x: random.sample(range(0, x), x)
#                 ) as (f, n):
#     f(n)
