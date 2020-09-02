/*
    1st approach: dynamic programming
    - similar to lc646

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

let a;
a = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35];
console.log(lengthOfLIS(a));

/*
    follow up: print the subsequence
*/
var printLIS = function (nums) {
	const n = nums.length;
	const dp = [];
	for (let i = 0; i < n; i++) {
		dp.push([nums[i]]);
	}
	for (let i = 0; i < n; i++) {
		for (let j = 0; j < i; j++) {
			if (nums[j] < nums[i]) {
				if (dp[j].length + 1 > dp[i].length) {
					dp[i] = [...dp[j], nums[i]];
				}
			}
		}
	}
	console.log(dp);
	let res = [];
	for (let i = 0; i < n; i++) {
		if (dp[i].length > res.length) {
			res = dp[i];
		}
	}
	return res;
};

a = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35];
console.log(printLIS(a));
