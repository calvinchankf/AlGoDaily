function fourNumberSum(nums, target) {
	// Write your code here.
	nums.sort((a, b) => a - b);
	const res = [];
	for (let h = 0; h < nums.length - 3; h++) {
		for (let i = h + 1; i < nums.length - 2; i++) {
			let left = i + 1;
			let right = nums.length - 1;
			while (left < right) {
				const sum = nums[h] + nums[i] + nums[left] + nums[right];
				if (sum === target) {
					res.push([nums[h], nums[i], nums[left], nums[right]]);
					left += 1;
					right -= 1;
				} else if (sum < target) {
					left += 1;
				} else {
					right -= 1;
				}
			}
		}
	}
	return res;
}

// Do not edit the line below.
exports.fourNumberSum = fourNumberSum;
