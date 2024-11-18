from typing import Optional

from tree_impl import TreeNode


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = []
        self.cur_idx = 0

        def inorder(root: Optional[TreeNode]) -> None:
            if root is None:
                return
            inorder(root.left)
            self.nodes.append(root)
            inorder(root.right)

        inorder(root)

    def next(self) -> int:
        rt = self.nodes[self.cur_idx]
        self.cur_idx += 1
        return rt

    def hasNext(self) -> bool:
        return self.cur_idx < len(self.nodes)
