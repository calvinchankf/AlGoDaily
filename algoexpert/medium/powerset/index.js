function powerset(array) {
	// Write your code here.
	const res = [];
	const dfs = (chosen, cands) => {
		res.push(chosen);
		for (let i = 0; i < cands.length; i++) {
			const nextChosen = [...chosen, cands[i]];
			const nextCands = cands.slice(i + 1);
			dfs(nextChosen, nextCands);
		}
	};
	dfs([], array);

	return res;
}

// Do not edit the line below.
exports.powerset = powerset;
