from tree_impl import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_ancestors = []

        def dfs(root: TreeNode | None, p: TreeNode) -> bool:
            if root == p:
                p_ancestors.append(root)
                return True
            if root is None:
                return False
            if dfs(root.left, p) or dfs(root.right, p):
                p_ancestors.append(root)
                return True
            return False
        
        def dfs_compare(root: TreeNode | None, q: TreeNode) -> bool:
            if root is None:
                return False
            if root == q:
                return True
            return dfs(root.left, q) or dfs(root.right, q)
        
        dfs(root, p)
        for n in p_ancestors:
            if dfs_compare(n, q):
                return n
        return None
