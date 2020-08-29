/*
    1st: sort + brute force dp
    - sort the envelops by area(w * h)
    - dp it by the logic similar to lc300: Longest Increasing Subsequence

    Time    O(N^2)
    Space   O(N)
    524 ms, faster than 33.71% <- LTE in python, but AC in JS
*/
var maxEnvelopes = function (envelopes) {
	const n = envelopes.length;
	if (n == 0) {
		return 0;
	}
	const nums = [...envelopes];
	nums.sort((a, b) => a[0] * a[1] - b[0] * b[1]);
	// console.log(nums)
	const dp = Array(n).fill(0);
	for (let i = 0; i < n; i++) {
		let maxPrev = 0;
		for (let j = 0; j < i; j++) {
			if (nums[j][0] < nums[i][0] && nums[j][1] < nums[i][1]) {
				maxPrev = Math.max(maxPrev, dp[j]);
			}
		}
		dp[i] = maxPrev + 1;
	}
	return Math.max(...dp);
};

// 4
a = [
	[5, 4],
	[8, 7],
	[8, 3],
	[6, 4],
	[8, 8],
	[6, 7],
	[2, 3],
	[1, 10],
	[3, 9],
	[10, 2],
	[10, 4],
	[10, 5],
];
console.log(maxEnvelopes(a));
