"""
    1st: sort

    Time    O(NlogN)
    Space   O(1)
    48 ms, faster than 100.00% 
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return (nums[-2]-1) * (nums[-1]-1)
