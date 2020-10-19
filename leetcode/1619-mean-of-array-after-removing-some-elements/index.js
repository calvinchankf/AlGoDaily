/*
    1st: math    

    Time    O(N)
    Space   O(1)
    84 ms, faster than 100.00%
*/
var trimMean = function(arr) {
    const n = arr.length
    arr.sort((a, b) => a - b)
    const fivePercent = n * 0.05
    let total = 0
    let count = 0
    for (let i = fivePercent; i < n - fivePercent; i++) {
        total += arr[i]
        count += 1
    }
    return total/count
};