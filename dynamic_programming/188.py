from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * n for _ in range(k + 1)]
        for i in range(1, k + 1):
            maxdiff = 0 - prices[0]
            for j in range(1, n):
                prev_day_profit = dp[i][j - 1] if j > 0 else 0
                dp[i][j] = max(prev_day_profit, prices[j] + maxdiff)
                maxdiff = max(maxdiff, dp[i - 1][j] - prices[j])

        return dp[k][n - 1]

print(Solution().maxProfit(2, [2, 4, 1]))
