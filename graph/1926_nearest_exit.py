from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        maze[entrance[0]][entrance[1]] = "x"
        exits: set[int] = set()

        for i in range(len(maze)):
            if maze[i][0] == ".":
                exits.add(position_to_int(i, 0))
            if maze[i][-1] == ".":
                exits.add(position_to_int(i, len(maze[0]) - 1))

        for i in range(len(maze[0])):
            if maze[0][i] == ".":
                exits.add(position_to_int(0, i))
            if maze[-1][i] == ".":
                exits.add(position_to_int(len(maze) - 1, i))

        if len(exits) == 0:
            return -1

        def walkable_neighbours(pos: List[int]) -> List[List[int]]:
            [row, col] = pos
            rs = [[r, c] for [r, c] in [[row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]]
                  if r >= 0
                  and r < len(maze)
                  and c >= 0
                  and c < len(maze[0])
                  and maze[r][c] == "."]
            for [r, c] in rs:
                maze[r][c] = "x"
            return rs

        frontiers = walkable_neighbours(entrance)
        frontiers_size = len(frontiers)
        step_count = 1
        while len(frontiers) != 0:
            frontier = frontiers.pop(0)
            frontiers_size -= 1
            if position_to_int(frontier[0], frontier[1]) in exits:
                return step_count
            frontiers.extend(walkable_neighbours(frontier))
            if frontiers_size == 0:
                step_count += 1
                frontiers_size = len(frontiers)

        return -1


def position_to_int(row: int, col: int) -> int:
    return row * 1000 + col
