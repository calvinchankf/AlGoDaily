/*
    2nd approach: back and forth array
    - similar to lc42, 842, 915
    - from the front to the end, store the min at each index
    - from the end to the front, store the max at each index
    - when forward[i] < num[i] < backward[i], there is a result

    e.g.        [8,3,5,1,6]
    forward ->   8 3 3 1 1
    backward <-  8 6 6 6 6  
    at index 2, forward[2] < nums[2] < backward[2] = 3 < 5 < 6

    Time    O(n)
    Space   O(n)
    80 ms, faster than 65.42%
*/
var increasingTriplet = function(nums) {
    const n = nums.length
    if (n == 0) { return false }
    let leftMin = 2**32
    const forward = Array(n).fill(0)
    for (let i = 0; i < n; i++) {
        leftMin = Math.min(leftMin, nums[i])
        forward[i] = leftMin
    }
    let rightMax = -(2**32)
    const backward = Array(n).fill(0)
    for (let i = n-1; i >= 0; i--) {
        rightMax = Math.max(rightMax, nums[i])
        backward[i] = rightMax
    }
    for (let i = 1; i < n-1; i++) {
        if (forward[i-1] < nums[i] && nums[i] < backward[i+1]) {
            return true
        }
    }
    return false
};