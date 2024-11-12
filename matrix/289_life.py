from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        copied_board = [[n for n in board[i]] for i in range(len(board))]

        def count_live_neighbours(row: int, col: int) -> int:
            rows = [row - 1, row, row + 1]
            cols = [col - 1, col, col + 1]
            rs = 0
            for r in rows:
                for c in cols:
                    if r < 0 or r >= len(copied_board) or c < 0 or c >= len(copied_board[0]):
                        continue
                    rs += copied_board[r][c]
            return rs - copied_board[row][col]
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                count_live = count_live_neighbours(r, c)
                if board[r][c] == 1:
                    if count_live < 2:
                        board[r][c] = 0
                    if count_live > 3:
                        board[r][c] = 0
                elif count_live == 3:
                    board[r][c] = 1
        
print(Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))