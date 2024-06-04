from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heights = dict()
        for num in nums:
            heights[num] = True
            if num - 1 in heights:
                heights[num - 1] = True
        max = 0
        for k in heights:
            if not heights[k] or k - 1 in heights:
                continue
            count = 0
            while k in heights:
                count += 1
                heights[k] = False
                k += 1
            max = count if count > max else max
        return max
