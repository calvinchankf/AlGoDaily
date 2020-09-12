"""
    very bad description

    Time    O(N)
    Space   O(N)
    56 ms, faster than 68.38% 
"""


class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        i = 0
        while i < len(nums):
            freq, val = nums[i], nums[i+1]
            res = res + freq * [val]
            i += 2
        return result
