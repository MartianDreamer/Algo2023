import heapq
import math
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] = -gifts[i]
        heapq.heapify(gifts)
        for i in range(k):
            new_pile = int(math.sqrt(-gifts[0]))
            heapq.heappushpop(gifts, -new_pile)
        return -sum(gifts)