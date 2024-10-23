from typing import Optional

from tree_impl import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        count = 0

        def d_sum(root: Optional[TreeNode], sums: list[int], target_sum: int):
            nonlocal count
            if root is None:
                return
            
            new_sums = [sums[i] + root.val if i < len(sums) else root.val for i in range(len(sums) + 1)]
            count += new_sums.count(target_sum)

            d_sum(root.left, new_sums, target_sum)
            d_sum(root.right, new_sums, target_sum)

        d_sum(root, [], targetSum)

        return count


t = TreeNode.make_tree([0,1,1])

print(Solution().pathSum(t, 1))
