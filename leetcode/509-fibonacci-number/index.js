/*
    1st: top-down recursive
	- use a hashtable to avoid redundant calculation
	
    Time O(n)		duplicates are avoided so only the unseen numbers go through the calculations
	Space O(2n)	    n for hashtable, n for recursive callstack
	68 ms, faster than 79.80% 
*/
var fib = function (N) {
	const ht = {};
	const f = (n) => {
		if (n == 0) {
			return 0;
		} else if (n == 1) {
			return 1;
		}
		if (n in ht) {
			return ht[n];
		}
		const temp = f(n - 1) + f(n - 2);
		ht[n] = temp;
		return temp;
	};
	return f(N);
};

/*
    2nd: bottom-up iterative

	Time 	O(n) iterate from 1 to N
	Space	O(n) for the array
	76 ms, faster than 70.93%
*/
var fib = function (N) {
	const dp = [0, 1];
	for (let i = 2; i <= N; i++) {
		dp.push(dp[i - 2] + dp[i - 1]);
	}
	return dp[N];
};
