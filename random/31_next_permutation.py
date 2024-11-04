from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in range(i + 1, len(nums)):
                    if nums[j] >= nums[i] and (j + 1 >= len(nums) or nums[j + 1] <= nums[i]):
                        nums[i], nums[j] = nums[j], nums[i]
                nums[i + 1:] = nums[:i:-1]
                return
        
        nums.reverse()
