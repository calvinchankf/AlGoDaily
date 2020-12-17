/*
    2nd approach: 2 pointers
    - similar to lc26, 75, 283
    - slow pointer points to the right most distinct number
    - fast pointer is for iteration
    - if fast pointer meets a different value, slow pointer move forward and modify the numer as the fast pointer points to

    Time    O(n)
    Space   O(1)
    124 ms, faster than 13.55%
*/
var removeDuplicates = function (nums) {
	if (nums.length == 0) {
		return 0;
	}
	let j = 0;
	let curNum = Number.MIN_SAFE_INTEGER;
	let curCount = 0;
	for (let i = 0; i < nums.length; i++) {
		if (nums[i] != curNum) {
			curNum = nums[i];
			[nums[i], nums[j]] = [nums[j], nums[i]];
			j += 1;
			curCount = 1;
		} else if (nums[i] == curNum && curCount < 2) {
			[nums[i], nums[j]] = [nums[j], nums[i]];
			j += 1;
			curCount += 1;
		}
	}
	return j;
};
