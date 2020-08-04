"""
    1st: sort

    Time    O(NlogN)
    Space   O(1)
    52 ms, faster than 66.67%
"""


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        n = len(arr)
        diff = None
        for i in range(1, n):
            if diff == None:
                diff = arr[i] - arr[i-1]
            elif arr[i] - arr[i-1] != diff:
                return False
        return True
