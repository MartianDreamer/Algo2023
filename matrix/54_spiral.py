from typing import List, Optional


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        STOP, UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3, 4
        upper, lower, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        def next_pos(row: int, column: int, direction: int) -> Optional[List[int]]:
            nonlocal upper, lower, left, right
            if direction == STOP:
                return None
            if direction == RIGHT:
                column += 1
                if column == right:
                    direction = DOWN
                    upper += 1
            elif direction == LEFT:
                column -= 1
                if column == left:
                    direction = UP
                    lower -= 1
            elif direction == UP:
                row -= 1
                if row == upper:
                    direction = RIGHT
                    left += 1
            else:
                row += 1
                if row == lower:
                    direction = LEFT
                    right -= 1
            if direction == LEFT and col == left:
                direction = STOP
            elif direction == RIGHT and col == right:
                direction = STOP
            elif direction == UP and row == upper:
                direction = STOP
            elif direction == DOWN and row == lower:
                direction = STOP
            return [row, column, direction]

        col, row = [0, 0]
        d = STOP
        if col < right:
            d = RIGHT
        elif row < lower:
            d = DOWN
        rs = [matrix[row][col]]
        next = next_pos(row, col, d)
        while next is not None:
            row, col, d = next
            rs.append(matrix[row][col])
            next = next_pos(row, col, d)
        return rs


print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().spiralOrder([[1]]))
