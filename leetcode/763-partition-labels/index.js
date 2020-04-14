/*
    2nd approach:
    - we can just save the char: last index in the hashtable
    - find the farthest reach of deletion during iteration
    - once i == farthest reach, the substring between i and previous end(this start point) is the result

    Time    O(n)
    Space   O(n)
    52 ms, faster than 98.36%
*/

/**
 * @param {string} S
 * @return {number[]}
 */
var partitionLabels = function (S) {
	const ht = {};
	for (let i = 0; i < S.length; i++) {
		const c = S[i];
		ht[c] = i;
	}
	const res = [];
	let startPoint = -1;
	let farthest = -1;
	for (let i = 0; i < S.length; i++) {
		const c = S[i];
		farthest = Math.max(farthest, ht[c]);
		if (i == farthest) {
			res.push(farthest - startPoint);
			startPoint = i;
		}
	}
	return res;
};
