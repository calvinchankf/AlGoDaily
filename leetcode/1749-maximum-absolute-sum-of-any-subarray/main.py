"""
    1st: dp: kadan's algorithm
    - similar to lc53

    Time    O(N)
    Space   O(1)
    552 ms, faster than 100.00%
"""


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        minSubSum = 2**32
        maxSubSum = -(2**32)
        curMin = 2**32
        curMax = -(2**32)
        for x in nums:
            curMin = min(curMin + x, x)
            minSubSum = min(minSubSum, curMin)
            curMax = max(curMax + x, x)
            maxSubSum = max(maxSubSum, curMax)
        return max(abs(minSubSum), abs(maxSubSum))
