/*
    1st approach: 2 hashtables

    Time    O(n)
    Space   O(n)
    68 ms, faster than 92.28%
*/
var wordPattern = function (pattern, s) {
	const words = s.split(" ");
	if (words.length !== pattern.length) {
		return false;
	}
	const forward = {};
	const backward = {};
	for (let i = 0; i < words.length; i++) {
		const p = pattern[i];
		const w = words[i];

		if (p in forward && forward[p] !== w) {
			return false;
		}
		if (w in backward && backward[w] !== p) {
			return false;
		}

		forward[p] = w;
		backward[w] = p;
	}
	return true;
};
