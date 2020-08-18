"""
    Time    O(N^2)
    Space   O(N^2)
    12 ms, faster than 98.47%
"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0:
            return []

        res = []
        for _ in range(n):
            res.append(n * [0])

        top = 0
        right = n-1
        bottom = n-1
        left = 0

        cur = 1

        while top <= bottom and left <= right:
            # go right
            for j in range(left, right+1):
                res[top][j] = cur
                cur += 1
            top += 1
            # go down
            for i in range(top, bottom+1):
                res[i][right] = cur
                cur += 1
            right -= 1
            # go left
            # top has been +1 previously, so bottom must be >= new top in order to traverse correctly
            if top <= bottom:
                for j in range(right, left-1, -1):
                    res[bottom][j] = cur
                    cur += 1
                bottom -= 1
            # go up
            # left has been +1 previously, so right must be >= new top in order to traverse correctly
            if left <= right:
                for i in range(bottom, top-1, -1):
                    res[i][left] = cur
                    cur += 1
                left += 1
        return res
