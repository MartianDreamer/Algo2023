from typing import List, Tuple
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def neighbours(row: int, col: int) -> List[Tuple[int, int]]:
            left, right, up, down = col - 1, col + 1, row - 1, row + 1
            rs = [[row, left], [row, right], [up, col], [down, col]]
            return [
                (r, c)
                for r, c in rs
                if 0 <= r < len(board)
                and 0 <= c < len(board[0])
                and board[r][c] == "O"
            ]

        def bfs(row: int, col: int):
            if board[row][col] != "O":
                return
            board[row][col] = "X"
            surrounded = True
            frontiers = deque([(row, col)])
            regions = []
            while frontiers:
                f = frontiers.popleft()
                regions.append(f)
                r, c = f
                fneighbours = neighbours(r, c)
                frontiers.extend(fneighbours)
                for r1, c1 in fneighbours:
                    board[r1][c1] = "X"
                if surrounded and (
                    r == 0 or r == len(board) - 1
                    or c == 0 or c == len(board[0]) - 1
                ):
                    surrounded = False
            if not surrounded:
                not_surrouneded.extend(regions)

        not_surrouneded = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                bfs(r, c)
        for r, c in not_surrouneded:
            board[r][c] = "O"
