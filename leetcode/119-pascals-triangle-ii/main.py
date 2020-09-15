"""
    naive approach

    Time    O(n!)
    Space   O(n)
    20 ms, faster than 77.84%
"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        nums = [1]
        for i in range(1, rowIndex+1):
            temp = (i+1) * [1]
            for j in range(1, len(temp)-1):
                temp[j] = nums[j-1] + nums[j]
            nums = temp
        return nums
