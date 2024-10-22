from typing import Optional

from tree_impl import TreeNode

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves_1 = []
        if root1 is None or root2 is None:
            return False
        dfs(root1, leaves_1)
        return dfs_compare(root2, leaves_1) and len(leaves_1) == 0

def dfs(root: TreeNode, leaves: list[int]):
    if root.left is None and root.right is None:
        leaves.append(root.val)
    if root.left is not None:
        dfs(root.left, leaves)
    if root.right is not None:
        dfs(root.right, leaves)

def dfs_compare(root: TreeNode, leaves: list[int]) -> bool:
    if root.left is None and root.right is None:
        return len(leaves) != 0 and root.val == leaves.pop(0)
    left_compare = True if root.left is None else dfs_compare(root.left, leaves)
    right_compare = True if root.right is None else dfs_compare(root.right, leaves)
    return left_compare and right_compare
