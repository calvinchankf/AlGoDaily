"""
    1st: math

    idea: [ 1, 4, 6, 8, 10]
    diff    0  3  5  7  9
           -3  0  2  4  6 <- all -3
           -5 -2  0  2  4 <- all -2
           -7 -4 -2  0  2 <- all -2
           -9 -6 -4 -2  0 <- all -2
    on every row, the result is the sum of all abs(nums[i])

    Time    O(N)
    Space   O(N)
    864 ms, faster than 100.00%
"""


class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        total = 0
        for i in range(1, n):
            total += nums[i] - nums[0]
        res = n * [0]
        res[0] = total
        for i in range(1, n):
            diff = nums[i] - nums[i-1]
            total = total - (n - i) * diff + i * diff
            res[i] = total
        return res
