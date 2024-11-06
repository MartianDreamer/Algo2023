from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        group_by_bit_count: List[List[int]] = []

        cur_bit = 0
        for n in nums:
            bit_count = int.bit_count(n)
            if bit_count != cur_bit:
                cur_bit = bit_count
                group_by_bit_count.append([n])
                continue
            group_by_bit_count[-1].append(n)

        sorted_groupby = []
        for g in group_by_bit_count:
            g.sort()
            sorted_groupby.extend(g)
        for n,m  in zip(sorted_groupby, sorted_groupby[1:]):
            if m < n:
                return False
        return True


print(Solution().canSortArray([8,4,2,30,15]))