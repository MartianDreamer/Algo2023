from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums[1:])
        if left == right:
            return 0
        for i in range(1, len(nums)):
            left, right = left + nums[i - 1], right - nums[i]
        return -1
