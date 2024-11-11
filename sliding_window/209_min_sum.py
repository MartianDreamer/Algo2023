from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = sum(nums)
        if total < target:
            return 0
        l, r = 0, len(nums) - 1
        while total >= target:
            if nums[l] <= nums[r]:
                total -= nums[l]
                l += 1
            else:
                total -= nums[r]
                r -= 1
        return r - l + 2


print(Solution().minSubArrayLen(7, [2,5,2,2,4,6]
))
