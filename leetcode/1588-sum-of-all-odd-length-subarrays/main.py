"""
    1st: brute force

    Time    O(N^2)
    Space   O(1)
    60 ms, faster than 33.33%
"""


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += arr[j]
                if (j-i+1) % 2 == 1:
                    res += total
        return res
