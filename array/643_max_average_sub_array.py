from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        rs = sum(nums[:k])
        cur_sum = rs
        for i in range(1, len(nums) - k + 1):
            cur_sum -= (nums[i-1] - nums[i+ k - 1])
            rs = max(rs, cur_sum)
        return rs/k
