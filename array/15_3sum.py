from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        result = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue    
            right = len(nums) - 1
            left = i + 1
            if nums[i] + nums[right - 1] + nums[right] < 0 or nums[i] + nums[left] + nums[left + 1] > 0:
                continue 
            while left < right:
                if nums[left] + nums[right] > -nums[i]:
                    right -= 1
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                else: 
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left + 1] == nums[left]:
                        left += 1
                    left += 1
        return result


print(Solution().threeSum([-2, 0, 1, 3]))
