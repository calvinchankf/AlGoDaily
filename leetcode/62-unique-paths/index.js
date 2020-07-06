/*
    2nd: bottom-up DP

    Time    O(MN)
    Space   O(MN)
    64 ms, faster than 69.51%
*/
var uniquePaths = function (m, n) {
	if (m <= 0 || n <= 0) {
		return 0;
	}
	const dp = [];
	for (let i = 0; i < m; i++) {
		dp.push(Array(n).fill(1));
	}
	for (let i = 1; i < m; i++) {
		for (let j = 1; j < n; j++) {
			dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
		}
	}
	return dp[m - 1][n - 1];
};
