from typing import Dict, List, Tuple
from __data import param


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[-1] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            dp[i][0] = 1 if matrix[i][0] == "1" else 0
        for i in range(len(matrix[0])):
            dp[0][i] = 1 if matrix[0][i] == "1" else 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        for r in dp:
            print(r)
        return dp[len(matrix) - 1][len(matrix[0]) - 1] ** 2


print(
    Solution().maximalSquare(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "1", "1", "1"],
        ]
    )
)
