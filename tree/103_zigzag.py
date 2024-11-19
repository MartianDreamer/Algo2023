from typing import List, Optional

from tree_impl import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        rs = [[root.val]]
        frontiers = [root]
        lcount = 1
        level = 0
        while frontiers:
            f = frontiers.pop(0)
            lcount -= 1
            if f.left is not None:
                frontiers.append(f.left)
            if f.right is not None:
                frontiers.append(f.right)
            if lcount == 0:
                lcount = len(frontiers)
                level += 1
                rs.append(
                    [f.val for f in frontiers]
                    if level % 2 == 0
                    else [f.val for f in reversed(frontiers)]
                )
        return rs
