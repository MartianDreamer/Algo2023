from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        elif nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums) - 1
        left, right = 0, len(nums) - 1
        middle = (left + right) // 2
        while nums[middle] < nums[middle - 1] or nums[middle] < nums[middle + 1]:
            if nums[middle] < nums[middle - 1]:
                left = middle - 2
                right = middle
            elif nums[middle] < nums[middle + 1]:
                right = middle + 2
                left = middle
            middle = (left + right) // 2
        return middle
