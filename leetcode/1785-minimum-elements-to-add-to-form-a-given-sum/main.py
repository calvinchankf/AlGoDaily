
from math import ceil
"""
    1st: math
    - sum nums
    - calculate the diff
    - answer = diff / limit

    Time    O(N)
    Space   O(1)
    740 ms, faster than 100.00%
"""
class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        total = sum(nums)
        diff = abs(goal - total)
        return ceil(diff / limit)