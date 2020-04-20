/*
    2nd learned from others:

    ref:
    - https://leetcode.com/problems/valid-parenthesis-string/discuss/107570/JavaC%2B%2BPython-One-Pass-Count-the-Open-Parenthesis
    - https://www.cnblogs.com/grandyang/p/7617017.html

    Time    O(n)
    Space   O(1)
    52 ms, faster than 74.55%
*/

/**
 * @param {string} s
 * @return {boolean}
 */
var checkValidString = function (s) {
	let minOpen = 0;
	let maxOpen = 0;
	for (let c of s) {
		if (c == "(") {
			minOpen += 1;
			maxOpen += 1;
		} else if (c == ")") {
			minOpen = Math.max(minOpen - 1, 0);
			maxOpen -= 1;
		} else {
			minOpen = Math.max(minOpen - 1, 0);
			maxOpen += 1;
		}
		if (maxOpen < 0) {
			return false;
		}
	}
	return minOpen == 0;
};
