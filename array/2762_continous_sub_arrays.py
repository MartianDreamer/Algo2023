from typing import List, Tuple


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        def calculate(start: int, end: int) -> Tuple[int, int, int]:
            lower = end
            upper = end
            streak = 0
            for i in range(end, start, -1):
                if abs(nums[i] - nums[lower]) > 2 or abs(nums[i] - nums[upper]) > 2:
                    break
                streak += end - i
                if nums[i] >= nums[upper]:
                    upper = i
                elif nums[i] <= nums[lower]:
                    lower = i
            return(lower, upper, streak)

        lower, upper , streak, rs, i = 0, 0, 1, 0, 0
        while i < len(nums):
            if abs(nums[i] - nums[lower]) > 2:
                (lower, upper, streak) = calculate(lower, i)
            elif abs(nums[i] - nums[upper]) > 2:
                (lower, upper, streak) = calculate(upper, i)
            if nums[i] >= nums[upper]:
                upper = i
            elif nums[i] <= nums[lower]:
                lower = i
            rs += streak
            streak += 1
            i += 1
        return rs


print(Solution().continuousSubarrays([35, 35, 36, 37, 36, 37, 38, 37, 38]))
