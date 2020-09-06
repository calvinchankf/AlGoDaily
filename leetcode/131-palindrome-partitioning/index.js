/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function (s) {
	const res = [];

	const reverse = (str) => {
		let cur = "";
		for (let i = str.length - 1; i >= 0; i--) {
			cur += str[i];
		}
		return cur;
	};

	const dfs = (remain, cur) => {
		if (remain.length == 0) {
			return res.push(cur);
		}
		for (let i = 0; i < remain.length; i++) {
			const sub = remain.slice(0, i + 1);
			if (sub == reverse(sub)) {
				dfs(remain.slice(i + 1), [...cur, sub]);
			}
		}
	};
	dfs(s, []);

	return res;
};
