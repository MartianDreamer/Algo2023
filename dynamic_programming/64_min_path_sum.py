from typing import Dict, List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp: Dict[int, int] = {}

        def calculate(i: int, j: int) -> int:
            if i >= len(grid) or j >= len(grid[0]):
                return 10**8

            if i == len(grid) - 1:
                return sum(grid[i][j:])

            if j == len(grid[0]) - 1:
                return sum([row[j] for row in grid[i:]])

            pos = i * 200 + j
            if pos in dp:
                return dp[pos]

            dp[pos] = grid[i][j] + min(calculate(i + 1, j), calculate(i, j + 1))

            return dp[pos]

        return calculate(0, 0)
