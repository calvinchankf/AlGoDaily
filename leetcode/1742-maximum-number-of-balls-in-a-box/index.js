/*
    1st: hashtable

    Time    O(NC)
    Space   O(N)
    148 ms, faster than 100.00%
*/
var countBalls = function(lowLimit, highLimit) {
    const counter = {}
    for (let i = lowLimit; i <= highLimit; i++) {
        const s = `${i}`
        let num = 0
        for (let c of s) {
            num += parseInt(c)
        }
        if (num in counter == false) {
            counter[num] = 0
        }
        counter[num] += 1
    }
    let maxCount = 0
    for (let key in counter) {
        maxCount = Math.max(maxCount, counter[key])
    }
    return maxCount
};