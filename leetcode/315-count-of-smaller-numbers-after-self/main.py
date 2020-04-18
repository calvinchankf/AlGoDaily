"""
    1st: binary search
    - at each index, record a sort list with binary search
    - iterate the input again to find the count of smaller numbers with with binary search

    e.g. [5,2,6,1,2]
    0: [1, 2, 2, 5, 6], <- 3
    1: [1, 2, 2, 6],    <- 1
    2: [1, 2, 6],       <- 2
    3: [1, 2],          <- 0
    4: [2]              <- 0

    Time    O(N * (logN + K))
    Spac    O(N)
    124 ms, faster than 74.46% 
"""


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sorted_arr = []
        result = []
        for num in nums[::-1]:
            idx = self.lowerBsearch(sorted_arr, num)
            result.append(idx)
            sorted_arr.insert(idx, num)

        return result[::-1]

    def lowerBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left
