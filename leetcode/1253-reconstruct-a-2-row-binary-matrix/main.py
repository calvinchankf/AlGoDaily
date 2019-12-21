"""
    1st: counting
    - fill the row1[i] and row2[i] if colsum[i] == 2
    - if colsum[i] == 1, fill the row1[i] first if upper > 0, else fill row2[i] if lower > 0
    - if the upper or lower dont exactly satisfy colsum

    Time    O(N) N: len(colsum)
    Space   O(N)
    684 ms, faster than 69.02%
"""


class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        n = len(colsum)
        row1 = n * [0]
        row2 = n * [0]
        for i in range(n):
            if colsum[i] == 2:
                if upper > 0 and lower > 0:
                    row1[i] = 1
                    row2[i] = 1
                    upper -= 1
                    lower -= 1
                else:
                    return []
        for i in range(n):
            if colsum[i] == 1:
                if upper > 0:
                    row1[i] = 1
                    upper -= 1
                elif lower > 0:
                    row2[i] = 1
                    lower -= 1
                else:
                    return []
        if upper == 0 and lower == 0:
            return [row1, row2]
        return []
