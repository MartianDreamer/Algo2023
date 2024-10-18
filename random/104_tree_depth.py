# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return max_depth(root, 0)


def max_depth(r: Optional[TreeNode], d: int) -> int:
    if r is not None:
        d += 1
        return max(max_depth(r.left, d), max_depth(r.right, d))
    else:
        return d
