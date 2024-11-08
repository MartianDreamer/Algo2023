from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_val = 2**maximumBit - 1
        nums_val = nums[0]
        for n in nums[1:]:
            nums_val ^= n
        rs = [max_val ^ nums_val]
        for n in nums[len(nums) - 1:0:-1]:
            nums_val ^= n
            rs.append(nums_val ^ max_val)
        return rs

print(Solution().getMaximumXor([2,3,4,7], 3))