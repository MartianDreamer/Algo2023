import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        piles.sort()
        left, right = 0, piles[-1]
        k = (0 + right) // 2
        while right != left:
            time = calculate2(piles, k)
            if time > h:
                left = k + 1
            if time <= h:
                right = k
            k = (left + right) // 2
            if k == 0:
                return 1
        return right

def calculate2(piles: List[int], k: int) -> int:
    time = 0
    for pile in piles:
        time += math.ceil(pile / k)
    return time
