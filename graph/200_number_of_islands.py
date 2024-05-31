from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.dfsConnect(j, i, grid):
                    count += 1
        return count

    def dfsConnect(self, rootX: int, rootY: int, grid: List[List[str]]) -> bool:
        if grid[rootY][rootX] != "1":
            return False
        grid[rootY][rootX] = "0"
        left = (rootX - 1, rootY) if rootX - 1 >= 0 else None
        right = (rootX + 1, rootY) if rootX + 1 < len(grid[0]) else None
        up = (rootX, rootY - 1) if rootY - 1 >= 0 else None
        down = (rootX, rootY + 1) if rootY + 1 < len(grid) else None
        for neighbor in (left, right, up, down):
            if neighbor is None or grid[neighbor[1]][neighbor[0]] != "1":
                continue
            self.dfsConnect(neighbor[0], neighbor[1], grid)
        return True


print(Solution().numIslands([["1", "1", "1", "1", "0"], [
      "1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
