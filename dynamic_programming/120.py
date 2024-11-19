from typing import Dict, List, Tuple


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        EMPTY = -(10**4) * 200 - 1
        dp: List[List[int]] = [[EMPTY] for _ in range(len(triangle))]

        def calculate(i: int, j: int) -> int:
            if dp[i][j] != EMPTY:
                return dp[i][j]
            if i == len(triangle) - 1:
                return triangle[i][j]
            dp[i][j] = triangle[i][j] + min(
                calculate(i + 1, j), calculate(i + 1, j + 1)
            )
            return dp[i][j]

        return calculate(0, 0)
