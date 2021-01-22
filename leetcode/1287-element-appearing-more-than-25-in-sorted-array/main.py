from collections import *

"""
    1st: hashtable
    - record count of each number
    - afterall, check if there is one number appears more than 25%

    Time        O(N)
    Space       O(N)
    80 ms, faster than 56.29%
"""


class Solution(object):
    def findSpecialInteger(self, arr):
        counter = Counter(arr)
        for key in counter:
            if counter[key] > len(arr) / 4:
                return key


"""
    2nd: binary search
    - for number at indices (0, n/4, n/2, 3n/4), find their first and last occurence index
    - and check if the range is more than 25% of the length of the input array

    Time    O(4logN)
    Space   O(1)
    76 ms, faster than 45.79%
"""


class Solution(object):
    def findSpecialInteger(self, arr):
        n = len(arr)
        if n == 1:
            return arr[0]
        indices = [0, n//4, n//2, 3*n//4]
        for i in indices:
            left = self.lowerBsearch(arr, arr[i])
            right = left + n//4
            if arr[left] == arr[right]:
                return arr[i]

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
