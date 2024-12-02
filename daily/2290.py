from collections import deque
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def bfs_0_1() -> int:
            nonlocal m, n
            distance = [[m + n - 1] * n for _ in range(m)]
            distance[0][0] = 0
            dq = deque([(0, 0)])
            while dq:
                r, c = dq.popleft()

                for nr, nc in [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]:
                    if nr >= 0 and nr < m and nc >= 0 and nc < n:
                        d = distance[r][c] + grid[nr][nc]
                        if distance[nr][nc] > d:
                            distance[nr][nc] = d
                            if grid[nr][nc]:
                                dq.append((nr, nc))
                            else:
                                dq.appendleft((nr, nc))

            return distance[m - 1][n - 1]

        return bfs_0_1()


print(
    Solution().minimumObstacles(
        [
            [0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
            [0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
            [1, 0, 1, 0, 0, 0, 1, 1, 1, 0],
        ]
    )
)
