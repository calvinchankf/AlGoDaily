/*
    - similar to lc34
*/

function searchForRange(nums, target) {
	// Write your code here.
	const a = lowBsearch(nums, target);
	const b = upBsearch(nums, target);
	if (nums[a] === target && nums[b - 1] === target) {
		return [a, b - 1];
	}
	return [-1, -1];
}

const lowBsearch = (nums, target) => {
	let left = 0;
	let right = nums.length;
	while (left < right) {
		const mid = Math.floor((left + right) / 2);
		if (target <= nums[mid]) {
			right = mid;
		} else {
			left = mid + 1;
		}
	}
	return left;
};

const upBsearch = (nums, target) => {
	let left = 0;
	let right = nums.length;
	while (left < right) {
		const mid = Math.floor((left + right) / 2);
		if (target >= nums[mid]) {
			left = mid + 1;
		} else {
			right = mid;
		}
	}
	return left;
};

// Do not edit the line below.
exports.searchForRange = searchForRange;
