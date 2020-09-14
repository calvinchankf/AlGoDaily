function levenshteinDistance(str1, str2) {
	// Write your code here.
	const dp = [];
	const l1 = str1.length;
	const l2 = str2.length;
	for (let i = 0; i < l1 + 1; i++) {
		const temp = [];
		for (let j = 0; j < l2 + 1; j++) {
			if (i == 0) {
				temp.push(j);
			} else if (j == 0) {
				temp.push(i);
			} else {
				temp.push(0);
			}
		}
		dp.push(temp);
	}
	for (let i = 0; i < l1; i++) {
		for (let j = 0; j < l2; j++) {
			if (str1[i] == str2[j]) {
				dp[i + 1][j + 1] = dp[i][j];
			} else {
				dp[i + 1][j + 1] =
					Math.min(dp[i][j], dp[i][j + 1], dp[i + 1][j]) + 1;
			}
		}
	}
	console.log(dp);
	return dp[l1][l2];
}

// Do not edit the line below.
exports.levenshteinDistance = levenshteinDistance;
