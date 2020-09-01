/*
    2nd approach: recursive dfs, avoid duplicate by considering the candidates which are >= num


    Time    O(N^k) k depends on target
    Space   O(N^N)
    104 ms, faster than 50.08% 
*/
var combinationSum = function (candidates, target) {
	candidates.sort((a, b) => a - b);

	const res = [];
	const dfs = (chosen, total) => {
		if (total == target) {
			res.push(chosen);
		}
		if (total > target) {
			return;
		}
		for (let i = 0; i < candidates.length; i++) {
			if (
				chosen.length == 0 ||
				candidates[i] >= chosen[chosen.length - 1]
			) {
				const nextChosen = [...chosen, candidates[i]];
				dfs(nextChosen, total + candidates[i]);
			}
		}
	};
	dfs([], 0);
	return res;
};
