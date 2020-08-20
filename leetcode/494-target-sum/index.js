/*
    recursive dfs + memorization
    - dfs to traverse the path from bottom
    - if we see a (idx, total) that we previously visited, we can just use the previous result because the way come up with the remain would be the same

    Time    O(n^2)
    Space   O(n)
    440 ms, faster than 23.93%
*/
var findTargetSumWays = function (nums, S) {
	const ht = {};
	const dfs = (idx, total) => {
		if (idx == nums.length) {
			if (total == S) {
				return 1;
			}
			return 0;
		}
		const key = `${idx},${total}`;
		if (key in ht) {
			return ht[key];
		}
		const left = dfs(idx + 1, total - nums[idx]);
		const right = dfs(idx + 1, total + nums[idx]);
		const nextTotal = left + right;
		ht[key] = nextTotal;
		return nextTotal;
	};
	return dfs(0, 0);
};
