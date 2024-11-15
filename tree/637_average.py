from typing import List, Optional

from tree_impl import TreeNode


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []

        border = [root]
        bcount = 1
        rs: List[float] = [root.val]
        total = 0

        while len(border) > 0:
            if bcount == 0:
                bcount = len(border)
                rs.append(total/bcount)
                total = 0
            frontier = border.pop(0)
            bcount -= 1
            if frontier.left is not None:
                border.append(frontier.left)
                total += frontier.left.val
            if frontier.right is not None:
                border.append(frontier.right)
                total += frontier.right.val

        return rs
