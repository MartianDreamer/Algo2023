from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        sorted_nums = sorted([(n, i) for i, n in enumerate(nums)], key=lambda e: e[0])
        rs = 0
        for sn, si in sorted_nums:
            if nums[si] == 1_000_001:
                continue
            rs += sn
            if si > 0 and nums[si - 1] != 1_000_001:
                nums[si - 1] = 1_000_001
            if si < len(nums) - 1 and nums[si + 1] != 1_000_001:
                nums[si + 1] = 1_000_001
        return rs

print(Solution().findScore([2, 1, 3, 4, 5, 2]))
