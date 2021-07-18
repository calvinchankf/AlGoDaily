"""
    1st: math

    Time    O(N)
    Space   O(1)
    548 ms, faster than 50.00%
"""


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        prev = 0
        res = 0
        for x in rungs:
            diff = x - prev - 1
            res += diff // dist
            prev = x
        return res
