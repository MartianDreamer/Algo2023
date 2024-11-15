from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        rs = []
        for i in range(len(nums)):
            rs.extend([[nums[i], *p] for p in self.permute(nums[:i] + nums[i + 1:])])
        return rs
