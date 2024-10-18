from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        fix_tree(root, None, None)

def fix_tree(root: Optional[TreeNode], upper_bound_node: Optional[TreeNode], lower_bound_node: Optional[TreeNode]) -> bool:
    if root is None:
        return False
    if upper_bound_node is not None and upper_bound_node.val < root.val:
        upper_bound_node.val, root.val = root.val, upper_bound_node.val
        return True
    elif lower_bound_node is not None and lower_bound_node.val > root.val:
        lower_bound_node.val, root.val = root.val, lower_bound_node.val
        return True
    check = fix_tree(root.left, root, lower_bound_node) or fix_tree(root.right, upper_bound_node, root)
    rs = check
    while check:
        check = fix_tree(root.left, root, lower_bound_node) or fix_tree(root.right, upper_bound_node, root)
    return rs
