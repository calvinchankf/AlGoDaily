"""
    1st approach: recursive dfs, combine the perimeter of each grid
    - simiar to lc1020, lc1254
    Time    O(n)
    Space   O(n, d)
    1372 ms, faster than 5.04%
"""


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        # visited
        seen = set()
        # iteration
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in seen:
                    res = self.dfs(grid, i, j, seen)
        return res

    def dfs(self, grid, i, j, seen):
        # if boundary, return 1 and stop exploring
        if i < 0 or i+1 > len(grid) or j < 0 or j+1 > len(grid[0]):
            return 1
        # if 0, return 1 and stop exploring
        if grid[i][j] == 0:
            return 1
        # if visited, stop exploring
        if (i, j) in seen:
            return 0
        seen.add((i, j))
        up = self.dfs(grid, i-1, j, seen)
        down = self.dfs(grid, i+1, j, seen)
        left = self.dfs(grid, i, j-1, seen)
        right = self.dfs(grid, i, j+1, seen)
        return up + down + left + right


a = []
print(Solution().islandPerimeter(a))

a = [[]]
print(Solution().islandPerimeter(a))

a = [[1]]
print(Solution().islandPerimeter(a))

a = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0],
]
print(Solution().islandPerimeter(a))

a = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 1, 0],
    [1, 1, 0, 0],
]
print(Solution().islandPerimeter(a))

a = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
]
print(Solution().islandPerimeter(a))

print("--------------------")


"""
    2nd approach: iterative bfs
    - we increment the area in 2 cases:
        1. the current cell reaches to the boundaries
        2. the current cell reaches to a zero

    Time    O(n)
    Space   O(n)
    696 ms, faster than 17.83%
"""


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        seen = []
        res = 0
        for i in range(len(grid)):
            seen.append(len(grid[0])*[False])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and seen[i][j] == False:
                    res = self.bfs(grid, i, j, seen)
        return res

    def bfs(self, grid, x, y, seen):
        edgesCount = 0
        q = []
        q.append((x, y))
        while len(q) > 0:
            i, j = q.pop(0)

            if grid[i][j] == 0:
                edgesCount += 1
            else:
                # if this cell of 1 is visited, skip
                if seen[i][j] == True:
                    continue
                seen[i][j] = True

                if i - 1 >= 0:
                    q.append((i-1, j))
                else:
                    edgesCount += 1

                if i + 1 < len(grid):
                    q.append((i+1, j))
                else:
                    edgesCount += 1

                if j - 1 >= 0:
                    q.append((i, j-1))
                else:
                    edgesCount += 1

                if j + 1 < len(grid[0]):
                    q.append((i, j+1))
                else:
                    edgesCount += 1
        return edgesCount


a = []
print(Solution().islandPerimeter(a))

a = [[]]
print(Solution().islandPerimeter(a))

a = [[1]]
print(Solution().islandPerimeter(a))

a = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0],
]
print(Solution().islandPerimeter(a))

a = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 1, 0],
    [1, 1, 0, 0],
]
print(Solution().islandPerimeter(a))

a = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
]
print(Solution().islandPerimeter(a))

print("--------------------")

"""
    follow-up 1: no more than 1 island
"""


class Solution(object):

    def __init__(self):
        self.res = 0

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        seen = []
        res = []
        for i in range(len(grid)):
            seen.append(len(grid[0])*[False])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and seen[i][j] == False:
                    temp = self.dfs(grid, i, j, seen)
                    res.append(temp)
        return res

    def dfs(self, grid, i, j, seen):
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1:
            return 1
        if grid[i][j] == 0:
            return 1
        elif grid[i][j] == 1 and seen[i][j] == False:
            seen[i][j] = True
            up = self.dfs(grid, i-1, j, seen)
            down = self.dfs(grid, i+1, j, seen)
            left = self.dfs(grid, i, j-1, seen)
            right = self.dfs(grid, i, j+1, seen)
            return up + down + left + right
        return 0


a = []
print(Solution().islandPerimeter(a))

a = [[]]
print(Solution().islandPerimeter(a))

a = [[1]]
print(Solution().islandPerimeter(a))

a = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0],
]
print(Solution().islandPerimeter(a))

a = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 1],
]
print(Solution().islandPerimeter(a))

print("--------------------")

"""
    follow-up 2: return the max area island
"""


class Solution(object):

    def __init__(self):
        self.res = 0

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        seen = []
        res = 0
        for i in range(len(grid)):
            seen.append(len(grid[0])*[False])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and seen[i][j] == False:
                    temp = self.dfs(grid, i, j, seen)
                    if temp > res:
                        res = temp
        return res

    def dfs(self, grid, i, j, seen):
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1:
            return 1
        if grid[i][j] == 0:
            return 1
        elif grid[i][j] == 1 and seen[i][j] == False:
            seen[i][j] = True
            up = self.dfs(grid, i-1, j, seen)
            down = self.dfs(grid, i+1, j, seen)
            left = self.dfs(grid, i, j-1, seen)
            right = self.dfs(grid, i, j+1, seen)
            return up + down + left + right
        return 0


a = []
print(Solution().islandPerimeter(a))

a = [[]]
print(Solution().islandPerimeter(a))

a = [[1]]
print(Solution().islandPerimeter(a))

a = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0],
]
print(Solution().islandPerimeter(a))

a = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 1],
]
print(Solution().islandPerimeter(a))
