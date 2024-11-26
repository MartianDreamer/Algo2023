from typing import Dict, Optional, Tuple

from tree_impl import TreeNode
from __data import param
from sys import setrecursionlimit

setrecursionlimit(1000000)


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        sum_ht: Dict[TreeNode, int] = {}

        def max_sum(root: TreeNode) -> int:
            if root in sum_ht:
                return sum_ht[root]
            if root.left is None and root.right is None:
                sum_ht[root] = root.val
                return root.val
            if root.left is not None and root.right is None:
                rs = max(root.val, root.val + max_sum(root.left))
                sum_ht[root] = rs
                return rs
            if root.left is None and root.right is not None:
                rs = max(root.val, root.val + max_sum(root.right))
                sum_ht[root] = rs
                return rs
            rs = max(root.val, root.val + max(max_sum(root.left), max_sum(root.right)))  # type: ignore
            sum_ht[root] = rs
            return rs

        def max_path(root: TreeNode) -> int:
            if root.left is None and root.right is None:
                return root.val
            if root.left is not None and root.right is None:
                return max(root.val, root.val + max_sum(root.left), max_path(root.left))
            if root.left is None and root.right is not None:
                return max(
                    root.val, root.val + max_sum(root.right), max_path(root.right)
                )
            return max(
                root.val,
                root.val + max_sum(root.left),  # type: ignore
                root.val + max_sum(root.right),  # type: ignore
                root.val + max_sum(root.left) + max_sum(root.right),  # type: ignore
                max_path(root.left),  # type: ignore
                max_path(root.right),  # type: ignore
            )

        if root is None:
            return 0
        max_sum(root)
        return max_path(root)


null = None
t = TreeNode.make_tree([5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1])
t2 = TreeNode.make_tree(param)
print(Solution().maxPathSum(t2))
