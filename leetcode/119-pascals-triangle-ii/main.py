"""
    naive approach

    Time    O(N^2)
    Space   O(N)
    16 ms, faster than 84.81%
"""


class Solution(object):
    def getRow(self, rowIndex):
        n = rowIndex + 1
        if n < 1:
            return []
        res = []
        for i in range(1, n+1):
            row = i * [1]
            for j in range(1, i-1):
                row[j] = res[j-1] + res[j]
            res = row
        return res
