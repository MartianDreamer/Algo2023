from typing import Optional, no_type_check

from tree_impl import TreeNode


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -10**5
        frontiers = [root]
        old_frontier_len = len(frontiers)
        level_sum = 0
        level = 1
        rs = 1
        while len(frontiers) != 0:
            frontier = frontiers.pop(0)
            old_frontier_len -= 1
            level_sum += frontier.val # type: ignore
            if frontier.left is not None: # type: ignore
                frontiers.append(frontier.left) # type: ignore
            if frontier.right is not None: # type: ignore
                frontiers.append(frontier.right) # type: ignore
            if old_frontier_len == 0:
                old_frontier_len = len(frontiers)
                (rs, max_sum) = (level, level_sum) if level_sum > max_sum else (rs, max_sum)
                level += 1
                level_sum = 0
        return rs
