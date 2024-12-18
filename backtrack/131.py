from typing import Dict, List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp: Dict[int, Dict[int, bool]] = {}

        for i in range(len(s)):
            dp[i] = {}
            dp[i][i + 1] = True

        def is_panlindrome(start: int, end: int) -> bool:
            if end in dp[start]:
                return dp[start][end]
            for i in range((end - start) // 2):
                if s[start + i] != s[end - 1 - i]:
                    dp[start][end] = False
                    return False
            dp[start][end] = True
            return True

        def part(start: int, end: int) -> List[List[str]]:
            if start == end:
                return [[]]
            rs: List[List[str]] = []
            for i in range(start + 1, end + 1):
                if not is_panlindrome(start, i):
                    continue
                sub_arr_partitions = part(i, end)
                for p in sub_arr_partitions:
                    p.insert(0, s[start:i])
                rs.extend(sub_arr_partitions)
            return rs

        return part(0, len(s))

print(Solution().partition("bb"))