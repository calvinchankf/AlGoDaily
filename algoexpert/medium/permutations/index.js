function getPermutations(array) {
	// Write your code here.
	const n = array.length;
	const res = [];
	const dfs = (chosen, cands) => {
		if (chosen.length == n) {
			if (chosen.length > 0) {
				res.push(chosen);
			}
			return;
		}
		for (let i = 0; i < cands.length; i++) {
			const nextChosen = [...chosen, cands[i]];
			const nextCands = [...cands.slice(0, i), ...cands.slice(i + 1)];
			dfs(nextChosen, nextCands);
		}
	};
	dfs([], array);

	return res;
}

// Do not edit the line below.
exports.getPermutations = getPermutations;
