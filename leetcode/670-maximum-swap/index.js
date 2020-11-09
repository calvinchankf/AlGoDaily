/*
    1st approach: brute-force
    - try all the pairs to swap
    - find the max number
    - since the input is at most 1x10^8, there are at most 8*7 trials

    Time    O(logn x logn x logn)
    Space   O(logn) save the digit
    84 ms, faster than 20.53%
*/
var maximumSwap = function(num) {
    const nums = []
    const s = `${num}`
    for (let i = 0; i < s.length; i++) {
        nums.push(parseInt(s[i]))
    }
    let maxNum = num
    for (let i = 0; i < nums.length; i++) {
        for (let j = i+1; j < nums.length; j++) {
            // swap
            [nums[i], nums[j]] = [nums[j], nums[i]]
            const s = nums.join('')
            const temp = parseInt(s)
            if (temp > maxNum) {
                maxNum = temp
            }
            // swap back
            [nums[i], nums[j]] = [nums[j], nums[i]]
        } 
    }
    return maxNum
};