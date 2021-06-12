"""
    1st: array
    - reuse leetcode 48
    - hash every rotation

    Time    O(9RC)
    Space   O(4RC)
    48 ms, faster than 66.67%
"""


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        hashTarget = self.hashMatrix(target)
        hash0 = self.hashMatrix(mat)
        hash90 = self.hashMatrix(self.rotate(mat))
        hash180 = self.hashMatrix(self.rotate(mat))
        hash270 = self.hashMatrix(self.rotate(mat))
        return hashTarget == hash0 or hashTarget == hash90 or hashTarget == hash180 or hashTarget == hash270

    def rotate(self, matrix):
        self.transpose(matrix)
        self.swapCols(matrix)
        return matrix

    def transpose(self, matrix):
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def swapCols(self, matrix):
        for i in range(len(matrix)):
            matrix[i].reverse()

    def hashMatrix(self, mat):
        N = len(mat)
        s = ''
        for i in range(N):
            s += ','.join([str(d) for d in mat[i]])
            s += '|'
        return s
