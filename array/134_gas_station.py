from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return  -1
        start = 0
        cur_gas = 0
        for i in range(len(gas)):
            cur_gas += gas[i] - cost[i]
            if cur_gas < 0:
                cur_gas = 0
                start = i + 1
        
        return start
