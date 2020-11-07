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
    - similar to lc162, 852

    Time    O(logN)
    Space   O(1)
    68 ms, faster than 93.13%
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
        if right-1 < 0:
            return 0
        return right - 1
