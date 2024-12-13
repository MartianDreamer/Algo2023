from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        sorted_indices = sorted([i for i in range(len(nums))], key=lambda e: nums[e])
        rs = 0
        for i in sorted_indices:
            if nums[i] == 1_000_001:
                continue
            rs += nums[i]
            if i > 0 and nums[i - 1] != 1_000_001:
                nums[i - 1] = 1_000_001
            if i < len(nums) - 1 and nums[i + 1] != 1_000_001:
                nums[i + 1] = 1_000_001
        return rs
