function longestIncreasingSubsequence(nums) {
	// Write your code here.
	const n = nums.length;
	const dp = [];
	for (let i = 0; i < n; i++) {
		dp.push([nums[i]]);
	}
	for (let i = 0; i < n; i++) {
		for (let j = 0; j < i; j++) {
			if (nums[j] < nums[i]) {
				// dp[i] = Math.max(dp[j] + 1, dp[i]);
				if (dp[j].length + 1 > dp[i].length) {
					dp[i] = [...dp[j], nums[i]];
				}
			}
		}
	}
	// console.log(dp);
	let res = [];
	for (let i = 0; i < n; i++) {
		// res = Math.max(res, x);
		if (dp[i].length > res.length) {
			res = dp[i];
		}
	}
	return res;
}

// Do not edit the line below.
exports.longestIncreasingSubsequence = longestIncreasingSubsequence;
