# 8/30/22 21:17
# v1: 8/30 23:00
# v2: 8/31 10:13
import itertools
import sys


def dailyTemperatures_v1(t: list[int]) -> list[int]:
    result = [0] * len(t)

    for i, t1 in enumerate(t):  # original stream
        offset_str = itertools.islice(t, i, sys.maxsize)
        days_checked = list(
            # keep offsetting 2nd stream until higher temp reached
            itertools.takewhile(lambda t2: t2 <= t1, offset_str))

        if (day_ct_til_hotter := len(days_checked)) != len(t) - i:
            result[i] = day_ct_til_hotter
        # else we've exhausted the days and didn't find a higher temperature day

    return result


def dailyTemperatures_v2(t: list[int]) -> list[int]:
    result = [0] * len(t)

    for i in range(len(t)):
        day_ct_til_hotter = 1
        for j in range(i + 1, len(t)):
            if t[j] <= t[i]:
                day_ct_til_hotter += 1
            else:
                break

        if day_ct_til_hotter != len(t) - i:
            result[i] = day_ct_til_hotter

    return result

# Optimal solution (unreached):
# Use stack to hold uncalculated indices. Repeatedly pop those indices off
# when a bigger element is encountered (so 1 big element could potentially
# pop off several elements), and process them.
def dailyTemperatures_lc(T: list[int]) -> list[int]:
    ans = [0] * len(T)
    stack = []
    for i, t in enumerate(T):
      while stack and T[stack[-1]] < t:
        cur = stack.pop()
        ans[cur] = i - cur
      stack.append(i)

    return ans