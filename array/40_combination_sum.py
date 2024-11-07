from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def calculate(nums: List[int], target: int) -> List[List[int]]:
            if target == 0:
                return [[]]
            rs = []
            prev = -1
            for i in range(len(nums)):
                if nums[i] == prev:
                    continue
                prev = nums[i]
                if target - nums[i] < 0:
                    break
                rs.extend([[nums[i], * c]
                          for c in calculate(nums[i + 1:], target - nums[i])])
            return rs

        return calculate(candidates, target)
