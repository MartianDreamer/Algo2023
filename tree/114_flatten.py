from typing import Optional

from tree_impl import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        left = right_most(root.left)
        if left is not None:
            left.right = root.right
            root.right = root.left
            root.left = None
    

def right_most(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return root
    while root.right is not None:
        root = root.right
    return root
