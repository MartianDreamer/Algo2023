from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) < 2:
            return 1

        candies = [0] * len(ratings)
        candies[0] = 1 if ratings[0] <= ratings[1] else 0

        i = 1

        while i < len(ratings):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
            else:
                right = i
                candy = 1
                while right + 1 < len(ratings) and ratings[right] >= ratings[right + 1]:
                    right += 1
                for j in range(right, i - 1, -1):
                    if j + 1 < len(ratings) and ratings[j] > ratings[j + 1]:
                        candy += 1
                        candies[j] += candy
                    else:
                        candy = 1
                        candies[j] = candy
                if ratings[i - 1] > ratings[i]:
                    candies[i - 1] = max(candies[i] + 1, candies[i - 1])
                i = right
            i += 1

        return sum(candies)


# print(Solution().candy([1, 2, 8, 7, 6, 5, 4, 3, 2, 1]))
print(Solution().candy([10, 10, 10, 10, 10, 10]))
