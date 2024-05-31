from typing import List


class Solution:
    # TODO not done yet
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        hSize, vSize = len(heights), len(heights[0])
        pacificFlow = [[False] * vSize for _ in range(hSize)]
        if vSize == 1 and hSize == 1:
            return [[0, 0]]
        rs = []
        sharedCells = ((0, vSize - 1), (hSize - 1, 0))
        queue = []
        for c in sharedCells:
            queue.append(c)
            while len(queue) > 0:
                qe = queue.pop(0)
                c, r = qe[0], qe[1]
                rs.append([r, c])
                for nb in self.neighbors(c, r, hSize, vSize):
                    if heights[nb[1]][nb[0]] > heights[r][c]:
                        queue.append(nb)
                heights[r][c] = -1
        return rs

    def neighbors(self, c: int, r: int, hSize: int, vSize: int):
        rs = []
        if c - 1 >= 0:
            rs.append((c - 1, r))
        if c + 1 < vSize:
            rs.append((c+1, r))
        if r - 1 >= 0:
            rs.append((c, r - 1))
        if r + 1 < hSize:
            rs.append((c, r + 1))
        return rs


print(Solution().pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
      2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
