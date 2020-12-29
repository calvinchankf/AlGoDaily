function getNthFib(n) {
	// Write your code here.
	const dp = [0, 1];
	for (let i = 2; i < n; i++) {
		dp.push(dp[i - 2] + dp[i - 1]);
	}
	return dp[n - 1];
}

// Do not edit the line below.
exports.getNthFib = getNthFib;
