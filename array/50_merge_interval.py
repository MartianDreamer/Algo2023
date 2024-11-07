from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda e: e[1])
        rs = []
        for i in intervals[1:]:
            while len(rs) > 0 and i[0] <= rs[-1][0]:
                rs.pop()
            if len(rs) > 0 and rs[-1][1] > i[0]:
                rs[-1][1] = i[1]
                continue
            rs.append(i)
        return rs
