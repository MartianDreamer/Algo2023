from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return (p is None and q is None)    \
            or (p is not None and q is not None and p.val == q.val) \
            and self.isSameTree(p.left, q.left) \
            and self.isSameTree(p.right, q.right)
