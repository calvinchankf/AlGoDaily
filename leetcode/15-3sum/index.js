/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
	nums.sort((a, b) => a - b);
	const res = [];
	for (let i = 0; i < nums.length - 2; i++) {
		if (i > 0 && nums[i] == nums[i - 1]) {
			continue;
		}
		let left = i + 1;
		let right = nums.length - 1;
		while (left < right) {
			const sum = nums[i] + nums[left] + nums[right];
			if (sum === 0) {
				res.push([nums[i], nums[left], nums[right]]);
				while (left < right && nums[left] == nums[left + 1]) {
					left += 1;
				}
				left += 1;
				while (left < right && nums[right - 1] == nums[right]) {
					right -= 1;
				}
				right -= 1;
			} else if (sum < 0) {
				left += 1;
			} else {
				right -= 1;
			}
		}
	}
	return res;
};
