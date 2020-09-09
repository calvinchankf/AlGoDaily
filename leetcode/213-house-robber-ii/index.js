/*
    1st approach: reuse leetcode 198
	- circular means that we cannot rob houses[0] and houses[n-1] at the same time, so the result is either:
        - from houses[1] to houses[n-2]
        - Or from houses[2] to houses[n-1]

	Time		O(2n)
	Space		O(1)
	72 ms, faster than 71.14%
*/
var rob = function (nums) {
	if (nums.length == 0) {
		return 0;
	} else if (nums.length == 1) {
		return [nums[0]];
	}
	const n = nums.length;
	const a = rob1(nums.slice(0, n - 1));
	const b = rob1(nums.slice(1, n));
	return Math.max(a, b);
};

var rob1 = function (nums) {
	let rob = 0;
	let notRob = 0;
	for (let x of nums) {
		let temp = rob;
		rob = Math.max(rob, notRob + x);
		notRob = temp;
	}
	return Math.max(rob, notRob);
};
