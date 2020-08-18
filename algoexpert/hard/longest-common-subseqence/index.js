function longestCommonSubsequence(str1, str2) {
	if (str1.length == 0 || str2.length == 0) {
		return [];
	}
	const S1 = str1.length;
	const S2 = str2.length;

	const dp = [];
	for (let i = 0; i < S1 + 1; i++) {
		dp.push(new Array(S2 + 1).fill([]));
	}

	for (let i = 0; i < S1; i++) {
		for (let j = 0; j < S2; j++) {
			if (str1[i] === str2[j]) {
				dp[i + 1][j + 1] = dp[i][j].concat(str1[i]);
			} else {
				if (dp[i + 1][j].length > dp[i][j + 1].length) {
					dp[i + 1][j + 1] = dp[i + 1][j];
				} else {
					dp[i + 1][j + 1] = dp[i][j + 1];
				}
			}
		}
	}

	return dp[S1][S2];
}

// Do not edit the line below.
exports.longestCommonSubsequence = longestCommonSubsequence;
