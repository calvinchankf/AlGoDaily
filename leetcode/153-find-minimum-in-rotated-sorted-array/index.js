/*
    - find the pivot point
    - when the range on the right hand side is increasing, the pivot is on the left (with the mid point)
    - else the pivot point is on the right hand side (without the mid point)
    - keep in mind that we always maintain the current minimum at index left

    e.g.1
    [4,5,1,2,3]
         ^

    e.g.2
    [3,4,5,1,2]
         ^

    Time    O(logN)
    Space   O(1)
    68 ms, faster than 83.09% 
*/
var findMin = function (nums) {
	let left = 0;
	let right = nums.length - 1;
	while (left <= right) {
		// if no left most < right most, the minval is the left most number
		if (nums[left] <= nums[right]) {
			return nums[left];
		}
		const mid = Math.floor((left + right) / 2);
		// this is so similar to lower bound,
		// both < and <= work fine because there are duplicate numbers
		if (nums[mid] < nums[right]) {
			right = mid;
		} else {
			left = mid + 1;
		}
	}
	return nums[left];
};
