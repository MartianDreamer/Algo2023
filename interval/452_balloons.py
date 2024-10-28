from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[1])
        count = 0
        prev_end = -2**31
        for start, end in points:
            if start <= prev_end:
                continue
            prev_end = end
            count += 1
        return count

Solution().findMinArrowShots([[1,2],[2,3],[3,4],[4,5]])
