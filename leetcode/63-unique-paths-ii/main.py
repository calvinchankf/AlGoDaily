"""
    1st approach: brute force, bottom up recursively with memorization
    - intuitively go through all the path with i+1 OR j+1
    - count the path which reaches to the destination coordinate (m, n)
    - cache the count of the coordinates which we have calculated before
    - if the current grid, grid[i][j], is blocked, tell its parent that this way is blocked by return 0
    - sum up all the coordinates' count

    Time    O(m*n) 0->m, 0->n. since we cache the intermediate coordinates, we dont have duplicate sets of i, j
    Space   O(m*n) depth of recursion calls
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0
        seen = {}
        return self.dfs(obstacleGrid, 0, 0, len(obstacleGrid)-1, len(obstacleGrid[0])-1, seen)

    def dfs(self, grid, i, j, m, n, seen):
        key = str(i)+","+str(j)
        if key in seen:
            return seen[key]
        if i == m and j == n:
            if grid[i][j] == 1:
                return 0
            return 1
        elif i > m or j > n:
            return 0
        if grid[i][j] == 1:
            seen[key] = 0
            return 0
        left = self.dfs(grid, i+1, j, m, n, seen)
        right = self.dfs(grid, i, j+1, m, n, seen)
        seen[key] = left + right
        return left + right


a = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print(Solution().uniquePathsWithObstacles(a))

a = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print(Solution().uniquePathsWithObstacles(a))

a = [
    [0, 0, 1],
    [0, 1, 0],
    [0, 0, 0]
]
print(Solution().uniquePathsWithObstacles(a))

a = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 0, 0]
]
print(Solution().uniquePathsWithObstacles(a))

a = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0]
]
print(Solution().uniquePathsWithObstacles(a))

a = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
print(Solution().uniquePathsWithObstacles(a))


"""
    2nd approach: dynamic programming, iterative top down
    - the basic idea is to sum up the count from left and top
        i.e. dp[i][j] = dp[i-1][j] + dp[i][j-1] 
    - https://leetcode.com/articles/unique-paths-ii/


    Time    O(m*n) iterate the 2d array
    Space   O(m*n) the dp array
    36 ms, faster than 94.84% 
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:
            return 0
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * C for i in range(R)]
        for i in range(R):
            for j in range(C):
                if i == 0 and j == 0:
                    dp[0][0] = 1
                elif i == 0:
                    dp[0][j] = dp[0][j-1]
                elif j == 0:
                    dp[i][0] = dp[i-1][0]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
        return dp[-1][-1]


print('2nd approach')

a = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print(Solution().uniquePathsWithObstacles(a))

a = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print(Solution().uniquePathsWithObstacles(a))

a = [
    [0, 0, 1],
    [0, 1, 0],
    [0, 0, 0]
]
print(Solution().uniquePathsWithObstacles(a))

a = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 0, 0]
]
print(Solution().uniquePathsWithObstacles(a))

a = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0]
]
print(Solution().uniquePathsWithObstacles(a))

a = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
print(Solution().uniquePathsWithObstacles(a))
