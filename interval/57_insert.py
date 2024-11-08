from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        def search_start() -> int:
            l, r = -1, len(intervals)
            while r - l > 1:
                m = (l + r) // 2
                if intervals[m][0] < newInterval[0]:
                    l = m
                elif intervals[m][0] >= newInterval[0]:
                    r = m
            return l

        def search_end() -> int:
            l, r = -1, len(intervals)
            while r - l > 1:
                m = (l + r) // 2
                if intervals[m][1] <= newInterval[1]:
                    l = m
                elif intervals[m][1] > newInterval[1]:
                    r = m
            return r

        start = search_start()
        end = search_end()
        rs = []

        if start < 0 or intervals[start][1] < newInterval[0]:
            rs.extend(intervals[:start + 1])
        else:
            rs.extend(intervals[:start])
            newInterval[0] = intervals[start][0]

        if end >= len(intervals) or intervals[end][0] > newInterval[1]:
            rs.append(newInterval)
            rs.extend(intervals[end:])
        else:
            newInterval[1] = intervals[end][1]
            rs.append(newInterval)
            rs.extend(intervals[end + 1:])

        return rs


# print(Solution().insert([[2,5],[6,7],[8,9]], [0,1]))
# print(Solution().insert([[5, 7]], [1, 5]))
# print(Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [0, 3]))
print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8]))
