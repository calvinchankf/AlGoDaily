/*
    sort

    Time    O(NlogN)
    Space   O(1)
    128ms beats 39.95%
*/
var maximumProduct = function(nums) {
    nums.sort((a, b) => a - b)
    const n = nums.length
    const a = nums[n-3] * nums[n-2] * nums[n-1]
    const b = nums[0] * nums[1] * nums[n-1]
    return Math.max(a, b)
};