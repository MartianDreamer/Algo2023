from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        rs = 0
        replaced_count = 0
        zeroes_pos = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes_pos.append(i)
                if replaced_count < k:
                    nums[i] = 1
                    replaced_count += 1
                else:
                    start = zeroes_pos.pop(0) + 1
            rs = max(rs, i + 1 - start)
        return rs

print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))