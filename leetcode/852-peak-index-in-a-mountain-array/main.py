"""
    1st: linear search the largest element

    Time    O(N)
    Space   O(N)
    96 ms, faster than 21.10%
"""


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return A.index(max(A))


"""
    2nd: upper boundy binary search

    Time    O(logN)
    Space   O(1)
    112 ms, faster than 14.14%
"""


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left = 0
        right = len(A)
        while left < right:
            mid = (left + right)//2
            if A[mid-1] < A[mid]:
                left = mid + 1
            else:
                right = mid
        return right - 1
