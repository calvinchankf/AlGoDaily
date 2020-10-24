/*
    1st: sliding window

    Time    O(n)
    Space   O(n)
    80 ms, faster than 51.49%
*/
var findLengthOfLCIS = function(nums) {
    if (nums.length <= 1) {
        return nums.length
    }
    let res = 0
    let cur = 1
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] > nums[i-1]) {
            cur += 1
        } else {
            cur = 1
        }
        res = Math.max(res, cur)
    }
    return res
};