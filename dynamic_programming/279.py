from math import sqrt, ceil

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [10001] * (n + 1)
        for i in range(1, n + 1):
            if sqrt(i) % 1 == 0:
                dp[i] = 1
                continue
            for j in range(1, ceil(sqrt(i))):
                dp[i] = min(dp[i], dp[j * j] + dp[i - j * j])
        return dp[n]
