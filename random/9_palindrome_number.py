class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        new_x = int(str(x)[::-1])
        return new_x == x