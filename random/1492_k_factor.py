from math import sqrt


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                factors.append(i)
                if n // i != i:
                    factors.append(n//i)

        if len(factors) % 2 == 1:
            pos = (k - 1) * 2 if (k - 1) <= len(factors) // 2 else - \
                (k - 1 - len(factors) // 2) * 2
        else:
            pos = (k - 1) * 2 if k <= len(factors) // 2 else -1 - (k - 1 - len(factors) // 2) * 2

        return factors[pos] if k <= len(factors) else -1

