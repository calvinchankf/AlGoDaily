/*
    1st approach: zero sum subarray

    - this question is fucking similar to leetcode 325, 560, 930, 1124, 1171
    - the general idea is transform 0 to -1, do prefix sum
    - if 2 cases:
        1. current prefix sum == 0, nums[:i+1] is a zero sum subarray
        2. if found this prefix sum from the hashtable, it means that there is a loop which we have 0 zero gain

    ref:
    - https://www.youtube.com/watch?v=hLcYp67wCcM

    Time	O(n)
    Space   O(n)
    160 ms, faster than 42.74%
*/
var findMaxLength = function (nums) {
	for (let i = 0; i < nums.length; i++) {
		nums[i] = nums[i] == 0 ? -1 : 1;
	}
	let res = 0;
	const ht = {};
	let pfs = 0;
	for (let i = 0; i < nums.length; i++) {
		pfs += nums[i];
		if (pfs === 0) {
			res = i + 1;
		}
		const remain = pfs;
		if (remain in ht) {
			res = Math.max(res, i - ht[remain]);
		}
		if (pfs in ht === false) {
			ht[pfs] = i;
		}
	}
	return res;
};
