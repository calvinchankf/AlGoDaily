"""
    1st: 2 arrays
    
    Time    O(3N)
    Space   O(2N)
    172 ms, faster than 56.15% 
"""


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        forward = n * [0]
        pfs = 0
        for i in range(n):
            pfs += nums[i]
            forward[i] = pfs
        backward = n * [0]
        sfs = 0
        for i in range(n-1, -1, -1):
            sfs += nums[i]
            backward[i] = sfs
        for i in range(n):
            if forward[i] == backward[i]:
                return i
        return -1


""" 
    2nd: 
    - similar to lc238, 724
    - at every index subtract prefix sum from the right until prefix sum == suffix sum

    [1, 7, 3, 6, 5, 6]
     1  8 11 17 22 28
             17 11 6
             ^
    
    Time    O(2N)
    Space   O(1)
    108 ms, faster than 98.64%
"""


class Solution(object):
    def pivotIndex(self, nums):
        pfs = sum(nums)
        sfs = 0
        for i in range(len(nums)):
            sfs += nums[i]
            if pfs == sfs:
                return i
            pfs -= nums[i]
        return -1
