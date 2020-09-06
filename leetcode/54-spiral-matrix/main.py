"""
    2nd approach: 4 pointers
    - narrow down the range by updating the poiners, top, bottom, left, right

    Time    O(n)
    Space   O(1)
    8 ms, faster than 99.30%
"""


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        top = 0
        right = len(matrix[0])-1
        bottom = len(matrix)-1
        left = 0

        res = []

        while top <= bottom and left <= right:
            # go right
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1
            # go down
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1
            # go left
            # top has been +1 previously, so bottom must be >= new top in order to traverse correctly
            if top <= bottom:
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            # go up
            # left has been +1 previously, so right must be >= new top in order to traverse correctly
            if left <= right:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res


a = [
    [1, 2, 3]
]
print(Solution().spiralOrder(a))

a = [
    [1, 2, 3],
    [4, 5, 6],
]
print(Solution().spiralOrder(a))

a = [
    [1],
    [2],
    [3],
]
print(Solution().spiralOrder(a))

a = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10]
]
print(Solution().spiralOrder(a))

a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(Solution().spiralOrder(a))

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(Solution().spiralOrder(a))

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
print(Solution().spiralOrder(a))

print("-----")

"""
    2nd approach: 4 pointers
    - narrow down the range by updating the poiners, top, bottom, left, right

    Time    O(n)
    Space   O(1)
    8 ms, faster than 99.30%
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        top = 0
        right = len(matrix[0])-1
        bottom = len(matrix)-1
        left = 0

        res = []

        while top <= bottom and left <= right:
            # go right
            j = left
            while j <= right:
                res.append(matrix[top][j])
                j += 1
            top += 1
            # go down
            i = top
            while i <= bottom:
                res.append(matrix[i][right])
                i += 1
            right -= 1
            # go left
            if top <= bottom:
                j = right
                while j >= left:
                    res.append(matrix[bottom][j])
                    j -= 1
                bottom -= 1
            # go up
            if left <= right:
                i = bottom
                while i >= top:
                    res.append(matrix[i][left])
                    i -= 1
                left += 1
        return res


a = [
    [1, 2, 3]
]
print(Solution().spiralOrder(a))

a = [
    [1, 2, 3],
    [4, 5, 6],
]
print(Solution().spiralOrder(a))

a = [
    [1],
    [2],
    [3],
]
print(Solution().spiralOrder(a))

a = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10]
]
print(Solution().spiralOrder(a))

a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(Solution().spiralOrder(a))

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(Solution().spiralOrder(a))

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
print(Solution().spiralOrder(a))
