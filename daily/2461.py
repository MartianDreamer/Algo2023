from typing import Dict, List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        hm: Dict[int, int] = {}
        start = 0
        total = 0
        rs = total
        for i in range(len(nums)):
            num = nums[i]
            if hm.get(num, -1) != -1:
                old_start = start
                for n in nums[old_start : hm[num] + 1]:
                    total -= n
                    start += 1
            if i - start < k:
                total += num
                hm[num] = i
            if i - start == k - 1:
                rs = max(rs, total)
                total -= nums[start]
                hm[nums[start]] = -1
                start += 1
        return rs


# print(Solution().maximumSubarraySum([9, 9, 9, 1, 2, 3], 3))
print(Solution().maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3))
