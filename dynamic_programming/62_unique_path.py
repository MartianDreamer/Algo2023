class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[m - 2][n - 1] = 1
        dp[m - 1][n - 2] = 1

        def find_path(r: int, c: int) -> int:
            if r >= m:
                return 0
            if c >= n:
                return 0
            if dp[r][c] != 0:
                return dp[r][c]
            dp[r][c] = find_path(r,c + 1) + find_path(r + 1, c)
            return dp[r][c]

        return find_path(0, 0)
