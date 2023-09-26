# 9:30 - 9:50 (20m)
# "One timer"
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0

        lo = 0
        hi = n - 1
        lmax = height[lo]
        rmax = height[hi]
        area = 0

        while lo < hi:
            # left side lower
            if height[lo] < height[hi]:
                if height[lo] < lmax:
                    area += min(lmax, rmax) - height[lo]
                lo += 1
                lmax = max(lmax, height[lo])
            else:  # right side lower
                if height[hi] < rmax:
                    area += min(lmax, rmax) - height[hi]
                hi -= 1
                rmax = max(rmax, height[hi])

        return area

    def trap2(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0

        lo = 0
        hi = n - 1
        lmax = height[lo]
        rmax = height[hi]
        area = 0

        while lo <= hi:
            # left side lower
            if lmax < rmax:
                lmax = max(lmax, height[lo])
                area += lmax - height[lo]
                lo += 1
            else:  # right side lower
                rmax = max(rmax, height[hi])
                area += rmax - height[hi]
                hi -= 1

        return area
