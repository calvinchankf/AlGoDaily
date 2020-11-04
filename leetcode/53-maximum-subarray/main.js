/*
    3rd approach: dynamic programming, kadan's algorithm
    - for each item, store the max either itself or extend the previous sum with itself
      e.g. dp[i] chooses between dp[i-1]+nums[i] and nums[i]
    - the result is the largest dp[i]
    - optimize the 2nd approach by using store one variable for dp array cos for each item
    we just need to compare with previous item result

    Time	O(n)
    Space	O(1)
    100 ms, faster than 27.58%

    ref:
    - https://www.youtube.com/watch?v=2MmGzdiKR9Y

    followups:
    - print the max sum subarray
    - what if circular
*/
var maxSubArray = function (nums) {
	let cur = Number.MIN_SAFE_INTEGER; // or -(2**31)
	let res = Number.MIN_SAFE_INTEGER; // or -(2**31)
	for (let x of nums) {
		cur = Math.max(cur + x, x);
		res = Math.max(res, cur);
	}
	return res;
};
