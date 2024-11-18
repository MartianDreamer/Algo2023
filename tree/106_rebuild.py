from typing import List, Optional

from tree_impl import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root_idx = len(postorder) - 1
        posmap = {inorder[i]: i for i in range(len(inorder))}

        def build_tree(left:int, right: int) -> Optional[TreeNode]:
            nonlocal root_idx
            if left > right:
                return None
            
            root = TreeNode(postorder[root_idx])
            root_pos = posmap[root.val]
            root_idx -= 1

            root.right = build_tree(root_pos + 1, right)
            root.left = build_tree(left, root_pos - 1)

            return root
        
        return build_tree(0, len(inorder) - 1)

