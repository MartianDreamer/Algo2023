from typing import Dict, List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp: Dict[str, int] = {}
        # find a subset with sum subset == sum(nums) / 2

        def subtract(total:int, idx: int) -> int:
            if total <= target:
                return total
            total -= nums[idx]
            rem = nums[idx]
            dp[str(idx)] = rem
            nums[idx] = - 1
            prev = [str(i) for i in range(len(nums)) if nums[i] == -1]
            k = "_".join(prev)
            if k in dp:
                return dp[k]
            rs = total
            dp[k] = total
            for i in range(idx + 1, len(nums)):
                if nums[i] == -1:
                    continue
                if subtract(total, i) == target:
                    return target
            nums[idx] = rem
            return rs

        for i in range(len(nums)):
            if subtract(total, i) == target:
                return True
        
        return False



print(Solution().canPartition([14, 9, 8, 4, 3, 2]))
