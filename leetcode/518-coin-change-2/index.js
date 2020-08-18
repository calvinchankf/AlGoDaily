/*
    3rd: 2d array DP

    ref: 
    - https://www.youtube.com/watch?v=DJ4a7cmjZY0
    - https://leetcode.com/problems/coin-change-2/discuss/674977/100-Faster-or-Recursive-1-d-2-d-DP-or-Matrix-With-Example-or-Commented
*/
var change = function (amount, coins) {
	if (amount == 0) {
		return 1;
	}
	if (coins.length == 0) {
		return 0;
	}
	const dp = [];
	for (let i = 0; i < coins.length; i++) {
		dp.push(Array(amount + 1).fill(0));
	}
	for (let i = 0; i < coins.length; i++) {
		dp[i][0] = 1;
	}
	for (let i = 0; i < coins.length; i++) {
		const coin = coins[i];
		for (let j = 1; j < amount + 1; j++) {
			const remain = j - coin;
			if (remain >= 0) {
				dp[i][j] = dp[i][remain] + (i - 1 >= 0 ? dp[i - 1][j] : 0);
			} else {
				dp[i][j] = i - 1 >= 0 ? dp[i - 1][j] : 0;
			}
		}
	}
	return dp[coins.length - 1][amount];
};
