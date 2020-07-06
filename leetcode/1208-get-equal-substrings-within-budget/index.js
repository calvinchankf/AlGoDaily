/*
    1st: sliding window
    - similar to lc904

    Time    O(2N)
    Space   O(N)
     80 ms, faster than 30.77%
*/

/**
 * @param {string} s
 * @param {string} t
 * @param {number} maxCost
 * @return {number}
 */
var equalSubstring = function (s, t, maxCost) {
	let res = 0;
	let curLen = 0;
	let curCost = 0;
	for (let i = 0; i < s.length; i++) {
		curLen += 1;
		curCost += Math.abs(s[i].charCodeAt(0) - t[i].charCodeAt(0));
		while (curCost > maxCost) {
			curCost -= Math.abs(
				s[i - curLen + 1].charCodeAt(0) -
					t[i - curLen + 1].charCodeAt(0)
			);
			curLen -= 1;
		}
		res = Math.max(res, curLen);
	}
	return res;
};
