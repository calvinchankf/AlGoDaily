/*
    1st: similar to lc256
    - but this time we can optimize the speed by precompute 2 smallest values from the previous row result

    Time    O(NK)
    Space   O(K)
    92 ms, faster than 56.52%
*/
var minCostII = function (costs) {
	if (costs.length == 0 || costs[0].length == 0) {
		return 0;
	}
	const R = costs.length;
	const C = costs[0].length;
	let dp = [...costs[0]];
	for (let i = 1; i < R; i++) {
		// store 2 minimum valus from the previous results
		// so later, if there is an index collision, pick the 2nd smallest
		let min1 = Number.MAX_SAFE_INTEGER;
		let min2 = Number.MAX_SAFE_INTEGER;
		let min1Idx = -1;
		let min2Idx = -1;
		for (let j = 0; j < C; j++) {
			if (dp[j] < min1) {
				min2 = min1;
				min2Idx = min1Idx;
				min1 = dp[j];
				min1Idx = j;
			} else if (dp[j] < min2) {
				min2 = dp[j];
				min2Idx = j;
			}
		}
		// add the smallest sum from the previous results
		const temp = Array(C).fill(0);
		for (let j = 0; j < C; j++) {
			if (j !== min1Idx) {
				temp[j] = costs[i][j] + min1;
			} else {
				temp[j] = costs[i][j] + min2;
			}
		}
		dp = temp;
	}
	return Math.min(...dp);
};
