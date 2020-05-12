"""
    1st: brute force
    
    Time    O(N)
    Space   O(1)
    60ms beats 49.91%
"""
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i+1 < len(nums):
            if nums[i] != nums[i+1]:
                return nums[i]
            i += 2
        return nums[i]

"""
    2nd: XOR

    Time    O(N)
    Space   O(1)
    60 ms, faster than 49.41% 
"""
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res = res^num
        return res