from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = int(len(nums) * (len(nums) + 1) / 2)
        for e in nums:
            sum -= e
        return sum