class Solution(object):
    def maximalRectangle(self, matrix):
        """
        classic approach: dynamic programming + max area within a histogram(leetcode 84)
        - similar to lc1504

        e.g.
        [
          [1,0,1,0,0],
          [1,0,1,1,1],
          [1,1,1,1,1],
          [1,0,0,1,0],
        ]

        for each row, we accumulate the ones on the grids on position in previous row and find the area of the current histogram
        [1,0,1,0,0] <- maxarea 1
        [2,0,2,1,1] <- maxarea 3
        [3,1,3,2,2] <- maxarea 6
        [4,0,0,3,0] <- maxarea 4

        therefore the answer is 6

        Time  O(n^2)
        Space O(n)
        380 ms, faster than 11.81%
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        retangle = []
        res = 0
        for arr in matrix:
            if len(retangle) == 0:
                # leetcode is bad at presenting the question, ["1","0","1","0","0"] <- WTF
                retangle = [int(x) for x in arr]
            else:
                for j in range(len(arr)):
                    if arr[j] == '0':
                        retangle[j] = 0
                    else:
                        retangle[j] += 1
            area = self.largestRectangleArea(retangle)
            if area > res:
                res = area
        return res

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int

        2nd approach: stack <= learned from others 
        - use a stack to store the indeces where the corresponding height can create a potential largest retangle

        ref:
        - https://www.youtube.com/watch?v=ZmnqCZp9bBs

        Time	O(n)
        Space	O(n)
        100 ms, faster than 31.99% 
        """
        res = 0
        # begining with -1, such that we can calculate the range, i - stack[-1][0] - 1, easier
        # (index, height)
        stack = [(-1, 0)]
        for i in range(len(heights)):
            cur = heights[i]
            if cur > stack[-1][1]:
                # if current height is taller, append to the stack
                stack.append((i, cur))
            else:
                # pop the stack if the items which is > cur height
                while stack[-1][1] > cur:
                    popIdx, popH = stack.pop()
                    width = i - stack[-1][0] - 1
                    area = popH * width
                    res = max(res, area)
                # put the current item to the array
                stack.append((i, cur))
        # if the stack is not empty, pop the items
        while len(stack) > 1:
            popIdx, popH = stack.pop()
            width = len(heights) - stack[-1][0] - 1
            area = popH * width
            res = max(res, area)
        return res


a = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
print(Solution().maximalRectangle(a))
