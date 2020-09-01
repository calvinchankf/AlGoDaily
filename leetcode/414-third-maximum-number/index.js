/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function (nums) {
	let max1 = Number.MIN_SAFE_INTEGER;
	let max2 = Number.MIN_SAFE_INTEGER;
	let max3 = Number.MIN_SAFE_INTEGER;
	for (let x of nums) {
		if (x > max1) {
			max3 = max2;
			max2 = max1;
			max1 = x;
		} else if (x > max2 && x < max1) {
			max3 = max2;
			max2 = x;
		} else if (x > max3 && x < max2) {
			max3 = x;
		}
	}
	if (max3 == Number.MIN_SAFE_INTEGER) {
		return max1;
	}
	return max3;
};
