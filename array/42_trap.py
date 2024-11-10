from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        rs = min(min(height[l], height[r]) * (r - 1 - l), 0)
        cur_min = min(height[l], height[r])
        while r - l > 1:
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            new_min = min(height[l], height[r])
            if new_min <= cur_min:
                rs -= new_min
            else:
                rs += (new_min - cur_min) * \
                    (r - l - 1) - cur_min
                cur_min = new_min
        return rs


print(Solution().trap([5,4,12,5,7,1,8,6,9,9,6,1,9,14,2,8,1,2,7,10]))
