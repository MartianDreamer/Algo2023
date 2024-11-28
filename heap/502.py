from typing import List
from heapq import heappop, heappush

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort()
        q = []
        idx = 0
        for i in range(k):
            while idx < n and projects[idx][0] <= w:
                heappush(q, -projects[idx][1])
                idx += 1
            if not q:
                break
            w -= heappop(q)
        return w