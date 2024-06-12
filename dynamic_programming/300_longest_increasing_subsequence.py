from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        counts = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    count = counts[j] + 1
                    counts[i] = count if count > counts[i] else counts[i]
        return max(counts)

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18]))
print(Solution().lengthOfLIS([3,7,8,6,3,10,9,10]))
print(Solution().lengthOfLIS([0,1,0,3,2,3]))
print(Solution().lengthOfLIS([7,7,7,7,7,7,7,7,7,7]))