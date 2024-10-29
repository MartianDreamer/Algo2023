import heapq
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if candidates * 2 + k >= len(costs) + 1:
            costs.sort()
            return sum(costs[0:k])

        rs = 0

        side_dict:dict[int, List[int]] = {}

        for c in costs[:candidates]:
            if c not in side_dict:
                side_dict[c] = [0]
            else:
                side_dict[c].append(0)

        for c in costs[-candidates:]:
            if c not in side_dict:
                side_dict[c] = [1]
            else:
                side_dict[c].append(1)
        
        heap = costs[:candidates] + costs[-candidates:]
        waiting = costs[candidates:-candidates]
        heapq.heapify(heap)

        for _ in range(k):
            popped_value = heapq.heappop(heap)
            rs += popped_value
            side = side_dict[popped_value].pop(0)
            added: int
            if side == 0:
                added = waiting.pop(0)
                if added not in side_dict:
                    side_dict[added] = [0]
                else:
                    side_dict[added].insert(0, 0)
            else:
                added = waiting.pop()
                if added not in side_dict:
                    side_dict[added] = [1]
                else:
                    side_dict[added].append(1)
            heapq.heappush(heap, added)
        return rs
    

# print(Solution().totalCost([10,20,30,50,60,10,9,8,7,6,5,4,3,2,1,130,140,150,160], 3, 4))
print(Solution().totalCost([2,1,2], 1, 1))