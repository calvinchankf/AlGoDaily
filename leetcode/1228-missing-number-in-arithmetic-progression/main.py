"""
    1st: math

    Time    O(N)
    Space   O(N)
    60 ms, faster than 14.07%
"""


class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        minDiff = sys.maxsize
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if abs(diff) < abs(minDiff):
                minDiff = diff
        for i in range(1, len(arr)):
            diff = arr[i] - arr[i-1]
            if abs(diff) != abs(minDiff):
                return arr[i-1] + minDiff
        return arr[-1] + minDiff
