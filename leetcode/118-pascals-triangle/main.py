"""
    1st approach:
	- intuitive approach inspired by the desc
    
	Time		O(N^2)
	Space		O(N^2) the result
	32 ms, faster than 53.50%
"""


class Solution(object):
    def generate(self, numRows):
        n = numRows
        if n < 1:
            return []
        res = []
        for i in range(1, n+1):
            row = i * [1]
            for j in range(1, i-1):
                row[j] = res[-1][j-1] + res[-1][j]
            res.append(row)
        return res
