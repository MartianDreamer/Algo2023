from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[len(nums) - 1]:
            return nums[0]
        if len(nums) <= 3:
            return min(nums)
        middle = int(len(nums) / 2)
        left = nums[:middle]
        right = nums[middle:]
        if left[0] > left[len(left) - 1]:
            return self.findMin(left)
        else:
            return self.findMin(right)
