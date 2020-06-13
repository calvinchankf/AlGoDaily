/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function (nums) {
	let firstZero = 0;
	for (let i = 0; i < nums.length; i++) {
		if (nums[i] != 0) {
			[nums[firstZero], nums[i]] = [nums[i], nums[firstZero]];
			firstZero++;
		}
	}
};
