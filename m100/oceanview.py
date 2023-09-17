"""
Observation:
- building at i has view if buildings at i + 1 onward are lower in value
- last building always has view, so last index always in result

Cases:
- [1] => [0]
- [1,2,2,3] => [3]
- [4,2,4,2] => [2,3]

Options:
- Brute force: O(n^2)
- Suffix max: O(n)
  - ex: [4,2,3,1] gives suffix max array of [4,3,3,1]
  - can offset array to the left since first element uneeded. Fill last element with 0
  - so example becomes [3,3,1,0]
  - or just deal with offset

"""


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        size = len(heights)
        max_heights_from_right = [0] * size

        i = size - 1
        prevhighest = 0
        while i >= 0:  # 3
            max_heights_from_right[i] = prevhighest  # 3
            prevhighest = max(heights[i], prevhighest)  # 4
            i -= 1

        res = []
        for i, (h, m) in enumerate(zip(heights, max_heights_from_right)):
            if h > m:
                res.append(i)

        return res

    # Done in 20m

    # improvement, based on online soln
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        highest = 0
        res = []
        # reverse traverse the list, upping the highest var to the max whenever encountered
        for i in range(n - 1, -1, -1):
            if heights[i] > highest:
                res.append(i)
                highest = heights[i]

        return reversed(res)
