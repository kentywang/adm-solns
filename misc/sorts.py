import random
from collections import deque
from heapq import heappush, heappop

from misc.datastructs import Heap
from profilerv2 import ProfilerV2


def selectionsort(nums):
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
    stable
    """
    for i in range(len(nums), 0, -1):
        for j in range(i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


def insertionsort(nums):
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
    h = []
    for x in xs:
        heappush(h, x)

    return list(heappop(h) for _ in range(len(h)))
    # while h:
    #     yield heappop(h)


def myheapsort(xs):
    h = Heap()
    d = deque()

    for x in xs:
        h.push(x)

    for _ in xs:
        d.appendleft(h.pop())

    return d


print(insertionsort([3, 7, 2, 5, 1, 6, 2, 8]))

with ProfilerV2(selectionsort, var='n', start=100,
                mapper=lambda x: random.sample(range(0, x), x)
                ) as (f, n):
    f(n)

with ProfilerV2(selectionsortV2, var='n', start=100,
                mapper=lambda x: random.sample(range(0, x), x)
                ) as (f, n):
    f(n)

with ProfilerV2(bubblesort, var='n', start=100,
                mapper=lambda x: random.sample(range(0, x), x)
                ) as (f, n):
    f(n)

with ProfilerV2(insertionsort, var='n', start=100,
                mapper=lambda x: random.sample(range(0, x), x)
                ) as (f, n):
    f(n)

with ProfilerV2(heapsort, var='n', start=100,
                mapper=lambda x: random.sample(range(0, x), x)
                ) as (f, n):
    f(n)

with ProfilerV2(myheapsort, var='n', start=100,
                mapper=lambda x: random.sample(range(0, x), x)
                ) as (f, n):
    f(n)
