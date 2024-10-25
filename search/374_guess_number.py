n = 2


def guess(num: int) -> int:
    return -1 if num < n else 0 if num == n else 1


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1 , n
        my_guess = (left + right) // 2
        rs = guess(my_guess)
        while rs != 0:
            if rs < 0:
                right = my_guess - 1
            else:
                left = my_guess + 1
            my_guess = (left + right) // 2
            rs = guess(my_guess)
        return my_guess

print(Solution().guessNumber(2))
