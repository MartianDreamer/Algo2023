from typing import Optional

from tree_impl import TreeNode

LEFT_OF_PARENT, RIGHT_OF_PARENT = 0, 1


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        counts = []
        def d(root: Optional[TreeNode], prev_count: int,parent_side: int):
            if root is None:
                counts.append(prev_count)
                return
            if parent_side == LEFT_OF_PARENT:
                d(root.right, 1 + prev_count, RIGHT_OF_PARENT)
                d(root.left, 0, LEFT_OF_PARENT)
            else:
                d(root.left, 1 + prev_count, LEFT_OF_PARENT)
                d(root.right, 0, RIGHT_OF_PARENT)
        d(root.left, 0, LEFT_OF_PARENT)
        d(root.right, 0, RIGHT_OF_PARENT)
        return max(counts)
