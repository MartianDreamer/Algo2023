import bisect
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda e: e[0])
        dp = [0] * len(events)
        maxval = 0
        for i in range(len(events) - 1, -1, -1):
            _,_,val = events[i]
            maxval = max(val, maxval)
            dp[i] = maxval

        rs = 0

        for i in range(len(events)):
            _, ei, vi = events[i]
            idx = bisect.bisect_left(events, ei + 1, key=lambda e: e[0])
            if idx < len(events):
                rs = max(rs, vi + dp[idx])
            else:
                rs = max(rs, vi)
        return rs


