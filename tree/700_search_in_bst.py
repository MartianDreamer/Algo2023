from typing import Optional

from tree_impl import TreeNode


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or root.val == val:
            return root
        return self.searchBST(root.left, val) if root.val > val else self.searchBST(root.right, val)
