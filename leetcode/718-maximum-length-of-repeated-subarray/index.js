/*
    1st approach: Longest Common Substring

    Time    O(AB)
    Space   O(AB)
    384 ms, faster than 66.34%
*/
var findLength = function (A, B) {
	const dp = [];
	for (let i = 0; i < A.length; i++) {
		const temp = Array(B.length).fill(0);
		dp.push(temp);
	}
	let res = 0;
	for (let i = 0; i < A.length; i++) {
		for (let j = 0; j < B.length; j++) {
			if (A[i] === B[j]) {
				if (i == 0 || j == 0) {
					dp[i][j] = 1;
				} else {
					dp[i][j] = dp[i - 1][j - 1] + 1;
				}
			}
			res = Math.max(res, dp[i][j]);
		}
	}
	return res;
};
