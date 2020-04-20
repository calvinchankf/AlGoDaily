/*
    2nd approach: dynamic programming
    - dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    - https://leetcode.com/articles/minimum-path-sum/

    Time    O(m*n)
    Space   O(m*n)
    64 ms, faster than 41.74%
*/

/**
 * @param {number[][]} grid
 * @return {number}
 */
const minPathSum = (grid) => {
	if (grid.length == 0 || grid[0].length == 0) {
		return 0;
	}
	const dp = [];
	for (let i = 0; i < grid.length; i++) {
		const cols = Array(grid[0].length).fill(0);
		dp.push(cols);
	}
	for (let i = 0; i < grid.length; i++) {
		for (let j = 0; j < grid[0].length; j++) {
			if (i == 0 && j == 0) {
				dp[0][0] = grid[0][0];
			} else if (i == 0) {
				dp[0][j] = dp[0][j - 1] + grid[0][j];
			} else if (j == 0) {
				dp[i][0] = dp[i - 1][0] + grid[i][0];
			} else {
				dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j];
			}
		}
	}
	return dp[dp.length - 1][dp[0].length - 1];
};
