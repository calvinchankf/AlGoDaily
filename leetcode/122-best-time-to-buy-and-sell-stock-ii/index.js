/**
 * 1st: maintain a dip
 * Time     O(N)
 * Space    O(1)
 * 64ms beats 46.52%
 *
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
	let dip = Number.MAX_SAFE_INTEGER;
	let res = 0;
	for (let p of prices) {
		if (p < dip) {
			dip = p;
		}
		diff = p - dip;
		if (diff > 0) {
			res += diff;
			dip = p;
		}
	}
	return res;
};
