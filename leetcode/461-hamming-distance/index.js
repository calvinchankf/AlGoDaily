/*
    2nd: bit op
    - get the bit operation of both numbers
    - find the diff

    Time    O(logM + logN)
    Space   O(64)
    96 ms, faster than 9.14%
*/
var hammingDistance = function (x, y) {
	let res = 0;
	while (x > 0 || y > 0) {
		const a = x & 1;
		const b = y & 1;
		res += a !== b;
		x >>= 1;
		y >>= 1;
	}
	return res;
};
