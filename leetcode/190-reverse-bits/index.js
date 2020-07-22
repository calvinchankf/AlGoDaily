/*
    1st approach: classic bit op similar to leetcode 191

	Time	O(32)
	Space	O(1)
	84 ms, faster than 59.34%
*/
var reverseBits = function (n) {
	let res = 0;
	let i = 0;
	while (i < 32) {
		const temp = n & 1;
		res = res * 2 + temp;
		n >>= 1;
		i += 1;
	}
	return res;
};
