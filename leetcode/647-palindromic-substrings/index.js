/*
    1st approach: expand from center like lc5

    Time    O(n^2)
    Space   O(1)
    92 ms, faster than 71.19%
*/
var countSubstrings = function (s) {
	let res = 0;
	for (let i = 0; i < s.length; i++) {
		res += explore(s, i - 1, i);
		res += explore(s, i, i);
	}
	return res;
};

const explore = (s, left, right) => {
	let i = left;
	let j = right;
	if (i < 0) {
		return 0;
	}
	if (s[i] != s[j]) {
		return 0;
	}
	let count = 1;
	while (i - 1 >= 0 && j + 1 < s.length && s[i - 1] == s[j + 1]) {
		count += 1;
		i -= 1;
		j += 1;
	}
	return count;
};
