function maxSumIncreasingSubsequence(array) {
	// Write your code here.
	const n = array.length;
	const dp = [...array];
	let resArrays = [];
	for (let i = 0; i < n; i++) {
		resArrays.push([array[i]]);
	}

	for (let i = 1; i < n; i++) {
		for (let j = 0; j < i; j++) {
			if (array[i] > array[j]) {
				if (array[i] + dp[j] > dp[i]) {
					dp[i] = array[i] + dp[j];
					resArrays[i] = [...resArrays[j], array[i]];
				}
			}
		}
	}

	let idx = 0;
	for (let i = 0; i < n; i++) {
		if (dp[i] > dp[idx]) {
			idx = i;
		}
	}

	return [dp[idx], resArrays[idx]];
}

// Do not edit the line below.
exports.maxSumIncreasingSubsequence = maxSumIncreasingSubsequence;
