/*
    1st: 2 pointers

    Time    O(n)
    Space   O(1)
    68ms beats 79.77%
*/
var isSubsequence = function (s, t) {
	let i = 0; // s
	let j = 0; // t
	for (; j < t.length; j++) {
		if (s[i] == t[j]) {
			i += 1;
		}
	}
	return i == s.length;
};
