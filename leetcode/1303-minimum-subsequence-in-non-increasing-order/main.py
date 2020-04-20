"""
    1st: sort

    Time    O(NlogN)
    Space   O(N)
    44 ms, faster than 94.35%
"""


class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = sum(nums)
        arr = sorted(nums, reverse=True)
        prefixSum = 0
        temp = []
        for x in arr:
            prefixSum += x
            temp.append(x)
            if prefixSum > total - prefixSum:
                return temp
