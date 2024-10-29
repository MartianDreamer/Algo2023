from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        i = 0
        while i < len(nums) - count:
            if nums[i] == val:
                count += 1
                while len(nums) - count > i and nums[-count] == val:
                    count += 1
                nums[-count], nums[i] = nums[i], nums[-count]
            i += 1
        return len(nums) - count

print(Solution().removeElement([4,5], 5))
