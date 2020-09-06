function minNumberOfCoinsForChange(n, denoms) {
	// Write your code here.
	const dp = Array(n + 1).fill(0);
	for (let i = 1; i <= n; i++) {
		let minCount = Number.MAX_SAFE_INTEGER;
		for (let c of denoms) {
			let target = i - c;
			if (target >= 0) {
				minCount = Math.min(minCount, dp[target] + 1);
			}
		}
		dp[i] = minCount;
	}
	if (dp[n] == Number.MAX_SAFE_INTEGER) {
		return -1;
	}
	return dp[n];
}

// Do not edit the line below.
exports.minNumberOfCoinsForChange = minNumberOfCoinsForChange;
