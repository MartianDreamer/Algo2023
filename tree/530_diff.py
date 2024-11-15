# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
from typing import Optional

from tree_impl import TreeNode


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return sys.maxsize
        rs = root.val
        if root.left is not None:
            rs = min(rs, root.val - most_right(root.left).val, self.getMinimumDifference(root.left))
        if root.right is not None:
            rs = min(rs, most_left(root.right).val - root.val, self.getMinimumDifference(root.right))
        return rs


def most_right(root: TreeNode) -> TreeNode:
    while root.right is not None:
        root = root.right
    return root

def most_left(root: TreeNode) -> TreeNode:
    while root.left is not None:
        root = root.left
    return root

null = None

t = TreeNode.make_tree([1,0,48,null,null,12,49])
print(Solution().getMinimumDifference(t))