import sys
from typing import List
from __test_cases.test_1466 import case1


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        count = 0
        links = [[] for _ in range(n)]
        met = set()

        for [departure, destination] in connections:
            links[departure].append(-destination)
            links[destination].append(departure)

        def dfs_count(root: int):
            if root in met:
                return
            met.add(root)
            nonlocal count
            for city in links[root]:
                if city < 0 and -city not in met:
                    count += 1
                dfs_count(abs(city))
        
        dfs_count(0)

        return count


# print(Solution().minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))
# print(Solution().minReorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]))
sys.setrecursionlimit(30000)
print(Solution().minReorder(case1[0], case1[1]))
