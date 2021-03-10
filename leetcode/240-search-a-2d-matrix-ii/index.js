/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function (matrix, target) {
	for (let row of matrix) {
		const b = bsearch(row, target);
		if (b > -1) {
			return true;
		}
	}
	return false;
};

const bsearch = (nums, target) => {
	let left = 0;
	let right = nums.length - 1;
	while (left <= right) {
		const mid = Math.floor((left + right) / 2);
		if (target < nums[mid]) {
			right = mid - 1;
		} else if (target > nums[mid]) {
			left = mid + 1;
		} else {
			return mid;
		}
	}
	return -1;
};
