from typing import List

EMPTY, STONE, BLOCK = ".", "#", "*"

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        rotated_box = [["."] * m for _ in range(n)]

        stones = []

        for i in range(m):
            for new_row in range(n):
                cloned_object = box[i][new_row]
                new_col = m - 1 -i
                rotated_box[new_row][new_col] = cloned_object
                if cloned_object == STONE:
                    stones.append((new_row, new_col))

        stones.sort(key=lambda e: e[0], reverse=True)

        for r, c in stones:
            fall(r, c, rotated_box)
        
        return rotated_box

def fall(r: int, c:int, box:List[List[str]]) -> None:
    pos: int = r
    for i in range(r + 1, len(box)):
        if box[i][c] != EMPTY:
            break
        pos = i
    box[r][c], box[pos][c] = EMPTY, STONE



for r in Solution().rotateTheBox([["*","#","*",".",".",".","#",".","*","."]]):
    print(r)
