/*
    2nd approach: simialar to lc90(subset 2)

    e.g  8

    Time    O(2^N) worset
    Space   O(2^N) the result
    108 ms, faster than 32.29%
    17june2019
*/
var combinationSum2 = function (candidates, target) {
	const res = [];
	candidates.sort((a, b) => a - b);
	const dfs = (cands, chosen, total) => {
		if (total == target) {
			res.push(chosen);
		} else if (total < target) {
			for (let i = 0; i < cands.length; i++) {
				const cand = cands[i];
				// check cands[i - 1] != cands[i] to avoid redundant subset
				// the next selection will be made in the next recursion, dont worry if we can generate [1,1,6] from nums=[10,1,2,7,6,1,5], k=8
				if (i == 0 || cands[i - 1] != cands[i]) {
					dfs(cands.slice(i + 1), [...chosen, cand], total + cand);
				}
			}
		}
	};
	dfs(candidates, [], 0);
	return res;
};
