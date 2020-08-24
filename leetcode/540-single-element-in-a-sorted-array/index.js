/*
    3rd: upper bound binary search on even indeces
    - if nums[mid] == nums[mid+1], the result must be on the right hand side excluding the current nums[mid] and nums[mid+1], so left = mid + 2
    - else the target is the current number or a number from my left hand side

    Time    O(logN)
    Space   O(1)
    104 ms, faster than 8.11%
*/
var singleNonDuplicate = function (nums) {
	let left = 0;
	let right = nums.length;
	while (left < right) {
		let mid = Math.floor((left + right) / 2);
		if (mid % 2 == 1) {
			mid -= 1;
		}
		if (nums[mid] == nums[mid + 1]) {
			left = mid + 2;
		} else {
			right = mid;
		}
	}
	return nums[left];
};
