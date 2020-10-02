/*
    2nd approach: hashtables
    
    - Compute a word's "signature"

    e.g.
    bbacyba
    0012301

    xxyzwxy
    0012301

    Time  O(n)
    Space O(n)
    88 ms, faster than 66.67%
*/
var isIsomorphic = function (s, t) {
	const a = getSignature(s);
	const b = getSignature(t);
	return a == b;
};

const getSignature = (s) => {
	const ht = {};
	let res = "";
	for (let c of s) {
		if (c in ht === false) {
			ht[c] = Object.keys(ht).length;
		}
		res += ht[c] + ",";
	}
	return res;
};
