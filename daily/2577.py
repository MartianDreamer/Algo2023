from typing import List
from heapq import heappush, heappop

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pq = [(0, 0, 0)]
        visited = set()
        while pq:
            t, r, c = heappop(pq)
            if r == m - 1 and c == n - 1:
                return t
            left, right, up, down = c - 1, c + 1, r - 1, r + 1
            stuck = True
            for nr, nc in [(r, left), (r, right), (up, c), (down, c)]:
                if 0 <= nr < m and 0 <= nc < n and t + 1 >= grid[nr][nc]:
                    stuck = False
                    if (nr, nc) not in visited:
                        heappush(pq, (t + 1, nr, nc))
                        visited.add((nr, nc))
            if stuck:
                continue
            for nr, nc in [(r, left), (r, right), (up, c), (down, c)]:
                if 0 <= nr < m and 0 <= nc < n and t + 1 < grid[nr][nc]:
                    if (grid[nr][nc] - t) % 2 == 0:
                        heappush(pq, (grid[nr][nc] + 1, nr, nc))
                    else:
                        heappush(pq, (grid[nr][nc], nr, nc))
                    
        return - 1