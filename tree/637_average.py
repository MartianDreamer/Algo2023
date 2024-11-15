from typing import List, Optional

from tree_impl import TreeNode


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        
        border = [root]
        bcount = 1
        rs: List[float] = [root.val]

        def bfs():
            nonlocal bcount
            while len(border) > 0:
                if bcount == 0:
                    bcount = len(border)
                    rs.append(sum([b.val for b in border])/bcount)
                frontier = border.pop(0)
                bcount -= 1
                if frontier.left is not None:
                    border.append(frontier.left)
                if frontier.right is not None:
                    border.append(frontier.right)

        bfs()
        return rs

t = TreeNode.make_tree([3,9,20,30,35,15,7])
print(Solution().averageOfLevels(t))