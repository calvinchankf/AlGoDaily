/*
    1st approach
    - for each charactor, expand its left and right if palindrome

    Time    O(n^2)
    Space   O(1)
    100 ms, faster than 78.74%
*/
var longestPalindrome = function (s) {
	let left = 0;
	let right = 0;
	for (let i = 0; i < s.length; i++) {
		const [a1, b1] = expand(s, i - 1, i);
		const [a2, b2] = expand(s, i, i);
		if (b1 - a1 > right - left) {
			left = a1;
			right = b1;
		}
		if (b2 - a2 > right - left) {
			left = a2;
			right = b2;
		}
	}
	return s.slice(left, right + 1);
};

const expand = (s, i, j) => {
	if (i < 0) {
		return [j, j];
	} else if (s[i] != s[j]) {
		return [j, j];
	}
	while (i - 1 >= 0 && j + 1 < s.length && s[i - 1] === s[j + 1]) {
		i -= 1;
		j += 1;
	}
	return [i, j];
};
