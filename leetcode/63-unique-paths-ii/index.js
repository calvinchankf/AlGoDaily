/*
    2nd approach: dynamic programming, iterative top down
    - the basic idea is to sum up the count from left and top
        i.e. dp[i][j] = dp[i-1][j] + dp[i][j-1] 
    - https://leetcode.com/articles/unique-paths-ii/


    Time    O(m*n) iterate the 2d array
    Space   O(m*n) the dp array
    80 ms, faster than 65.82%
*/
var uniquePathsWithObstacles = function(obstacleGrid) {
    if (obstacleGrid[0][0] === 1) {
        return 0
    } 
    const R = obstacleGrid.length
    const C = obstacleGrid[0].length
    const dp = []
    for (let i = 0; i < R; i++) {
        dp.push(Array(C).fill(0))
    }
    for (let i = 0; i < R; i++) {
        for (let j = 0; j < C; j++) {
            if (obstacleGrid[i][j] == 1) {
                continue
            }
            if (i == 0 && j == 0) {
                dp[i][j] = 1
            } else if (i == 0) {
                dp[i][j] = dp[i][j-1]
            } else if (j == 0) {
                dp[i][j] = dp[i-1][j]
            } else {
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            }
            
        }
    }
    return dp[R-1][C-1]
};