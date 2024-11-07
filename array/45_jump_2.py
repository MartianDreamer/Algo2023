from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        step: int = 0
        cur: int = 0
        while cur < len(nums) - 1:
            start = cur
            farthest = 0
            for i in range(1, nums[start] + 1):
                if start + i >= len(nums) - 1:
                    cur = start + i
                    break
                if start + i + nums[start + i] > farthest:
                    farthest = start + i + nums[start + i]
                    cur = start + i
            step += 1
        return step

print(Solution().jump([2,3,1,1,4]))