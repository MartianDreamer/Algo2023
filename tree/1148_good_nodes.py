from tree_impl import TreeNode

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return dfs_check_good_node(root, -10**4-1)
    
def dfs_check_good_node(root: TreeNode, greatest: int) -> int:
    rs = 1 if root.val >= greatest else 0
    if root.left is not None:
        rs += dfs_check_good_node(root.left, max(root.val, greatest))
    if root.right is not None:
        rs += dfs_check_good_node(root.right, max(root.val, greatest))
    return rs

t = TreeNode.make_tree([3,1,4,3,None,1,5])

print(Solution().goodNodes(t)) # type: ignore