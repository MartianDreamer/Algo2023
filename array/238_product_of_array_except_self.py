from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        prefixProduct = [1]
        suffixProduct = [1]
        for e in nums[:len(nums) - 1]:
            product *= e
            prefixProduct.append(product)
        product = 1
        for e in reversed(nums[1:]):
            product *= e
            suffixProduct.insert(0, product)
        return [prefixProduct[i] * suffixProduct[i] for i in range(len(nums))]
