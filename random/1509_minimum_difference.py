from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        rs = 2 * 10**9 + 1
        for i in range(3):
            rs = min(rs, nums[- 1 - (3 - i)] - nums[i], nums[-1] - nums[3 - i])
        return rs
