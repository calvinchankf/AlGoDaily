from typing import List
from sys import maxsize

"""
    1st: histogram
    - similar to lc85

    e.g. matrix = 
    [[1, 0, 1],
     [1, 1, 0],
     [1, 1, 0]]


    1. Find the histogram on every row, histgoram = 
    [[1, 0, 1],
     [1, 2, 0],
     [1, 2, 0]]

    2. For every row, move up and add the historgram[_i][j] to our result,
        the reason we use minimum is that when we consider this...
        [[0,0,0,1],
         [0,0,1,2],
         [0,1,2,3]]
        When we look at the bottom right corner, the width of histogram shrinks when we go up,
        it means that we can only form fewer retangles when we go up

    Time    O(RRC)
    Space   O(RC)
    828 ms, faster than 50.00%
"""


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        R, C = len(mat), len(mat[0])
        histogram = [[0] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if mat[i][j] == 1:
                    if j > 0:
                        histogram[i][j] = 1 + histogram[i][j - 1]
                    else:
                        histogram[i][j] = 1
        total = 0
        for i in range(R):
            for j in range(C):
                _i = i
                min_val = maxsize
                while _i >= 0 and histogram[_i][j] > 0:
                    min_val = min(min_val, histogram[_i][j])
                    total += min_val
                    _i -= 1
        return total


s = Solution()

a = [[1, 0, 1],
     [1, 1, 0],
     [1, 1, 0]]
print(s.numSubmat(a))

a = [[0, 1, 1, 0],
     [0, 1, 1, 1],
     [1, 1, 1, 0]]
print(s.numSubmat(a))

a = [[1, 1, 1, 1, 1, 1]]
print(s.numSubmat(a))

a = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
print(s.numSubmat(a))

a = [[0, 1], [1, 1], [1, 0]]
print(s.numSubmat(a))

a = [[1, 0, 1],
     [1, 1, 0],
     [1, 1, 1],
     [1, 1, 1]]
print(s.numSubmat(a))
