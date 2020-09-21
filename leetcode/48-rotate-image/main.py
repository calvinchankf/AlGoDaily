"""
    1st attempt:
	1. transpose
	2. swap columns

	if anit-clockwise:
	1. swap columns
	2. transpose

	Time		O(2n)
	Space		O(1)
	36 ms, faster than 14.18%
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.swapCols(matrix)

    def transpose(self, matrix):
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def swapCols(self, matrix):
        for i in range(len(matrix)):
            n = len(matrix[0])
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]


"""
    2nd attempt:
	1. transpose
	2. swap columns, optimzation is to reverse the each row

	if anit-clockwise:
	1. swap columns
	2. transpose

	Time		O(2n)
	Space		O(1)
	36 ms, faster than 14.18%
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.swapCols(matrix)

    def transpose(self, matrix):
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def swapCols(self, matrix):
        for i in range(len(matrix)):
            matrix[i].reverse()


"""
    variation: anti transpose
    123     963
    456 ->  852
    789     741
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)  # <- N = R = C
        for i in range(N):
            for j in range(N-i):
                matrix[i][j], matrix[N-j-1][N-i-1] \
                    = matrix[N-j-1][N-i-1], matrix[i][j]


s = Solution()
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s.rotate(a)
print(a)
