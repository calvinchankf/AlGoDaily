"""
    2nd approach
	- for earch item in the array, cache the sum from start

	Time of Constructor O(n)
	Space of Constructor O(n)
	Time of SumRange O(1)
	Space of SumRange O(1)
	68 ms, faster than 67.78%
"""


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        pfs = 0
        self.pfss = []
        for i in range(len(nums)):
            pfs += nums[i]
            self.pfss.append(pfs)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.pfss[j]
        return self.pfss[j] - self.pfss[i-1]
