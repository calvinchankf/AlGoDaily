/*
    1st: 2 sum
*/
function threeNumberSum(array, targetSum) {
	// Write your code here.
	array.sort((a, b) => a - b);
	const res = [];
	for (let i = 0; i < array.length; i++) {
		const ht = {};
		for (let j = i + 1; j < array.length; j++) {
			const remain = targetSum - array[i] - array[j];
			if (remain in ht) {
				const k = ht[remain];
				res.push([array[i], array[k], array[j]]);
			}
			ht[array[j]] = j;
		}
	}
	res.sort((a, b) => {
		if (a[0] == b[0]) {
			return a[1] - b[1];
		}
		return a[0] - b[0];
	});
	return res;
}

/*
    2nd: 2 pointers
*/
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
	nums.sort((a, b) => a - b);
	const res = [];
	for (let i = 0; i < nums.length - 2; i++) {
		// avoid redudant pairs
		if (i > 0 && nums[i] == nums[i - 1]) {
			continue;
		}
		// */
		let left = i + 1;
		let right = nums.length - 1;
		while (left < right) {
			const sum = nums[i] + nums[left] + nums[right];
			if (sum === 0) {
				res.push([nums[i], nums[left], nums[right]]);

				// avoid redudant pairs
				while (left < right && nums[left] == nums[left + 1]) {
					left += 1;
				}
				left += 1;
				while (left < right && nums[right - 1] == nums[right]) {
					right -= 1;
				}
				right -= 1;
				//*/
			} else if (sum < 0) {
				left += 1;
			} else {
				right -= 1;
			}
		}
	}
	return res;
};
