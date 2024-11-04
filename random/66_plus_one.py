from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus_val = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += plus_val
            if digits[i] > 9:
                digits[i] = 0
                plus_val = 1
                continue
            plus_val = 0
        if plus_val == 1:
            digits.insert(0, 1)
        return digits
