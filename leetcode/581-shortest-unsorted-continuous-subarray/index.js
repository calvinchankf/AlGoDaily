/*
    1st approach:
	1. compare the nums with its sorted result
	2. 2 pointers to look for the boundaries

	Time	O(nlogn)
	Space	O(n)
	108 ms, faster than 53.37%
*/
var findUnsortedSubarray = function (nums) {
	const n = nums.length;
	const clone = [...nums];
	clone.sort((a, b) => a - b);

	let i = -1;
	while (i + 1 < n && nums[i + 1] == clone[i + 1]) {
		i += 1;
	}

	if (i + 1 == n) {
		return 0;
	}

	let j = n;
	while (j - 1 >= 0 && nums[j - 1] == clone[j - 1]) {
		j -= 1;
	}

	return j - i - 1;
};
