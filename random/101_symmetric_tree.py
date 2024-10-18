# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        return is_symmetric(root.left, root.right)
    
def is_symmetric(p: Optional[TreeNode], q: Optional[TreeNode]):
    return (p is None and q is None)    \
        or (p is not None and q is not None and p.val == q.val) \
        and is_symmetric(p.left, q.right)   \
        and is_symmetric(p.right, q.left)

