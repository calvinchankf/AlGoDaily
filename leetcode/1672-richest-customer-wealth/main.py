"""
    1st:

    Time    O(MN)
    Space   O(1)
    60ms
"""


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        for acc in accounts:
            res = max(res, sum(acc))
        return res
