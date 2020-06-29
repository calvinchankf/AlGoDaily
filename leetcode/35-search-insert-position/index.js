/*
    1st approach: lower bound binary search

    Time    O(logn)
    Space   O(1)
    68 ms, faster than 57.76%
*/
var searchInsert = function (nums, target) {
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
