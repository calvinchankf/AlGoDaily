/*
    1st: brute force

    Time    O(N^2)
    Space   O(N)
    72 ms, faster than 100.00%
*/

/**
 * @param {string[]} words
 * @return {string[]}
 */
var stringMatching = function (words) {
	const res = new Set();
	for (let i = 0; i < words.length; i++) {
		for (let j = 0; j < words.length; j++) {
			if (i === j) {
				continue;
			}
			if (words[i].indexOf(words[j]) > -1) {
				res.add(words[j]);
			}
		}
	}
	return Array.from(res);
};
