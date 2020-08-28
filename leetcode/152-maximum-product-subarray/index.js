/*
    3rd approach: Kadan's algorithm
    - idea similar to leetcode 53:maximum subarray
    - for each item, store the max&mix among itself, or extend the previous max&min with itself
      e.g. dp[i] chooses between dp[i-1]+nums[i] and nums[i]
    - the result is the largest dp[i]
    - see ./idea.jpeg

    Time	O(n)
    Space	O(n)
    120 ms, faster than 16.10%
*/
var maxProduct = function (nums) {
	let minP = Number.MAX_SAFE_INTEGER;
	let maxP = Number.MIN_SAFE_INTEGER;
	let res = Number.MIN_SAFE_INTEGER;
	for (let x of nums) {
		if (x > 0) {
			minP = Math.min(x, x * minP);
			maxP = Math.max(x, x * maxP);
		} else {
			const temp = minP;
			minP = Math.min(x, x * maxP);
			maxP = Math.max(x, x * temp);
		}
		res = Math.max(res, maxP);
	}
	return res;
};
