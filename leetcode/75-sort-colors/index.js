/*
    2nd approach:
	- move the zeros to the front
	- move the twos to the back
	- see leetcode 283) moving zeros

	Time	O(n)
	Space	O(2)
	68ms beats 38.01%
*/
var sortColors = function (nums) {
	let nonZeroIdx = 0;
	for (let i = 0; i < nums.length; i++) {
		if (nums[i] === 0) {
			[nums[i], nums[nonZeroIdx]] = [nums[nonZeroIdx], nums[i]];
			nonZeroIdx += 1;
		}
	}
	let nonTwoIdx = nums.length - 1;
	for (let i = nums.length - 1; i >= 0; i--) {
		if (nums[i] === 2) {
			[nums[i], nums[nonTwoIdx]] = [nums[nonTwoIdx], nums[i]];
			nonTwoIdx -= 1;
		}
	}
};
