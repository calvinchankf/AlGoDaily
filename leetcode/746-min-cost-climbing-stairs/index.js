/*
    2nd approach: bottom-up DP, learned from others https://zhuanlan.zhihu.com/p/32980698
    - similar to lc983

	e.g. [10,15,20,30,4]
	dp[0] = 10
	dp[1] = 15 to get here, we must step on this stair, therefore it is not min(10, 15) = 10
	dp[2] = 20 + min(dp[0], dp[1]) = 20 + 10 = 30
	dp[3] = 30 + min(dp[1], dp[2]) = 20 + 15 = 35
	dp[4] = 4  + min(dp[2], dp[3]) = 4  + 30 = 34
    dp[5] = 0  + min(dp[3], dp[4]) = 34

	Time 	O(n)
	Space	O(n) the dp array
	88 ms, faster than 52.38%
*/
var minCostClimbingStairs = function (cost) {
	const n = cost.length;
	const dp = Array(n + 1).fill(0);
	dp[0] = cost[0];
	dp[1] = cost[1];
	for (let i = 2; i < n + 1; i++) {
		let curCost = 0;
		if (i < n) {
			curCost = cost[i];
		}
		dp[i] = Math.min(dp[i - 1], dp[i - 2]) + curCost;
	}
	return Math.min(dp[n - 2], dp[n - 1]);
};
