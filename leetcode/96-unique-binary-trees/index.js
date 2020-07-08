/*
    Classic DP: Catalan Number
    - https://www.youtube.com/watch?v=YDf982Lb84o
    - https://www.youtube.com/watch?v=GgP75HAvrlY

    f(0) = 1
	f(1) = 1
	f(2) = f(1) + f(1)
	f(3) = f(2) + f(1)f(1) + f(2)
	f(4) = f(3) + f(1)f(2) + f(2)f(1) + f(3)
	f(5) = f(4) + f(1)f(3) + f(2)f(2) + f(3)f(1) + f(4)
	f(6) = f(5) + f(1)f(4) + f(2)f(3) + f(3)f(2) + f(4)f(1) + f(5)

	Time 	O(n^2) for each number, we need to iterate through the previous items and sum up the results
	Space	O(n)
	64 ms, faster than 59.42%
*/
var numTrees = function (n) {
	if (n < 2) {
		return 1;
	}
	dp = {};
	dp[0] = 1;
	dp[1] = 1;

	var f = function (k) {
		if (k in dp) {
			return dp[k];
		}
		sum = 0;
		for (let i = 0; i < k; i++) {
			sum += f(i) * f(k - i - 1);
		}
		dp[k] = sum;
		return sum;
	};
	f(n);

	return dp[n];
};
