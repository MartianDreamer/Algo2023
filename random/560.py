from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefixes = [0] * len(nums)
        prefixes[0] = nums[0]
        for i in range(1, len(nums)):
            prefixes[i] = prefixes[i - 1] + nums[i]
        ht = {0 : 1}
        count = 0
        for p in prefixes:
            count += ht.get(k - p, 0)
            ht[-p] = ht.get(-p, 0) + 1
        return count

print(Solution().subarraySum([1, -1, 0], 0))
