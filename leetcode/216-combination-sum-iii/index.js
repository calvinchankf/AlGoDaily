/*
    1st: recursion
    - similar to lc77(combinations)

    Time    O(nCk)
    Space   O(nCk)
    80 ms, faster than 32.73% 
*/
var combinationSum3 = function (k, n) {
	const res = [];
	const candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9];
	const dfs = (cands, chosen, total) => {
		if (chosen.length === k) {
			if (total === n) {
				res.push(chosen);
			}
		} else if (total < n) {
			for (let i = 0; i < cands.length; i++) {
				dfs(
					cands.slice(i + 1),
					[...chosen, cands[i]],
					total + cands[i]
				);
			}
		}
	};
	dfs(candidates, [], 0);
	return res;
};
