import sys

"""
    1st: array
    - for each position, move all chips to here and see how much does it cost

    Time    O(N^2)
    Space   O(N^2)
    52 ms, faster than 5.48%
"""


class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        res = sys.maxsize
        for i in range(len(chips)):
            cost = 0
            for j in range(len(chips)):
                if i == j or chips[i] == chips[j]:
                    continue
                diff = abs(chips[i] - chips[j])
                if diff % 2 == 1:
                    cost += 1
            res = min(res, cost)
        return res
