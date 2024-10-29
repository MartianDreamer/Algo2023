import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [i for i in range(1, 1001)]
        

    def popSmallest(self) -> int:
        return heapq.heappop(self.heap)

    def addBack(self, num: int) -> None:
        if num not in self.heap:
            heapq.heappush(self.heap, num)
