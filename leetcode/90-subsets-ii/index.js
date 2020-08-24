/*
    2nd approach: recursion
    - similar to 1st dont need to use a hashtable(since the array is sorted)
    
    Time    O(2^n) worst
    Space   O(2^n) recursion
    108 ms, faster than 22.25%
*/
var subsetsWithDup = function (nums) {
	nums.sort((a, b) => a - b);
	const res = [];
	const dfs = (cands, chosen) => {
		res.push(chosen);
		for (let i = 0; i < cands.length; i++) {
			if (i == 0 || cands[i] != cands[i - 1]) {
				dfs(cands.slice(i + 1), [...chosen, cands[i]]);
			}
		}
	};
	dfs(nums, []);
	return res;
};
