"""
    1st: math

    Time    O(1)
    Space   O(1)
    28 ms, faster than 100.00%
"""


class Solution:
    def minOperations(self, n: int) -> int:
        last = (n-1)*2+1
        mid = (1 + last)//2
        diff = last - mid
        m = diff//2
        if n % 2 == 1:
            return (1 + m) * m
        return (1 + m)*m + m + 1
