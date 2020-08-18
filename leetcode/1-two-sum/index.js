/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
	const n = nums.length;
	const ht = {};
	for (let i = 0; i < n; i++) {
		const x = nums[i];
		const remain = target - x;
		if (remain in ht) {
			return [i, ht[remain]];
		}
		ht[x] = i;
	}
	return [-1, -1];
};
