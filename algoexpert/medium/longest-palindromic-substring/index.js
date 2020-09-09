function longestPalindromicSubstring(s) {
	// Write your code here.
	let res = "";
	for (let i = 0; i < s.length; i++) {
		const a = expand(s, i - 1, i); // abba
		const b = expand(s, i, i); //   aba
		if (a.length > res.length) {
			res = a;
		}
		if (b.length > res.length) {
			res = b;
		}
	}
	return res;
}

const expand = (s, left, right) => {
	let i = left;
	let j = right;
	if (i < 0) {
		return "";
	}
	if (s[i] != s[j]) {
		return "";
	}
	while (i - 1 >= 0 && j + 1 < s.length && s[i - 1] == s[j + 1]) {
		i -= 1;
		j += 1;
	}
	return s.slice(i, j + 1);
};

// Do not edit the line below.
exports.longestPalindromicSubstring = longestPalindromicSubstring;
