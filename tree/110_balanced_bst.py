
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    height_dict: dict[TreeNode, int] = {}

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return root is None or abs(self.height(root.left) - self.height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root in self.height_dict:
            return self.height_dict[root]
        self.height_dict[root] = 1 + \
            max(self.height(root.left), self.height(root.right))
        return self.height_dict[root]
