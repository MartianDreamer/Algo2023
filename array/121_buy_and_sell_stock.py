from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = prices[0]
        rs = 0
        for price in prices:
            lowestPrice = price if price < lowestPrice else lowestPrice
            rs = price - lowestPrice if price - lowestPrice > rs else rs
        return rs
