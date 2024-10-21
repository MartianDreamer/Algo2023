from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        zero_pos = []
        deleted = False
        rs = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_pos.append(i)
                if deleted:
                    start = zero_pos.pop(0) + 1
                else:
                    deleted = True
            rs = max(rs, i - start + 1 - 1)
        return rs
