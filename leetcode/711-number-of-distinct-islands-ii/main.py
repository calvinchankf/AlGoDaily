import sys

"""
    1st: BFS + hastable
    - basic concept is similar to lc200
    - for see if a shape is distinct, we can save 8 possibilities(rotate 0, 90,180,270, flip, 90, 180, 270) in a hashtbale
    - use strings to speed up the hashtable look up

    Time    O(16 * RC)
    Space   O(RC)
    684 ms, faster than 23.64%
"""


class Solution(object):
    def numDistinctIslands2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        shapes = set()
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in seen and grid[i][j] == 1:
                    cells = self.bfs(grid, i, j, seen)

                    shape = self.buildShape(cells)
                    shapeKey = self.shape2Key(shape)
                    if shapeKey in shapes:
                        continue

                    rotate90 = self.clockewise(shape)
                    rotate180 = self.clockewise(rotate90)
                    rotate270 = self.clockewise(rotate180)

                    rotate90Key = self.shape2Key(rotate90)
                    rotate180Key = self.shape2Key(rotate180)
                    rotate270Key = self.shape2Key(rotate270)

                    flip = self.swapRows(shape)
                    flip90 = self.clockewise(flip)
                    flip180 = self.clockewise(flip90)
                    flip270 = self.clockewise(flip180)

                    flipKey = self.shape2Key(flip)
                    flip90Key = self.shape2Key(flip90)
                    flip180Key = self.shape2Key(flip180)
                    flip270Key = self.shape2Key(flip270)

                    shapes |= set([shapeKey, rotate90Key, rotate180Key,
                                   rotate270Key, flipKey, flip90Key, flip180Key, flip270Key])
                    res += 1
        return res

    def bfs(self, grid, x, y, seen):
        visited = []
        q = []
        q.append((x, y))
        while len(q) > 0:
            i, j = q.pop(0)
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
                continue
            if (i, j) in seen:
                continue
            seen.add((i, j))
            if grid[i][j] == 1:
                visited.append((i, j))
                q.append((i-1, j))
                q.append((i+1, j))
                q.append((i, j-1))
                q.append((i, j+1))
        return visited

    def buildShape(self, cells):
        minI, minJ = sys.maxsize, sys.maxsize
        maxI, maxJ = -sys.maxsize, -sys.maxsize
        for i, j in cells:
            minI, maxI = min(minI, i), max(maxI, i)
            minJ, maxJ = min(minJ, j), max(maxJ, j)
        matrix = []
        for i in range(maxI-minI+1):
            matrix.append((maxJ-minJ+1)*[0])
        for i, j in cells:
            matrix[i-minI][j-minJ] = 1
        return matrix

    def shape2Key(self, grid):
        key = ''
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                key += str(grid[i][j]) + ','
            key += '|'
        return key

    def clockewise(self, matrix):
        result = []
        for i in range(len(matrix[0])):
            temp = []
            for j in reversed(range(len(matrix))):
                temp.append(matrix[j][i])
            result.append(temp)
        return result

    def swapRows(self, grid):
        matrix = []
        for i in range(len(grid)-1, -1, -1):
            matrix.append(grid[i])
        return matrix


s = Solution()

a = [
    [1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 1, 1, 1],
]
print(s.numDistinctIslands2(a))

a = [
    [0, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 1],
]
print(s.numDistinctIslands2(a))

a = [
    [1, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 1],
]
print(s.numDistinctIslands2(a))

a = [
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0],
]
print(s.numDistinctIslands2(a))

print("-----")

"""
    2nd: DFS + hastable
    - basic concept is similar to lc200
    - for see if a shape is distinct, we can save 8 possibilities(rotate 0, 90,180,270, flip, 90, 180, 270) in a hashtbale
    - use strings to speed up the hashtable look up

    Time    O(16 * RC)
    Space   O(RC)
    576 ms, faster than 27.27%
"""


class Solution(object):
    def numDistinctIslands2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        shapes = set()
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in seen and grid[i][j] == 1:
                    cells = self.dfs(grid, i, j, seen)

                    shape = self.buildShape(cells)
                    shapeKey = self.shape2Key(shape)
                    if shapeKey in shapes:
                        continue

                    rotate90 = self.clockewise(shape)
                    rotate180 = self.clockewise(rotate90)
                    rotate270 = self.clockewise(rotate180)

                    rotate90Key = self.shape2Key(rotate90)
                    rotate180Key = self.shape2Key(rotate180)
                    rotate270Key = self.shape2Key(rotate270)

                    flip = self.swapRows(shape)
                    flip90 = self.clockewise(flip)
                    flip180 = self.clockewise(flip90)
                    flip270 = self.clockewise(flip180)

                    flipKey = self.shape2Key(flip)
                    flip90Key = self.shape2Key(flip90)
                    flip180Key = self.shape2Key(flip180)
                    flip270Key = self.shape2Key(flip270)

                    shapes |= set([shapeKey, rotate90Key, rotate180Key,
                                   rotate270Key, flipKey, flip90Key, flip180Key, flip270Key])
                    res += 1
        return res

    def dfs(self, grid, x, y, seen):
        visited = []

        def f(i, j, visited):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if (i, j) in seen:
                return
            seen.add((i, j))
            if grid[i][j] == 1:
                visited.append((i, j))
                f(i-1, j, visited)
                f(i+1, j, visited)
                f(i, j-1, visited)
                f(i, j+1, visited)
        f(x, y, visited)
        return visited

    def buildShape(self, cells):
        minI, minJ = sys.maxsize, sys.maxsize
        maxI, maxJ = -sys.maxsize, -sys.maxsize
        for i, j in cells:
            minI, maxI = min(minI, i), max(maxI, i)
            minJ, maxJ = min(minJ, j), max(maxJ, j)
        matrix = []
        for i in range(maxI-minI+1):
            matrix.append((maxJ-minJ+1)*[0])
        for i, j in cells:
            matrix[i-minI][j-minJ] = 1
        return matrix

    def shape2Key(self, grid):
        key = ''
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                key += str(grid[i][j]) + ','
            key += '|'
        return key

    def clockewise(self, matrix):
        result = []
        for i in range(len(matrix[0])):
            temp = []
            for j in reversed(range(len(matrix))):
                temp.append(matrix[j][i])
            result.append(temp)
        return result

    def swapRows(self, grid):
        matrix = []
        for i in range(len(grid)-1, -1, -1):
            matrix.append(grid[i])
        return matrix


s = Solution()

a = [
    [1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 1, 1, 1],
]
print(s.numDistinctIslands2(a))

a = [
    [0, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 1],
]
print(s.numDistinctIslands2(a))

a = [
    [1, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 1],
]
print(s.numDistinctIslands2(a))

a = [
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0],
]
print(s.numDistinctIslands2(a))
