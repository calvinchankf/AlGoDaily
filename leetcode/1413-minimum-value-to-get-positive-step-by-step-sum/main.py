"""
    1st: prefix sum

    Time    O(N)
    Space   O(1)
    36 ms, faster than 100.00%
"""


class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minValue = 0
        cur = 0
        for num in nums:
            cur += num
            minValue = min(minValue, cur)
        return 1 - minValue
