class MedianFinder:
    def __init__(self):
        self.maxh = []
        self.minh = []

    def addNum(self, num: int) -> None:
        heappush(self.minh, -heappushpop(self.maxh, -num))
        if len(self.maxh) < len(self.minh):
            heappush(self.maxh, -heappop(self.minh))

    def findMedian(self) -> float:
        if len(self.maxh) > len(self.minh):
            return -self.maxh[0]
        return (-self.maxh[0] + self.minh[0]) / 2
