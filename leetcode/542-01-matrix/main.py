import sys

"""
    1st: BFS from 0

    Time    O(N^2)
    Space   O(N)
    TLE 35 / 48 test cases passed.
"""


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        R = len(matrix)
        C = len(matrix[0])

        dists = []
        for i in range(R):
            dists.append(C * [sys.maxsize])

        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    self.bfs(matrix, i, j, dists)

        return dists

    def bfs(self, matrix, x, y, dists):
        R = len(matrix)
        C = len(matrix[0])

        q = [(x, y, 0)]
        while len(q) > 0:
            i, j, steps = q.pop(0)
            if i < 0 or i == len(matrix) or j < 0 or j == len(matrix[0]):
                continue
            if steps >= dists[i][j]:
                continue
            dists[i][j] = steps

            if matrix[i][j] == 0 and i != x and j != y:
                continue

            q.append((i-1, j, steps + 1))
            q.append((i+1, j, steps + 1))
            q.append((i, j-1, steps + 1))
            q.append((i, j+1, steps + 1))


"""
    2nd: BFS from 1
"""


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return matrix

        R = len(matrix)
        C = len(matrix[0])

        mask = []
        for i in range(R):
            arr = []
            for j in range(C):
                if matrix[i][j] == 0:
                    arr.append(0)
                else:
                    arr.append(sys.maxsize)
            mask.append(arr)

        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 1:
                    mask[i][j] = self.bfs(matrix, i, j)
        return mask

    def bfs(self, matrix, i, j):

        R = len(matrix)
        C = len(matrix[0])

        q = [(i, j, 0)]
        while len(q) > 0:
            i, j, steps = q.pop(0)
            if matrix[i][j] == 0:
                return steps
            for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                if 0 <= i + di < R and 0 <= j + dj < C:
                    q.append((i + di, j + dj, steps + 1))
