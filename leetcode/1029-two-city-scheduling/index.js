/*
    2nd: dynamic programming
    - recursion to get all the combinations
    - use a hashtable to avoid redundant calculation to optimize the speed from O(2^N) tp O(N^2)

    Time    O(N^2)
    Space   O(N^2)
    120 ms, faster than 5.22%
*/
var twoCitySchedCost = function (costs) {
	const ht = {};
	const res = dfs(costs, 0, 0, 0, ht);
	return res;
};

var dfs = function (costs, i, a, b, ht) {
	if (a == b && 2 * a === costs.length) {
		return 0;
	}
	if (i === costs.length) {
		return Number.MAX_SAFE_INTEGER;
	}
	const key = `${a},${b}`;
	if (key in ht) {
		return ht[key];
	}
	const c = dfs(costs, i + 1, a + 1, b, ht) + costs[i][0];
	const d = dfs(costs, i + 1, a, b + 1, ht) + costs[i][1];
	ht[key] = Math.min(c, d);
	return ht[key];
};

let a = [
	[10, 20],
	[30, 200],
	[400, 50],
	[30, 20],
];
console.log(twoCitySchedCost(a));
