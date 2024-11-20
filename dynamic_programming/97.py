class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp: dict[str, bool] = {}
        
        def calculate(s1: str, s2: str, s3: str) -> bool:
            s1, s2 = sorted([s1, s2])
            key = f"{s1}_{s2}_{s3}"
            if len(s1) + len(s2) != len(s3):
                dp[key] = False
            if len(s1) <= 1 and len(s2) <= 1:
                dp[key] = s1 + s2 == s3 or s2 + s1 == s3
            if key in dp:
                return dp[key]
            dp[key] = False
            if s1.startswith(s3[0]):
                dp[key] = dp[key] or calculate(s1[1:], s2, s3[1:])
            if not dp[key] and s2.startswith(s3[0]):
                dp[key] = dp[key] or calculate(s1, s2[1:], s3[1:])
            return dp[key]

        return calculate(s1, s2, s3)
    
print(Solution().isInterleave("aa", "ab", "aaba"))