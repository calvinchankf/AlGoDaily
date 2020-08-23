/*
    1st approach: recursion + hashtable
    - similar to classic coin change/knapsack problem
    - when we calculate recursively, there must be some redundant 'subtrees'. we can use a hashtable to avoid redundant calculation

    Time    O(DFT)
    Space   O(DF)
    748 ms, faster than 39.83%
*/

/**
 * @param {number} d
 * @param {number} f
 * @param {number} target
 * @return {number}
 */
const numRollsToTarget = (d, f, target) => {
	const ht = {};
	const res = dfs(d, f, target, ht);
	return res;
};

const dfs = (d, f, remain, ht) => {
	if (d == 0) {
		if (remain == 0) {
			return 1;
		}
		return 0;
	}
	const key = `${d},${remain}`;
	if (key in ht) {
		return ht[key];
	}
	let total = 0;
	for (let num = 1; num < f + 1; num++) {
		total += dfs(d - 1, f, remain - num, ht);
	}
	ht[key] = total % (Math.pow(10, 9) + 7);
	return ht[key];
};
