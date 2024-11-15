from typing import Optional

from tree_impl import TreeNode


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return -1
        c = 1
        rs = -1
        def inorder_traversal(root: TreeNode) -> None:
            nonlocal c, rs
            if root.left is not None:
                inorder_traversal(root.left)
            if c == k:
                rs = root.val
            c+= 1
            if root.right is not None:
                return inorder_traversal(root.right)

        inorder_traversal(root)        
        return rs
        
null = None
t = TreeNode.make_tree([3,1,4,null,2])

print(Solution().kthSmallest(t, 1))