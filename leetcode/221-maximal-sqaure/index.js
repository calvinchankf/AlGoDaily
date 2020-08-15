/*
    1st approach: classic dynamic programming approach
    - similar to lc1277

    ref:
    - https://www.youtube.com/watch?v=NYeVhmWsWec

    Time  O(r*c)
    Space O(r*c)
    100 ms, faster than 43.14% 
*/
var maximalSquare = function (matrix) {
	if (matrix.length === 0 || matrix[0].length === 0) {
		return 0;
	}
	const dp = [];
	const r = matrix.length;
	const c = matrix[0].length;
	for (let i = 0; i < r; i++) {
		dp.push(Array(c).fill(0));
	}
	let res = 0;
	for (let i = 0; i < r; i++) {
		for (let j = 0; j < c; j++) {
			if (i === 0 || j === 0) {
				dp[i][j] = parseInt(matrix[i][j]);
			} else if (matrix[i][j] === "1") {
				dp[i][j] =
					1 + Math.min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]);
			}
			res = Math.max(res, dp[i][j] ** 2);
		}
	}
	return res;
};
