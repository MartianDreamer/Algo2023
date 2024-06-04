class Solution(object):
    def maxSubArray(self, nums):
        maxSoFar, maxEndingHere = -10**4, 0
        for num in nums:
            maxEndingHere += num
            if maxSoFar < maxEndingHere:
                maxSoFar = maxEndingHere
            if maxEndingHere < 0:
                maxEndingHere = 0
        return maxSoFar

