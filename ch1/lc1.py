# 8/30/22 21:17
# v1: 8/30 23:00
# v2: 8/31 10:13
from itertools import islice, takewhile
import sys


def daily_temperatures_v1(t: list[int]) -> list[int]:
    for i, t1 in enumerate(t):  # original stream
        days_til_hotter = 0
        offset_str = islice(t, i, sys.maxsize)
        for _ in takewhile(lambda t2: t1 >= t2, offset_str):
            # keep offsetting 2nd stream until higher temp reached
            days_til_hotter += 1

        if days_til_hotter != len(t) - i:
            t[i] = days_til_hotter
        # else we've exhausted the days and didn't find a higher temperature day
        else:
            t[i] = 0
    return t


def daily_temperatures_v2(t: list[int]) -> list[int]:
    for i in range(len(t)):
        day_ct_til_hotter = 1
        for j in range(i + 1, len(t)):
            if t[j] <= t[i]:
                day_ct_til_hotter += 1
            else:
                break

        if day_ct_til_hotter != len(t) - i:
            t[i] = day_ct_til_hotter
        else:
            t[i] = 0
    return t

# Optimal solution (unreached):
# Use stack to hold uncalculated indices. Repeatedly pop those indices off
# when a bigger element is encountered (so 1 big element could potentially
# pop off several elements), and process them.
def daily_temperatures_lc(T: list[int]) -> list[int]:
    stack = []
    for i, t in enumerate(T):
        while stack and T[stack[-1]] < t:
            cur = stack.pop()
            T[cur] = i - cur
        stack.append(i)

    for i in stack:
        T[i] = 0

    return T
