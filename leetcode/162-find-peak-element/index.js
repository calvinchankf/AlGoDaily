/*
    2nd: lower bound binary search
    - similar to lc162, 852
    - when the next item is smaller, the peak is on the left hand side
    - actually same as 2nd, but the left & right are always within boundary

    Time    O(logN)
    Space   O(1)
    72 ms, faster than 93.39%
*/
var findPeakElement = function (nums) {
	let left = 0;
	let right = nums.length-1;
	while (left < right) {
		const mid = Math.floor((left + right) / 2);
		if (nums[mid] >= nums[mid+1]) {
            right = mid;
		} else {
			left = mid + 1;
		}
	}
	return left;
};
