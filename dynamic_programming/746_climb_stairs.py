import random
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        table = [-1] * (len(cost) + 1)

        def calculate(cost: List[int]) -> int:
            if len(cost) <= 1:
                return 0
            elif table[len(cost)] != -1:
                return table[len(cost)]
            table[len(cost)] = min(cost[-1] + calculate(cost[:-1]), cost[-2] + calculate(cost[:-2]))
            return table[len(cost)]

        return calculate(cost)
