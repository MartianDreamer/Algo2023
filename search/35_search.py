from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums)
        while right - left > 1:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            elif nums[mid] < target:
                left = mid
        return right
