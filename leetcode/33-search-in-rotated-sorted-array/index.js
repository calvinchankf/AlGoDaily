/*
    2nd approach: still binary search but refactor a bit for understanding

    Time	O(logn)
    Space	O(1)
    100 ms, faster than 5.49% <- its weird
*/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
	let left = 0;
	let right = nums.length - 1;
	while (left <= right) {
		const mid = Math.floor((left + right) / 2);
		if (target < nums[mid]) {
			if (target >= nums[left] || nums[left] > nums[mid]) {
				right = mid - 1;
			} else {
				left = mid + 1;
			}
		} else if (target > nums[mid]) {
			if (target <= nums[right] || nums[mid] > nums[right]) {
				left = mid + 1;
			} else {
				right = mid - 1;
			}
		} else {
			return mid;
		}
	}
	return -1;
};
