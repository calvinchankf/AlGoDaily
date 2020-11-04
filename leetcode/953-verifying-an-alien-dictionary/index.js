/*
    1st: brute force to compare every charactor with a hashtable

    Time    O(MN)
    Space   O(N)
    20 ms, faster than 90.49%
*/
var isAlienSorted = function (words, order) {
	const mapping = {};
	for (let i = 0; i < order.length; i++) {
		mapping[order[i]] = i;
	}
	for (let i = 1; i < words.length; i++) {
		const prev = words[i - 1];
		const cur = words[i];
		const n = Math.min(prev.length, cur.length);
		for (let j = 0; j < n; j++) {
			const p = prev[j];
			const c = cur[j];
			if (mapping[p] < mapping[c]) {
				break;
			} else if (mapping[p] > mapping[c]) {
				return false;
			}
		}
		if (prev.slice(0, n) === cur.slice(0, n) && prev.length > cur.length) {
			return false;
		}
	}
	return true;
};
