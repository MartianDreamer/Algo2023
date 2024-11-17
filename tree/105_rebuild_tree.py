from typing import Dict, List, Optional

from tree_impl import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        posdict = {inorder[i]: i for i in range(len(inorder))}
        root_idx = 0

        def list_to_tree(left:int, right:int) -> Optional[TreeNode]:
            nonlocal root_idx
            if left > right:
                return None
            
            root = TreeNode(preorder[root_idx])
            root_pos = posdict[root.val]
            root_idx += 1
            root.left = list_to_tree(left, root_pos - 1)
            root.right = list_to_tree(root_pos + 1, right)
            return root
        
        return list_to_tree(0, len(inorder) - 1)
