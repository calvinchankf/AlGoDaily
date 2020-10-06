/*
    2nd approach: zero sum subarray
    - this question is fucking similar to leetcode523, 525, 560, 930, 1124, 1171
    - learned from others: https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/discuss/77807/Clean-python-solution-one-pass
    - the basic idea is to store the previous sum in a hashtable
        e.g. key: previous sum, value: index of the previous sum
    - if currentSum - target in the hastable, the result is currentIndex - hastable[previous sum]

    ref:
    - https://www.youtube.com/watch?v=hLcYp67wCcM

    Time O(n)
    Space O(n) hashtable
    104 ms, faster than 74.83%
*/
var maxSubArrayLen = function (nums, k) {
	let res = 0;
	const ht = {};
	let pfs = 0;
	for (let i = 0; i < nums.length; i++) {
		const x = nums[i];
		pfs += x;
		if (pfs === k) {
			res = i + 1;
		}
		const remain = pfs - k;
		if (remain in ht) {
			res = Math.max(res, i - ht[remain]);
		}
		if (pfs in ht === false) {
			ht[pfs] = i;
		}
	}
	return res;
};
