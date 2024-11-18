from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft: Node | None = topLeft
        self.topRight: Node | None = topRight
        self.bottomLeft: Node | None = bottomLeft
        self.bottomRight: Node | None = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def check_grid(rstart, rend, cstart, cend) -> bool:
            prev_c = grid[rstart][cstart]
            for r in grid[rstart:rend]:
                for c in r[cstart:cend]:
                    if c != prev_c:
                        return False
            return True

        def build(rstart: int, rend: int, cstart: int, cend: int) -> Node:
            if check_grid(rstart, rend, cstart, cend):
                return Node(grid[rstart][cstart], 1, None, None, None, None)
            rsplit = (rstart + rend) // 2
            csplit = (cstart + cend) // 2
            root = Node(1, 0, None, None, None, None)
            root.topLeft = build(rstart, rsplit, cstart, csplit)
            root.topRight = build(rstart, rsplit, csplit, cend)
            root.bottomLeft = build(rsplit, rend, cstart, csplit)
            root.bottomRight = build(rsplit, rend, csplit, cend)
            return root
        
        return build(0, len(grid), 0, len(grid))

print(Solution().construct([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]))