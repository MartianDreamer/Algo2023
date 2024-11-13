from typing import List
import __data

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count, cur, l, r = 0, 0, 1, len(nums) - 1
        if nums[r] + nums[r-1] < lower or nums[l] + nums[l + 1] > upper:
            return count
        while True:
            while nums[r] + nums[cur] > upper and r > cur:
                r -= 1
            if r == cur:
                break
            while True:
                if nums[l] + nums[cur] < lower and l < r:
                    l += 1
                elif nums[l - 1] + nums[cur] >= lower and l - 1 > cur:
                    l -=1
                else:
                    break
            count += r - l + 1 if nums[cur] + nums[l] >= lower else 0
            cur += 1
            l = cur + 1 if l <= cur else l
        return count


# print(Solution().countFairPairs([1,7,9,2,5], 11, 11))
# print(Solution().countFairPairs([0,1,7,4,4,5], 3, 6))
# print(Solution().countFairPairs(*__data.param))
print(Solution().countFairPairs([0,2,1,7,4,4,5], 3, 6))
