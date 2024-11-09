from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        rs = len(nums)
        c = 1
        i = 1
        while i < rs:
            if nums[i] != nums[i - 1]:
                c = 1
                i += 1
                continue
            c += 1
            if c <= 2:
                i += 1
                continue
            idx = i
            while idx < rs and nums[i] == nums[idx]:
                idx += 1
            rs -= idx - i
            nums[i:] = nums[idx:]
        return rs

print(Solution().removeDuplicates([0,0,0,0,0,1,2,2,3,3,4,4]))
# print(Solution().removeDuplicates([1, 1, 1, 2, 2, 3]))
