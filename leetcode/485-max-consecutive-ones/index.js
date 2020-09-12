/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function (nums) {
	let res = 0;
	let count = 0;
	for (let x of nums) {
		if (x == 1) {
			count += 1;
		} else {
			count = 0;
		}
		res = Math.max(res, count);
	}
	return res;
};
