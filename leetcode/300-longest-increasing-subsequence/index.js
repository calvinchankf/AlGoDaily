/*
    1st approach: dynamic programming
    - similar to lc354, 646

    ref: Longest Increasing Subsequence
    - https://www.youtube.com/watch?v=CE2b_-XfVDk

    Time    O(n^2)
    Space   O(n)
    96 ms, faster than 55.81%
*/
var lengthOfLIS = function (nums) {
	if (nums.length == 0) {
        return 0
    }
    const n = nums.length
    const dp = Array(n).fill(1)
    for (let i = 0; i < n; i++) {
        let maxCount = 0
        for (let j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                maxCount = Math.max(maxCount, dp[j])
            }
        }
        dp[i] += maxCount
    }
    return Math.max(...dp)
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
