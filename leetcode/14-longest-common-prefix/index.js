/*
    2nd approach:
	- instead of appending charactors so many times, slice the end
    
	Time		O(n*m)
	Space		O(m)
	80 ms, faster than 75.62%
*/
var longestCommonPrefix = function (strs) {
	const n = strs.length;
	if (n == 0) {
		return "";
	}
	let res = strs[0];
	for (let i = 1; i < n; i++) {
		const s = strs[i];
		let j = 0;
		while (j < res.length && j < s.length) {
			if (s[j] !== res[j]) {
				break;
			}
			j += 1;
		}
		res = s.slice(0, j);
	}
	return res;
};
