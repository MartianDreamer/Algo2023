import time
from typing import Dict, List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold_stock, not_hold_stock = -prices[0], 0

        for price in prices[1:]:
            not_hold_stock = max(not_hold_stock, hold_stock + price - fee)
            hold_stock = max(hold_stock, not_hold_stock - price)
        return not_hold_stock