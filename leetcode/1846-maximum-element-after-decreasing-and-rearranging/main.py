"""
    1st: sort

    Time    O(NlogN)
    Space   O(1)
    508 ms, faster than 100.00%
"""


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        n = len(arr)
        if arr[0] != 1:
            arr[0] = 1
        for i in range(1, n):
            if arr[i] - arr[i-1] > 1:
                arr[i] = arr[i-1] + 1
        return arr[-1]
