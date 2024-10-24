from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        rs = 0
        for num in nums:
            rs ^= num
        return rs
