from heapq import heappushpop, heappush


class MedianFinder:

    def __init__(self):
        self.lh = []
        self.sh = []
       

    def addNum(self, num: int) -> None:
        if len(self.lh) == len(self.sh):
            heappush(self.lh, -heappushpop(self.sh, -num))
        else:
            heappush(self.sh, -heappushpop(self.lh, num))
        

    def findMedian(self) -> float:
        return self.lh[0] if (len(self.lh) + len(self.sh)) % 2 == 1 else (self.lh[0] - self.sh[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
