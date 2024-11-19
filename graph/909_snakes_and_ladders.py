from typing import List, Tuple
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def ord_to_pos(ord: int) -> Tuple[int, int]:
            ord -= 1
            row_length = len(board[0])
            row_offset = ord // row_length
            col = (
                ord % row_length
                if row_offset % 2 == 0
                else row_length - 1 - (ord % row_length)
            )
            row = len(board) - 1 - row_offset
            return (row, col)

        frontiers = deque([1])
        fcount = 1
        target = len(board) * len(board[0])
        dr_count = 0
        rs = -1
        reach = False

        while frontiers and not reach:
            f = frontiers.popleft()
            fcount -= 1
            for neighbour in range(f + 1, min(f + 6, target) + 1):
                r, c = ord_to_pos(neighbour)
                if board[r][c] == -1:
                    frontiers.append(neighbour)
                elif board[r][c] > 0:
                    frontiers.append(board[r][c])
                reach = reach or (neighbour == target or board[r][c] == target)
                board[r][c] = 0
            if not fcount:
                fcount = len(frontiers)
                dr_count += 1
            if reach:
                rs = dr_count + (1 if fcount != len(frontiers) else 0)

        return rs

 
print(Solution().snakesAndLadders([[-1,-1,-1],[-1,9,8],[-1,8,9]]
))