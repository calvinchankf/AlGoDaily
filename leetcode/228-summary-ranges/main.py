"""
    1st approach: intervals
    - if the last interval ends at cur-1, we extend the last interval
    - else we create a new interval and append it to the intervals array

    Time    O(2n)
    Space   O(n)
    32 ms, faster than 63.89%
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []

        intvs = []
        i = 0
        for j in range(1, len(nums)):
            if nums[j-1] + 1 < nums[j]:
                intvs.append((i, j-1))
                i = j
        intvs.append((i, len(nums)-1))

        res = []
        for i, j in intvs:
            if i == j:
                res.append(str(nums[i]))
            else:
                res.append(str(nums[i]) + "->" + str(nums[j]))
        return res
