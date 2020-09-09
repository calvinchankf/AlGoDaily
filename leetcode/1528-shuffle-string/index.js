/*
    Time    O(2N)
    Space   O(N)
    68 ms, faster than 100.00%
*/
var restoreString = function (s, indices) {
	const n = s.length;
	let res = Array(n).fill("");
	for (let i = 0; i < n; i++) {
		const c = s[i];
		const x = indices[i];
		res[x] = c;
	}
	return res.join("");
};
