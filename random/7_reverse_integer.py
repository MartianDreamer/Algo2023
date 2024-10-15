class Solution:
    def reverse(self, x: int) -> int:
        weight = 1
        if x < 0:
            x = -x
            weight = -1
        new_x_str = str(x)[::-1]
        new_x = int(new_x_str) * weight
        if new_x > 2**31 - 1:
            return 0
        elif new_x < -2**31:
            return 0
        else:
            return new_x
