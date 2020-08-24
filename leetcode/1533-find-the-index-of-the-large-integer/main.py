# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

"""
    1st: binary search

    Time    O(logN)
    Space   O(1)
    340 ms, faster than 100.00%
"""


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        left = 0
        right = reader.length() - 1
        while left < right:
            mid = (left + right) // 2
            n = right - left + 1
            if n % 2 == 0:
                b = reader.compareSub(left, mid, mid+1, right)
                if b == -1:
                    left = mid + 1
                elif b == 1:
                    right = mid
                else:
                    return mid
            else:
                b = reader.compareSub(left, mid-1, mid+1, right)
                if b == -1:
                    left = mid + 1
                elif b == 1:
                    right = mid - 1
                else:
                    return mid
        return left
