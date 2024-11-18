from typing import Optional

from tree_impl import TreeNode


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def nodesum(prevsum:int, root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            total = prevsum * 10 + root.val
            if root.left is None and root.right is None:
                return total
            return nodesum(total, root.left) + nodesum(total, root.right)

        return nodesum(0, root)
