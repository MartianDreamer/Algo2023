from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        rs = 0
        for i in range(24):
            count = 0
            for c in candidates:
                count += 1 if c >> i & 1 == 1 else 0
            rs = max(rs, count)
        return rs
