/*
    2nd: hashtable
    - similar to lc5
    - similar to algoexpert: largest range

    Time    O(N)
    Space   O(N)
    84 ms, faster than 67.86%
*/
var longestConsecutive = function (nums) {
	const numSet = new Set(nums);
	const seen = new Set();
	let res = 0;
	for (let i = 0; i < nums.length; i++) {
		const x = nums[i];

		// stop if explored
		if (seen.has(x)) {
			continue;
		}
		seen.add(x);

		// explore to the left
		let left = x;
		while (numSet.has(left - 1)) {
			left -= 1;
			seen.add(left);
		}

		// explore to the right
		let right = x;
		while (numSet.has(right + 1)) {
			right += 1;
			seen.add(right);
		}
		res = Math.max(res, right - left + 1);
	}
	return res;
};
