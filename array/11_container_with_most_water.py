from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max = min(height[left],height[right]) * (right - left)
        while left < right:
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            area = min(height[left],height[right]) * (right - left)
            max = area if area > max else max
        return max


Solution().maxArea([1,3,2,5,25,24,5])