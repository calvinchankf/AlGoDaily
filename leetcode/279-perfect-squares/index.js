/*
    2nd approach: bottom up dp

    similar to lc322: coin change
    e.g. coins = [1,2,5], amount = 7
    f(0) = 0  so if f(100-100), it output 0+1=1
    f(1) = min(f0)) + 1
    f(2) = min(f(1)+f(0)) + 1
    f(3) = min(f(2)+f(1)) + 1
    f(4) = min(f(3)+f(2)) + 1
    f(5) = min(f(4)+f(3)+f(0)) + 1
    f(6) = min(f(5)+f(4)+f(1)) + 1
    f(7) = min(f(6)+f(5)+f(2)) + 1

    Time    O(nk) k: square of n
    Space   O(n)
    160 ms, faster than 77.28%
*/
var numSquares = function (n) {
	const root = Math.ceil(Math.sqrt(n));

	const cands = [];
	for (let i = 1; i <= root; i++) {
		cands.push(i * i);
	}

	const dp = Array(root + 1).fill(0);
	for (let i = 1; i <= n; i++) {
		let minCount = Number.MAX_SAFE_INTEGER;
		for (let c of cands) {
			if (i - c >= 0) {
				minCount = Math.min(minCount, dp[i - c] + 1);
			} else {
				break;
			}
		}
		dp[i] = minCount;
	}
	return dp[n];
};
