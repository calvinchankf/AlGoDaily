/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function (digits) {
	if (digits.length == 0) {
		return [];
	}
	const ht = {
		"2": ["a", "b", "c"],
		"3": ["d", "e", "f"],
		"4": ["g", "h", "i"],
		"5": ["j", "k", "l"],
		"6": ["m", "n", "o"],
		"7": ["p", "q", "r", "s"],
		"8": ["t", "u", "v"],
		"9": ["w", "x", "y", "z"],
	};
	const n = digits.length;
	const res = [];

	const dfs = (cands, chosen) => {
		if (cands.length === 0) {
			if (chosen.length > 0) {
				res.push(chosen);
			}
			return;
		}
		const c = cands[0];
		if (c in ht) {
			for (let cand of ht[c]) {
				dfs(cands.slice(1), chosen + cand);
			}
		} else {
			dfs(cands.slice(1), chosen);
		}
	};
	dfs(digits, "");
	return res;
};
