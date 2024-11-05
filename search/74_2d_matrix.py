from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bi_search(nums: List[int], target: int) -> bool:
            left, right = 0, len(nums) - 1
            while right >= left:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    return True
            return False
        
        flatten = []
        for nums in matrix:
            flatten.extend(nums)
        return bi_search(flatten, target)

print(Solution().searchMatrix([[1,3]], 3))