from typing import List, Optional

from tree_impl import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rs = []

        def traverse(node: Optional[TreeNode], blocked: int) -> int:
            if node is None:
                return -1
            if blocked <= 0:
                rs.append(node.val)
            depth_right = 1 + traverse(node.right, blocked - 1)  # type: ignore
            depth_left = 1 + traverse(node.left, max(blocked - 1, depth_right)) # type: ignore
            return max(depth_right, depth_left)

        traverse(root, 0)

        return rs

null = None
t = TreeNode.make_tree([1,2,3,null,5,6])
print(Solution().rightSideView(t))