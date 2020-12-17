/*
    sliding window(2 pointers)
	- similar to lc3, 76
	- fast pointer to find the next item which sum up > target
	- once each the target, move the slow pointer to the right to see if the sum persist if sum = sum - nums[slow]

	Time	O(2n)
	Space 	O(1)
	80 ms, faster than 72.22%
*/
var minSubArrayLen = function(s, nums) {
    let j = 0
    let curSum = 0
    let minSize = 2**32
    for (let i = 0; i < nums.length; i++) {
        const x = nums[i]
        curSum += x
        while (curSum >= s) {
            minSize = Math.min(minSize, i - j + 1)
            let left = nums[j]
            j += 1
            curSum -= left 
        }
    }
    if (minSize == 2**32) { return 0 }
    return minSize
};