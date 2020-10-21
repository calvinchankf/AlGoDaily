/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function (digits) {
	if (digits.length == 0) {
		return [];
	}
	const ht = {
		2: "abc",
		3: "def",
		4: "ghi",
		5: "jkl",
		6: "mno",
		7: "pqrs",
		8: "tuv",
		9: "wxyz",
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
