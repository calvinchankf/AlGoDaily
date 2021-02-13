"""
    1st: brute force dynamic programming
    - similar to lc1504

    e.g.
    [
        [1,0,1,0,0],
        [1,0,1,1,1],
        [1,1,1,1,1],
        [1,0,0,1,0],
    ]

    for each row, we accumulate the ones on the grids on position in previous row and find the area of the current histogram
    [1,0,1,0,0]
    [1,0,1,2,3]
    [1,2,3,4,5]
                ^ at this point the width = min(5, 3) = 3, height = 2 - 1 + 1 = 2, so the area = 6
    [1,0,0,1,0]

    therefore the answer is 6

    Time  O(RCR)
    Space O(RC)
    2452 ms, faster than 5.21%
"""


class Solution(object):
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        R, C = len(matrix), len(matrix[0])
        res = 0
        dp = [C * [0] for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == '0':
                    continue

                # go right to accumulate the ones
                if j > 0:
                    dp[i][j] = dp[i][j-1] + 1
                else:
                    dp[i][j] = 1
                w = dp[i][j]

                # go up to see if we can form a larger rectangle
                for k in range(i, -1, -1):
                    w = min(w, dp[k][j])
                    h = i - k + 1
                    res = max(res, w*h)
        return res


"""
    2nd: histogram
    - reuse lc84

    e.g.
    [
        [1,0,1,0,0],
        [1,0,1,1,1],
        [1,1,1,1,1],
        [1,0,0,1,0],
    ]
    for row=0, find the largest histogram area of [1,0,1,0,0]
    for row=1, find the largest histogram area of [2,0,2,1,1]
    for row=2, find the largest histogram area of [3,0,3,2,2]
    for row=3, find the largest histogram area of [4,0,0,1,0]

    Time    O(RC)
    Space   O(C)
    200 ms, faster than 77.39%
"""


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        R, C = len(matrix), len(matrix[0])
        res = 0
        histogram = C * [0]
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == '1':
                    histogram[j] += 1
                else:
                    histogram[j] = 0
            rowMaxArea = self.largestRectangleArea(histogram)
            res = max(res, rowMaxArea)
        return res

    def largestRectangleArea(self, heights):
        res = 0
        stack = [(-1, 0)]
        for i in range(len(heights)):
            cur = heights[i]
            if cur > stack[-1][1]:
                stack.append((i, cur))
            else:
                while stack[-1][1] > cur:
                    popIdx, popH = stack.pop()
                    width = i - stack[-1][0] - 1
                    area = popH * width
                    res = max(res, area)
                stack.append((i, cur))
        while len(stack) > 1:
            popIdx, popH = stack.pop()
            width = len(heights) - stack[-1][0] - 1
            area = popH * width
            res = max(res, area)
        return res
