from typing import List
from itertools import chain


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [[0] * n for _ in range(m)]
        for r, c in chain(guards, walls):
            grid[r][c] = 1

        guarded = 0
        for gr, gc in guards:
            # guard up
            for i in range(gr - 1, -1, -1):
                if grid[i][gc] == 1:
                    break
                guarded += 1 if grid[i][gc] == 0 else 0
                grid[i][gc] = 2

            # guard down
            for i in range(gr + 1, m):
                if grid[i][gc] == 1:
                    break
                guarded += 1 if grid[i][gc] == 0 else 0
                grid[i][gc] = 2

            # guard left
            for i in range(gc - 1, -1, -1):
                if grid[gr][i] == 1:
                    break
                guarded += 1 if grid[gr][i] == 0 else 0
                grid[gr][i] = 2

            # guard right
            for i in range(gc + 1, n):
                if grid[gr][i] == 1:
                    break
                guarded += 1 if grid[gr][i] == 0 else 0
                grid[gr][i] = 2

        return m * n - guarded - len(guards) - len(walls)


print(
    Solution().countUnguarded(4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]])
)
