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
        l = check_left_tree(root.left)
        return check_right_tree(root.right, l)


def check_left_tree(root: Optional[TreeNode]) -> List[int | None]:
    if root is None:
        return [None]
    result: List[int | None] = [root.val]
    result.extend(check_left_tree(root.left))
    result.extend(check_left_tree(root.right))
    return result


def check_right_tree(root: Optional[TreeNode], l: List[int | None]) -> bool:
    val = l.pop(0)
    return (val is None and root is None) or (root is not None and val == root.val) and check_right_tree(root.right, l) and check_right_tree(root.left, l)


def list_to_tree(l: List[int | None]) -> Optional[TreeNode]:
    tree_nodes = [TreeNode(n) if n is not None else None for n in l]
    for i in range(len(tree_nodes)//2):
        if tree_nodes[i] is None:
            continue
        tree_nodes[i].left = tree_nodes[i*2 + 1]  # type: ignore
        tree_nodes[i].right = tree_nodes[i*2 + 2]  # type: ignore
    return None if len(tree_nodes) == 0 else tree_nodes[0]


tree = list_to_tree([1, 2, 2, 3, 4, 4, 3])

print(Solution().isSymmetric(tree))
