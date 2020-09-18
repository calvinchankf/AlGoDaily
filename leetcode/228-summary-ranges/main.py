"""
    1st approach: intervals
    - if the last interval ends at cur-1, we extend the last interval
    - else we create a new interval and append it to the intervals array

    Time    O(2n)
    Space   O(n)
    20 ms, faster than 99.11%
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []

        n = len(nums)
        intvs = []
        j = 0
        for i in range(1, n):
            if nums[i] > nums[i-1] + 1:
                intvs.append((nums[j], nums[i-1]))
                j = i
        intvs.append((nums[j], nums[-1]))

        res = []
        for s, e in intvs:
            if s == e:
                res.append(str(s))
            else:
                res.append(str(s) + '->' + str(e))
        return res
