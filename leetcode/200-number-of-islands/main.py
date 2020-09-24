"""
    1st approach: dfs, hashtable for visited island territories
    268ms beats 10.53%
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        seen = []
        for i in range(len(grid)):
            seen.append(len(grid[0])*[False])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if seen[i][j] == False and grid[i][j] == '1':
                    self.dfs(grid, i, j, seen)
                    res += 1
        return res

    def dfs(self, grid, i, j, seen):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or seen[i][j] == True:
            return
        seen[i][j] = True
        if grid[i][j] == '1':
            self.dfs(grid, i-1, j, seen)
            self.dfs(grid, i+1, j, seen)
            self.dfs(grid, i, j-1, seen)
            self.dfs(grid, i, j+1, seen)


"""
    follow-up: no recursion

    2nd approach: bfs

    Time    O(n)
    Space   O(n)
    264 ms, faster than 11.41%
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in seen and grid[i][j] == '1':
                    self.bfs(grid, i, j, seen)
                    res += 1
        return res

    def bfs(self, grid, x, y, seen):
        q = []
        q.append((x, y))
        while len(q) > 0:
            i, j = q.pop(0)
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
                continue
            if grid[i][j] == '0':
                continue
            if (i, j) in seen:
                continue
            seen.add((i, j))
            q.append((i-1, j))
            q.append((i+1, j))
            q.append((i, j-1))
            q.append((i, j+1))


"""
    follow-up: diagonal nodes
"""


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        seen = []
        for i in range(len(grid)):
            seen.append(len(grid[0])*[False])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if seen[i][j] == False and grid[i][j] == '1':
                    self.dfs(grid, i, j, seen)
                    res += 1
        return res

    def dfs(self, grid, i, j, seen):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or seen[i][j] == True:
            return
        seen[i][j] = True
        if grid[i][j] == '1':
            self.dfs(grid, i-1, j, seen)
            self.dfs(grid, i+1, j, seen)
            self.dfs(grid, i, j-1, seen)
            self.dfs(grid, i, j+1, seen)
            # diagonal direction
            self.dfs(grid, i-1, j-1, seen)
            self.dfs(grid, i+1, j+1, seen)
            self.dfs(grid, i+1, j-1, seen)
            self.dfs(grid, i-1, j+1, seen)
