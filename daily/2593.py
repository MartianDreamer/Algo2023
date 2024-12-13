from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        sorted_nums = sorted([(n, i) for i, n in enumerate(nums)], key=lambda e: e[0])
        rs = 0
        count = 0
        for sn, si in sorted_nums:
            if count == len(nums):
                break
            if nums[si] == 1_000_001:
                continue
            rs += sn
            count += 1
            if si > 0 and nums[si - 1] != 1_000_001:
                nums[si - 1] = 1_000_001
                count += 1
            if si < len(nums) - 1 and nums[si + 1] != 1_000_001:
                nums[si + 1] = 1_000_001
                count += 1
        return rs

print(Solution().findScore([2, 1, 3, 4, 5, 2]))
