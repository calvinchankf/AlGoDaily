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

"""
    3rd: binary search the odd index

    e.g.1 [1,1,2,3,3,4,4]

     0 1 2 3 4 5 6
    [1,1,2,3,3,4,4]
         <- search on the left becos nums[i] == nums[i+1], nums[3] == nums[4] which is 3

    e.g.2 [1,1,2,2,3,4,4]

     0 1 2 3 4 5 6
    [1,1,2,2,3,4,4]
            -> search on the right becos nums[i] == nums[i-1], nums[3] == nums[2] which is 2

    Time    O(NlogN)
    Space   O(1)
    48 ms, faster than 98.62% 
"""
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if mid%2 == 0:
                mid += 1
            
            if mid + 1 >= len(nums):
                return nums[-1]
            
            if nums[mid] == nums[mid+1]:
                right = mid - 1
            elif nums[mid] == nums[mid-1]:
                left = mid + 1
        return nums[left]