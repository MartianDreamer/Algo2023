from typing import List, Set
from collections import deque


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        TARGET = "1_2_3_4_5_0"
        met = set()
        frontiers = deque([board_to_str(board)])
        c = 1
        moves = 0
        if TARGET in frontiers:
            return 0

        while frontiers:
            f = frontiers.popleft()
            c -= 1
            str_to_boards(f, board)
            met.add(f)
            fneighbours = neighbours(board, met)
            if TARGET in fneighbours:
                return moves + 1
            frontiers.extend(fneighbours)
            if c == 0:
                c = len(frontiers)
                moves += 1

        return -1


def str_to_boards(s: str, board: List[List[int]]) -> None:
    i = 0
    for n in s.split("_"):
        board[i // 3][i % 3] = int(n)
        i += 1


def board_to_str(board: List[List[int]]) -> str:
    str_nums = []
    for r in board:
        for n in r:
            str_nums.append(str(n))
    return "_".join(str_nums)


def neighbours(board: List[List[int]], met: Set[str]) -> List[str]:
    rs = []
    r = 0
    c = 0
    for r in range(2):
        for c in range(3):
            if board[r][c] == 0:
                break
        else:
            continue
        break
    up, down, left, right = r - 1, r + 1, c - 1, c + 1
    if up >= 0:
        board[up][c], board[r][c] = board[r][c], board[up][c]
        s = board_to_str(board)
        if s not in met:
            rs.append(s)
        board[up][c], board[r][c] = board[r][c], board[up][c]
    if down < 2:
        board[down][c], board[r][c] = board[r][c], board[down][c]
        s = board_to_str(board)
        if s not in met:
            rs.append(s)
        board[down][c], board[r][c] = board[r][c], board[down][c]
    if left >= 0:
        board[r][left], board[r][c] = board[r][c], board[r][left]
        s = board_to_str(board)
        if s not in met:
            rs.append(s)
        board[r][left], board[r][c] = board[r][c], board[r][left]
    if right < 3:
        board[r][right], board[r][c] = board[r][c], board[r][right]
        s = board_to_str(board)
        if s not in met:
            rs.append(s)
        board[r][right], board[r][c] = board[r][c], board[r][right]

    return rs

print(Solution().slidingPuzzle([[1,2,3],[4,5,0]]))
