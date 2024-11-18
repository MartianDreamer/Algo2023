from typing import Optional, no_type_check

from tree_impl import TreeNode



class Solution:
    @no_type_check
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        root_idx = 1
        while root.left is not None or root.right is not None:
            if height_of(root.left) > height_of(root.right):
                root_idx *= 2
                root = root.left
            else:
                root_idx = root_idx * 2 + 1
                root = root.right
            
        return root_idx

def height_of(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    cur = root
    h = 0
    while cur is not None:
        cur = cur.left
        h += 1
    return h
