"""
    classic approach:
    - bottom up dynamic programming 
    - select the path with min cost from bottom to top, mutate the input array
    Time	O(n)
    Space	O(1)
    24 ms, faster than 91.10%
"""


class Solution(object):
    def minimumTotal(self, triangle):
        if len(triangle) == 0 or len(triangle[0]) == 0:
            return 0
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] = min(
                    triangle[i+1][j], triangle[i+1][j+1]) + triangle[i][j]
        return triangle[0][0]
