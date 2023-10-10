from collections import defaultdict, deque
from typing import List

"""
20:36 - 21:22 (46m)
time: O(max(m,n)^2)
space: O(1)

BCR: O(mn)

Strategy:
- find max row length, 
    0,0

    1,0
    0,1

    2,0
    1,1
    0,2

    3,0
    2,1
    1,2
    0,3

    00
    00
    00
    00

    13
    2456
    height = 2, mrl = 4
    i : 0 to 3
    j : i to 0
    00√
    10√
    01√
    20x
    11√
    02x
    30x
    21x
    12√
    ...

    13
    2
    4
    height: 3, mrl:2
    i: 0 to 3
    j: i to 3
    00  √
    10  √
    01  √
    20  √
    11  x

    1,2,3,4,5,6,7,8,9,10,11,12
    1
    1
    1
    1
    1
    1
    9,2,3,4,2,1



    123
     456
      789 


        23456
       901
      8
     67
    12345

    1
    2
    3
    4
    5
        5
       4
      3
     2
    1
    - there's probl some way to zip these in an interleaved way to get it, but I don't see it yet


    5 -> (5,0),(4,1),(3,2),(2,3),(1,4),(0,5)
"""


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """
        my attempt (TLE)
        time: O(max(m,n)^2)
        space: O(1)
        """
        height = len(nums)
        max_row_len = max(len(row) for row in nums)

        res = []
        for i in range(2 * max(height, max_row_len)):
            for j in range(i, -1, -1):
                if j < height and i - j < len(nums[j]):
                    res.append(nums[j][i - j])
        # possible optimizations:
        #   - count num of elements. Terminate when len(res) reaches that count.
        return res

    def findDiagonalOrder2(self, nums: List[List[int]]) -> List[int]:
        """
        online, with my changes
        time: O(mn)
        space: O(mn)
        """
        d = defaultdict(deque)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                d[i + j].appendleft(nums[i][j])
        return [v for k in d.keys() for v in d[k]]
