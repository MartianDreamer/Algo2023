from typing import List, Optional

from tree_impl import TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        nodes = [TreeNode(n) for n in nums]
        root = nodes[0]
        for i in range(1, len(nodes)):
            if nodes[i - 1].val < nodes[i].val:
                parent, child = None, nodes[i - 1]
                for j in range(i - 1, -1, -1):
                    if nodes[j].val > nodes[i].val:
                        parent = nodes[j]
                        break
                    if nodes[j].val > child.val:
                        child = nodes[j]
                nodes[i].left = child
                if parent is not None:
                    parent.right = nodes[i]
            else:
                nodes[i - 1].right = nodes[i]
            if nodes[i].val > root.val:
                root = nodes[i]
        
        return root
