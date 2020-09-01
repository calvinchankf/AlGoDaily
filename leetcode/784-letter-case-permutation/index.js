/**
 * @param {string} S
 * @return {string[]}
 */
var letterCasePermutation = function (S) {
	const res = [];
	const dfs = (chosen, s) => {
		if (s.length == 0) {
			return res.push(chosen);
		}
		const c = s[0].toLowerCase();
		const idx = c.charCodeAt(0) - "a".charCodeAt(0);
		if (idx >= 0 && idx < 26) {
			const lower = c;
			const upper = c.toUpperCase();
			dfs(chosen + lower, s.slice(1));
			dfs(chosen + upper, s.slice(1));
		} else {
			dfs(chosen + c, s.slice(1));
		}
	};
	dfs("", S);

	return res;
};
