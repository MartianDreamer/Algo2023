from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counts = {}
        rs = 0
        for row in grid:
            key = " ".join([str(e) for e in row])
            counts[key] = counts.get(key, 0) + 1
        for col in [[grid[j][i] for j in range(len(grid))] for i in range(len(grid))]:
            key = " ".join([str(e) for e in col])
            if key in counts:
                rs += counts[key]
        return rs

print(Solution().equalPairs([[3,2,1],[1,7,6],[2,7,7]]))