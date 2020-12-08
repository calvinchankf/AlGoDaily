/*
    3rd approach: Kadan's algorithm
    - idea similar to leetcode 53:maximum subarray
    - for each item, store the max&mix among itself, or extend the previous max&min with itself
      e.g. dp[i] chooses between dp[i-1]+nums[i] and nums[i]
    - the result is the largest dp[i]
    - see ./idea.jpeg

    Time	O(N)
    Space	O(N)
    76 ms, faster than 94.10%
*/
var maxProduct = function (nums) {
	let minP = 2**32
    let maxP = -(2**32)
    let res = -(2**32)
    for (let x of nums) {
        if (x >= 0) {
            minP = Math.min(minP * x, x)
            maxP = Math.max(maxP * x, x)
        } else {
            const temp = minP
            minP = Math.min(maxP * x, x)
            maxP = Math.max(temp * x, x)
        }
        res = Math.max(res, maxP)
    }
    return res
};
