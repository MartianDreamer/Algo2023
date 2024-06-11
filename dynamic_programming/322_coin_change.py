from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        mem = dict()
        for num in coins:
            mem[num] = 1
        return self.__coinChange(mem, coins, amount)

    def __coinChange(self, mem: dict, coins: List[int], amount: int) -> int:
        if amount in mem:
            return mem[amount]
        mem[amount] = -1
        minStep = -1
        for coin in coins:
            if amount - coin < 0:
                continue
            preStep = self.__coinChange(mem, coins, amount - coin)
            if preStep == -1:
                continue
            minStep = preStep if minStep == -1 or minStep > preStep else minStep
        if minStep > -1:
            mem[amount] = 1 + minStep
        return mem[amount]

print(Solution().coinChange([2,5,10,1], 27))