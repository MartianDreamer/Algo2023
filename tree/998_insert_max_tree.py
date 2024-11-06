from typing import Optional
from tree_impl import TreeNode

class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return root
        node = TreeNode(val)
        left, right = root.left, root.right
        if val > root.val:
            node.left = root
            return node
        if right is None or val > right.val:
            node.left = right
            root.right = node
        elif val <= right.val:
            self.insertIntoMaxTree(right, val)
        return root
