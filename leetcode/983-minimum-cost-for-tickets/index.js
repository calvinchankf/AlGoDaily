/*
    dp, learned from others, more concise
    - actually it is similar to coin change, we can do it with a bottom up approach
    - be careful that:
        1. for non-present days, extand the previous day cost
        2. since 7days, 30 days passes might cheaper than the 1day and 7days, we need to consider the cost if i-1/7/30 < 0

    e.g. days = [1, 4, 6, 7, 8, 20], costs = [2, 7, 15]
    cost
    dp[0]                           = 0
    dp[1] = dp[1]+2                 = 2
    dp[2] = dp[1]                   = 2 <= no such date extand from previous
    dp[3] = dp[2]                   = 2 <= no such date extand from previous
    dp[4] = dp[3]+2                 = 4
    dp[5] = dp[4]                   = 4 <= no such date extand from previous
    dp[6] = dp[5]+2                 = 6
    dp[7] = min(dp[6]+2, dp[0]+7)   = 7
    dp[8] = min(dp[7]+2, dp[1]+7)   = 9
    dp[9] = dp[8]                   = 9 <= no such date extand from previous
    ...

    Time    O(n)
    Space   O(n)
    132 ms, faster than 9.96%
*/
var mincostTickets = function (days, costs) {
	const daySet = new Set(days);
	const n = days[days.length - 1];
	const dp = Array(n + 1).fill(0);
	for (let i = 1; i < n + 1; i++) {
		if (!daySet.has(i)) {
			dp[i] = dp[i - 1];
		} else {
			dp[i] = Math.min(
				dp[Math.max(0, i - 1)] + costs[0],
				dp[Math.max(0, i - 7)] + costs[1],
				dp[Math.max(0, i - 30)] + costs[2]
			);
		}
	}
	return dp[n];
};

/*
    Or this
*/
var mincostTickets = function (days, costs) {
	const n = days[days.length - 1];
	const dp = Array(n + 1).fill(0);
	const hs = new Set(days);
	for (let i = 1; i < n + 1; i++) {
		if (!hs.has(i)) {
			dp[i] = dp[i - 1];
			continue;
		}
		let minCost = Number.MAX_SAFE_INTEGER;
		minCost = Math.min(
			minCost,
			i - 1 >= 0 ? dp[i - 1] + costs[0] : costs[0]
		);
		minCost = Math.min(
			minCost,
			i - 7 >= 0 ? dp[i - 7] + costs[1] : costs[1]
		);
		minCost = Math.min(
			minCost,
			i - 30 >= 0 ? dp[i - 30] + costs[2] : costs[2]
		);
		dp[i] = minCost;
	}
	return dp[n];
};
