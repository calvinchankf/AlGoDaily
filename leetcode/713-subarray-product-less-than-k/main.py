"""
    1st approach: 2 pointers
	- when the current product is >= target, substruct the items on the left hand side
	- in each iteration, count the subarray
	e.g.
	[10,5,2,6,4], 100
	for 10 => [10] = 1
	for 5 => [10,5], [5] = 2
	for 2 => [5,2], [2] = 2
	for 6 => [5,2,6], [2,6], [6] = 3
	for 4 => [2,6,4], [6,4], [4] = 3
	count = 1+2+2+3+3 = 11

	hence, for each iteration, res += i - slow + 1

    Time    O(n)
    Space   O(1)
	1028 ms, faster than 48.88%
"""


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
        res = 0
        j = 0
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            while j <= i and prod >= k:
                prod //= nums[j]
                j += 1
            res += i - j + 1
        return res
