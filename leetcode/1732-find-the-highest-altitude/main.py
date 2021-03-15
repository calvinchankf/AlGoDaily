"""
    1st: array

    Time    O(N)
    Space   O(1)
"""


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        cur = 0
        for x in gain:
            cur += x
            res = max(res, cur)
        return res
