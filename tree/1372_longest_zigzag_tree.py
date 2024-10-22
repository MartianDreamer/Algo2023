from typing import Optional

from tree_impl import TreeNode



class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_val = 0
        def dfs_left(root: Optional[TreeNode], prev_count: int):
            if root is None:
                nonlocal max_val
                max_val = max(max_val, prev_count)
                return
            dfs_right(root.right, 1 + prev_count)
            dfs_left(root.left, 0)
        
        def dfs_right(root: Optional[TreeNode], prev_count: int):
            if root is None:
                nonlocal max_val
                max_val = max(max_val, prev_count)
                return
            dfs_left(root.left, 1 + prev_count)
            dfs_right(root.right, 0)

        dfs_left(root.left, 0)
        dfs_right(root.right, 0)
        return max_val
