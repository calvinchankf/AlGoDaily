from typing import List
import sys

"""
    1st: min max

    Time    O(N)
    Space   O(1)
    36 ms, faster than 25.00%
"""


class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        dip = sys.maxsize
        peak = -sys.maxsize
        total = 0
        for x in salary:
            dip = min(dip, x)
            peak = max(peak, x)
            total += x
        return (total - peak - dip) / (n - 2)
