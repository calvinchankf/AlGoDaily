/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
	const ht = {};
	const f = (i) => {
		if (i < 0) {
			return 0;
		} else if (i === 0) {
			return 1;
		}
		if (i in ht) {
			return ht[i];
		}
		const temp = f(i - 1) + f(i - 2);
		ht[i] = temp;
		return temp;
	};
	return f(n);
};
