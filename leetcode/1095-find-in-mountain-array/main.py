# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

"""
    1st: binary searches
    1. find the peak
    2. find the target on the left hand side
    3. find the target on right hand side if necessary

    Time    O(2logN) -> O(3NlogN)
    Space   O(1)
    28 ms, faster than 76.53%
"""


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        # 1: find the peak
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            cur = mountain_arr.get(mid)
            curNext = mountain_arr.get(mid+1)
            if cur < curNext:
                left = mid + 1
            else:
                right = mid
        peak = left
        # 2: find the target on the left hand side
        left = 0
        right = peak
        while left <= right:
            mid = (left + right) // 2
            temp = mountain_arr.get(mid)
            if target < temp:
                right = mid - 1
            elif target > temp:
                left = mid + 1
            else:
                return mid
        # 3: find the target on right hand side if necessary
        left = peak
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            temp = mountain_arr.get(mid)
            if target < temp:
                left = mid + 1
            elif target > temp:
                right = mid - 1
            else:
                return mid
        return -1
