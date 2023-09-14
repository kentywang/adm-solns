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


def heapsort(xs):
    h = []
    for x in xs:
        heappush(h, x)
    return list(heappop(h) for _ in range(len(h)))


def myheapsort(xs):
    h = Heap()
    d = deque()

    for x in xs:
        h.push(x)

    for _ in xs:
        d.appendleft(h.pop())

    return d


print(list(myheapsort([3, 7, 2, 5, 1, 6, 2, 8])))

with ProfilerV2(selectionsort, var='n', start=100,
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
