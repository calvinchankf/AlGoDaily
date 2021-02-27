"""
    1st: sort by unit

    Time    O(NlogN)
    Space   O(1)
    156 ms, faster than 100.00%
"""


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        res = 0
        boxTypes.sort(key=lambda x: -x[1])
        for n, u in boxTypes:
            if truckSize >= 0:
                count = min(truckSize, n)
                res += count * u
                truckSize -= count
        return res
