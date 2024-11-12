from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda e: e[0])
        sorted_queries = sorted([[i, queries[i]]
                                for i in range(len(queries))], key=lambda e: e[1])
        checked = 0
        max_b = 0
        for l in sorted_queries:
            q = l[1]
            for i in range(checked, len(items)):
                p, b = items[i]
                if p > q:
                    break
                max_b = max(max_b, b)
            checked = i
            l.append(max_b)
        sorted_queries.sort(key=lambda e: e[0])
        return [b for _, _, b in sorted_queries]


print(Solution().maximumBeauty(
    [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [1, 2, 3, 4, 5, 6]))
