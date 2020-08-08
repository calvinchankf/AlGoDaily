/*
    1st approach: dynamic programming

    ref: Longest Increasing Subsequence
    - https://www.youtube.com/watch?v=CE2b_-XfVDk

    Time    O(n^2)
    Space   O(n)
    164 ms, faster than 11.50%
*/
var lengthOfLIS = function (nums) {
	const n = nums.length;
	const dp = Array(n).fill(1);
	for (let i = 0; i < n; i++) {
		for (let j = 0; j < i; j++) {
			if (nums[j] < nums[i]) {
				dp[i] = Math.max(dp[j] + 1, dp[i]);
			}
		}
	}
	let res = 0;
	for (let x of dp) {
		res = Math.max(res, x);
	}
	return res;
};
