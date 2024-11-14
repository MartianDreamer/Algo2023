from typing import List, Set

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def check(r: int, c: int, w_idx: int) -> bool:
            visited: Set[int] = set()
            if board[r][c] != word[w_idx]:
                return False
            elif w_idx == len(word) - 1:
                return True
            board[r][c] = "."
            neighbours = find_neighbors(r, c, r_n, c_n, visited)
            rs = False
            for nr, nc in neighbours:
                visited.add(nr * 10 + nc)
                rs = rs or check(nr, nc, w_idx + 1)
            if not rs:
                board[r][c] = word[w_idx]
            return rs

        r_n = len(board)
        c_n = len(board[0])
        for r in range(r_n):
            for c in range(c_n):
                if board[r][c] != word[0]:
                    continue
                if check(r, c, 0):
                    return True
        return False


def find_neighbors(
    r: int, c: int, r_n: int, c_n: int, visited: Set[int]
) -> List[List[int]]:
    potential_neighbours = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]
    return [
        [r, c]
        for r, c in potential_neighbours
        if r >= 0 and r < r_n and c >= 0 and c < c_n and (r * 10 + c) not in visited
    ]
