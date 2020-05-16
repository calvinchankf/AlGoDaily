/*
    1st: math

    Time    O(N)
    Space   O(1)
    52 ms, faster than 100.00%
*/

/**
 * @param {string} s
 * @param {number[][]} shift
 * @return {string}
 */
var stringShift = function (s, shift) {
	let finalShift = 0;
	for (let [dir, amount] of shift) {
		if (dir == 0) {
			finalShift -= amount;
		} else {
			finalShift += amount;
		}
	}
	finalShift %= s.length;
	const ptr = (s.length - finalShift) % s.length;
	return s.substring(ptr, s.length) + s.substring(0, ptr);
};
