from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        rem = nums[len(nums) - k:]
        for i in range(len(nums) - 1 - k, -1, -1):
            nums[i + k] = nums[i]
        for i in range(k):
            nums[i] = rem[i]
