from typing import Dict, List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if max(nums) >= k:
            return 1
        subarr_or: List[Dict[int, int]] = [{nums[0]: 1}]
        for n in nums[1:]:
            d: Dict[int, int] = {n: 1}
            for key, value in subarr_or[-1].items():
                val = n | key
                if val not in d:
                    d[val] = value + 1
                if val >= k:
                    break
            subarr_or.append(d)

        print(subarr_or)
        rs = 2 * 10**5 + 1

        for d in subarr_or:
            for key, val in d.items():
                if key < k:
                    continue
                rs = min(val, rs)
        return rs if rs != 2 * 10**5 + 1 else -1
