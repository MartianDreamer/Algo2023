from typing import Optional
from tree_impl import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        def search_parent(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if root is None or  \
                    root.left is not None and root.left.val == key   \
                    or root.right is not None and root.right.val == key \
                    or root.val == key:
                return root
            return search_parent(root.left) if root.val > key else search_parent(root.right)

        removed_parent = search_parent(root)

        if removed_parent is None:
            return root

        def go_left(parent: TreeNode, node: TreeNode) -> tuple[TreeNode, TreeNode]:
            if node.left is None:
                return (parent, node)
            return go_left(node, node.left)

        def rotate(node: TreeNode) -> Optional[TreeNode]:
            if node.left is None and node.right is None:
                return None
            if node.right is None:
                return node.left
            (replaced_parent, replaced) = go_left(node, node.right)
            if replaced_parent.left == replaced:
                replaced_parent.left = rotate(replaced)
            else:
                replaced_parent.right = rotate(replaced)
            replaced.left, replaced.right = node.left, node.right

            return replaced

        if root.val == key:
            return rotate(root)

        if removed_parent.right is not None and removed_parent.right.val == key:
            removed_parent.right = rotate(removed_parent.right)
            return root

        removed_parent.left = rotate(removed_parent.left)  # type: ignore
        return root


null = None

t = TreeNode.make_tree([20000, 10000, 30000, 5000, 15000, 25000, 35000, 2500, 7500,
                       12500, 17500, null, null, null, null, null, null, null, null, 11000, 13000])

print(Solution().deleteNode(t, 10000))
