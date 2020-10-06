/*
    1st: hashtable

    Time    O(N)
    Space   O(N)
	112 ms, faster than 71.60%
*/
var firstUniqChar = function (s) {
	const ht = {};
	for (let c of s) {
		if (c in ht) {
			ht[c] += 1;
		} else {
			ht[c] = 1;
		}
	}
	for (let i = 0; i < s.length; i++) {
		const c = s[i];
		if (ht[c] === 1) {
			return i;
		}
	}
	return -1;
};
