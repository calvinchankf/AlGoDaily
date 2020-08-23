/*
    1st approach: intervals
    - if the last interval ends at cur-1, we extend the last interval
    - else we create a new interval and append it to the intervals array

    Time    O(2n)
    Space   O(n)
    100 ms, faster than 15.60% 
*/
var summaryRanges = function (nums) {
	if (!nums || nums.length == 0) {
		return [];
	}
	const n = nums.length;
	const intvs = [];
	let i = 0;
	for (let j = 0; j < n; j++) {
		if (nums[j - 1] + 1 < nums[j]) {
			intvs.push([i, j - 1]);
			i = j;
		}
	}
	intvs.push([i, n - 1]);
	const res = [];
	for (let [i, j] of intvs) {
		if (i == j) {
			res.push(`${nums[i]}`);
		} else {
			res.push(`${nums[i]}->${nums[j]}`);
		}
	}
	return res;
};

/*
    2nd approach: optimize 1st in one loop

    Time    O(2n)
    Space   O(n)
    100 ms, faster than 15.60% 
*/
var summaryRanges = function (nums) {
	if (!nums || nums.length == 0) {
		return [];
	}
	const n = nums.length;
	const res = [];
	let i = 0;
	let j = 0;
	for (; j < n; j++) {
		if (nums[j - 1] + 1 < nums[j]) {
			if (i == j - 1) {
				res.push(`${nums[i]}`);
			} else {
				res.push(`${nums[i]}->${nums[j - 1]}`);
			}
			i = j;
		}
	}
	if (i == j - 1) {
		res.push(`${nums[i]}`);
	} else {
		res.push(`${nums[i]}->${nums[j - 1]}`);
	}
	return res;
};
