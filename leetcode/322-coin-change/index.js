/*
    3rd: dp
    learned from others: bottom-up
    e.g. coins = [1,2,5], amount = 7
    f(0) = 0  so if f(100-100), it output 0+1=1
    f(1) = min(f(0)) + 1
    f(2) = min(f(1)+f(0)) + 1
    f(3) = min(f(2)+f(1)) + 1
    f(4) = min(f(3)+f(2)) + 1
    f(5) = min(f(4)+f(3)+f(0)) + 1
    f(6) = min(f(5)+f(4)+f(1)) + 1
    f(7) = min(f(6)+f(5)+f(2)) + 1
    ...

    Time    O(CA) C: number of coins, A: amount
    Space   O(A)
    152 ms, faster than 42.49%
*/
var coinChange = function (coins, amount) {
	const n = amount;
	const dp = Array(n + 1).fill(0);
	for (let i = 1; i < n + 1; i++) {
		let minStepsFromRemain = Number.MAX_SAFE_INTEGER;
		for (let c of coins) {
			const remain = i - c;
			if (remain >= 0) {
				minStepsFromRemain = Math.min(dp[remain], minStepsFromRemain);
			}
		}
		dp[i] = minStepsFromRemain + 1;
	}
	if (dp[amount] >= Number.MAX_SAFE_INTEGER) {
		return -1;
	}
	return dp[amount];
};
