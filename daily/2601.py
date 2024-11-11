from typing import List


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= nums[i + 1]:
                n = find_prime(nums[i], nums[i] - nums[i + 1])
                if n == None:
                    return False
                nums[i] -= n
        return True


def find_prime(upper: int, lower: int) -> int | None:
    for n in range(lower + 1, upper):
        if is_prime(n):
            return n
    return None


def is_prime(n: int) -> bool:
    if n == 1:
        return False
    if 1 < n <= 3:
        return True
    c = 0
    for i in range(2, n//2 + 1):
        if n % i == 0:
            c += 1
        if c >= 1:
            return False
    return True


print(Solution().primeSubOperation([5,13,4,13]))
