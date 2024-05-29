from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remDict = dict()
        for i, v in enumerate(nums):
            if target - v in remDict:
                return [remDict[target - v], i]
            remDict[v] = i
        return []
