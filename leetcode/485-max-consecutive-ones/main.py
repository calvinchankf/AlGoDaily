"""
    1st approach:
    1. for each num, count the number of consecutive ones
    2. after count, compare with the intermediate result
    3. the final intermediate result is the reuslt

    Time    O(N)
    Space   O(1)
    352 ms, faster than 76.16%
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        cur = 0
        for x in nums:
            if x == 1:
                cur += 1
            else:
                cur = 0
            res = max(res, cur)
        return res
