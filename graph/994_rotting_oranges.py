
from typing import List, Tuple


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        empty_cell_count = 0
        rotten_oranges: List[Tuple[int, int]] = []
        minute_count = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    rotten_oranges.append((row, col))
                elif grid[row][col] == 0:
                    empty_cell_count += 1

        rotten_orange_count = len(rotten_oranges)

        def infect_rot(row: int, col: int) -> List[Tuple[int, int]]:
            nonlocal rotten_orange_count
            rotten_oranges = [
                (r, c) for (r, c) in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
                if 0 <= r < len(grid)
                and 0 <= c < len(grid[0])
                and grid[r][c] == 1
            ]
            for (r, c) in rotten_oranges:
                grid[r][c] = 2
                rotten_orange_count += 1
            return rotten_oranges

        frontier_size = len(rotten_oranges)
        while len(rotten_oranges) != 0:
            (r, c) = rotten_oranges.pop(0)
            frontier_size -= 1
            rotten_oranges.extend(infect_rot(r, c))
            if frontier_size == 0 and len(rotten_oranges) != 0:
                minute_count += 1
                frontier_size = len(rotten_oranges)

        return minute_count if rotten_orange_count + empty_cell_count == len(grid) * len(grid[0]) else -1
