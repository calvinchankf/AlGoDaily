from collections import Counter

"""
    1st: hashtable

    Time    O(RC)
    Time    O(R+C)
    260 ms, faster than 100.00%
"""


class Solution(object):
    def numSpecial(self, mat):
        row_ht = Counter()
        col_ht = Counter()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    row_ht[i] += 1
                    col_ht[j] += 1
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and row_ht[i] == 1 and col_ht[j] == 1:
                    res += 1
        return res
