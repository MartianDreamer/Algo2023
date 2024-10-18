from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return is_valid_bst(root)


def is_valid_bst(root: Optional[TreeNode], upper_bound: int = 2**31, lower_bound: int = -2**31 - 1) -> bool:
    if root is None:
        return True
    return (root.left is None
            or (root.left.val < root.val and root.left.val > lower_bound))    \
        and (root.right is None
             or (root.right.val > root.val and root.right.val < upper_bound))   \
        and is_valid_bst(root.left, root.val, lower_bound)    \
        and is_valid_bst(root.right, upper_bound, root.val)
