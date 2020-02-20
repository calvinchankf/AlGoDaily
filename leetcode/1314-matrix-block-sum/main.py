from typing import List

"""
    1st: prefix sum
    e.g.
    [
        [ 1, 2, 3, 4],
        [ 5, 6, 7, 8],
        [ 9,10,11,12],
        [13,14,15,16],
    ]
    prefix sums =
    [
        [ 1,  3,  6, 10], 
        [ 5, 11, 18, 26], 
        [ 9, 19, 30, 42], 
        [13, 27, 42, 58],
    ]

    now, u see that for every cell, pattern to calculate the block sum is
    res[i][j] += prefSums[cur][j+K] - prefSums[cur][j-K-1]

    then we just have to deal with the corner cases by calculating the bound of the prefSums[][]
    i.e. i+K, i-K, j-K, j+K

    Time    O(RC * 2K)
    Space   O(RC)
    436 ms, faster than 14.68%
"""


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        r = len(mat)
        c = len(mat[0])
        prefSums = [c * [0] for _ in range(r)]
        for i in range(r):
            prevSum = 0
            for j in range(c):
                prevSum += mat[i][j]
                prefSums[i][j] = prevSum
        res = [c * [0] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                top = max(0, i-K)
                bottom = min(r-1, i+K)
                left = max(0, j-K)
                right = min(c-1, j+K)
                for k in range(top, bottom+1):
                    res[i][j] += prefSums[k][right] \
                        - (prefSums[k][left-1] if left-1 >= 0 else 0)
        return res


s = Solution()
a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
print(s.matrixBlockSum(a, 1))

"""
    2nd: dynamic programming
    - similar to the 1st approach but in a 2D fashion

    prefix sums =
    [
        [0, 0, 0, 0, 0],
        [0, 1, 3, 6, 10],
        [0, 6, 14, 24, 36],
        [0, 15, 33, 54, 78],
        [0, 28, 60, 96, 136],
    ]

    now, u see that for every cell, pattern to calculate the block sum is
    res[i][j] += areaSums[i+K][j+K] - areaSums[i-K-1][j+K] - areaSums[i+K][j-K-1] + areaSums[i-K-1][j-K-1]

    ref:
    - https://leetcode.com/problems/matrix-block-sum/discuss/482730/Python-O(-m*n-)-sol.-based-on-integral-image-technique.-90%2B-With-explanation

    Time    O(RC)
    Space   O(RC)
    108 ms, faster than 82.54%
"""


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        r = len(mat)
        c = len(mat[0])
        areaSums = [c * [0] for _ in range(r)]
        for i in range(r):
            prevSum = 0
            for j in range(c):
                prevSum += mat[i][j]
                areaSums[i][j] = prevSum \
                    + (areaSums[i-1][j] if i-1 >= 0 else 0)

        res = [c * [0] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                top = max(0, i-K)
                bottom = min(r-1, i+K)
                left = max(0, j-K)
                right = min(c-1, j+K)
                res[i][j] = areaSums[bottom][right] \
                    - (areaSums[top-1][right] if top-1 >= 0 else 0) \
                    - (areaSums[bottom][left-1] if left-1 >= 0 else 0) \
                    + (areaSums[top-1][left-1] if top -
                       1 >= 0 and left-1 >= 0 else 0)
        return res


s = Solution()
a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
print(s.matrixBlockSum(a, 1))
