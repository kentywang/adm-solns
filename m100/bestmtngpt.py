"""
18:19 - 19:00 (BF idea)
   3
   v
01234
11010 colsum

coding attempt:
20:10 - 20:33 (23m)
------- rowsum
10000 | 1
01000 | 1
00010 | 1

k = 3
rowcost[0] = 0*1 + 1*1 + 2*1 = 1 + 2 = 3
rowcost[1] = 3 + 1 - 3 + 1 = 2
rowcost[2] = 2 + 2 - 3 + 2 = 3

colcost[0] = 0*1 + 1*1 + 3*1 = 1 + 3 = 4
colcost[1] = 4 + 1 - 3 + 1 = 3
colcost[2] = 3 + 2 - 3 + 2 = 4
colcost[3] = 4 + 2*2 - 3 = 5
colcost[4] = 5 + 2*3 - 3 = 8

2 + 3 = 5

cols = [0,1,2,2,3,3,4,4,5,6]
rows = [0,0,1,1,2,2,3,3,4,4]
0123456
1010000 0
0101000 1
0010100 2
0001010 3
0000101 4

012345678
111000001     5 + 3+ 2 +1 = 11 or 6+2 + 1 + 0 = 9
(0+1+2+8)/4 = 2.75

conclusion: can't just use avg of coords as meeting place.
obs: we should minimize retreading of the same cell by different ppl
    - median is the optimal?
01234
11011       2+1+1+2 = 6,    3+2+0+1 = 6


- 0s row -> always just +1

Brute force:
- Try each coord as the ideal meeting point for all 1s
- can save the coords of all 1s so we can just iterate through them per each outer iteration of all coords as the meeting pt
- Time: O(mn * mn)
- Space: O(mn)

101
010
rowwise: 001, so median is 0, so row dist is 0 + 0 + 1 = 1
colwise: 012, so median is 1, so col dist is 1 + 0 + 1 = 2
total is thus 1 + 2 = 3
"""


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        """
        Time: O(mn)
        Space: O(max(m,n))
        """
        m = len(grid)
        n = len(grid[0])
        res = 0

        # rowwise iteration
        rows = [i for i, j in product(range(m), range(n)) if grid[i][j]]
        median_row = rows[len(rows) // 2]
        res += sum(abs(r - median_row) for r in rows)

        # colwise iteration
        cols = [j for j, i in product(range(n), range(m)) if grid[i][j]]
        median_col = cols[len(cols) // 2]
        res += sum(abs(c - median_col) for c in cols)

        return res
