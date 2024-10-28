from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        count = 0
        prev_end = -5 * 10**4
        for start, end in intervals:
            if prev_end > start:
                count += 1
                continue
            prev_end = end
                
        return count



print(Solution().eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))