/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function (nums) {
	let largest = Number.MIN_SAFE_INTEGER;
	let largest2 = Number.MIN_SAFE_INTEGER;
	for (let i = 0; i < nums.length; i++) {
		if (nums[i] > largest) {
			largest2 = largest;
			largest = nums[i];
		} else if (nums[i] > largest2) {
			largest2 = nums[i];
		}
	}
	return (largest - 1) * (largest2 - 1);
};
