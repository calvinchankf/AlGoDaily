/*
    Classic DP: Catalan Number
    - https://www.youtube.com/watch?v=YDf982Lb84o
    - https://www.youtube.com/watch?v=GgP75HAvrlY

    f(0) = 1
	f(1) = 1
	f(2) = f(1)f(0) + f(1)f(0)
	f(3) = f(2)f(0) + f(1)f(1) + f(2)f(0)
	f(4) = f(3)f(0) + f(1)f(2) + f(2)f(1) + f(3)f(0)
	f(5) = f(4)f(0) + f(1)f(3) + f(2)f(2) + f(3)f(1) + f(4)f(0)
	f(6) = f(5)f(0) + f(1)f(4) + f(2)f(3) + f(3)f(2) + f(4)f(1) + f(5)f(0)

	Time 	O(n^2) for each number, we need to iterate through the previous items and sum up the results
	Space	O(n)
	64 ms, faster than 59.42%
*/
var numTrees = function (n) {
	return dfs(n, {});
};

const dfs = (n, ht) => {
	// there is no n = 0 from input but
	if (n == 0 || n == 1) {
		return 1;
	}
	if (n in ht) {
		return ht[n];
	}
	let res = 0;
	for (let i = 0; i < n; i++) {
		res += dfs(i, ht) * dfs(n - i - 1, ht);
	}
	ht[n] = res;
	return res;
};
