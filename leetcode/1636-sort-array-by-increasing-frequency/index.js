/*
    1st: hashtable + sort

    Time    O(NlogN)
    Space   O(N)
    104 ms, faster than 50.38%
*/
var frequencySort = function(nums) {
    const counter = {}
    let maxFreq = 0
    for (let x of nums) {
        if (x in counter == false) {
            counter[x] = 0
        }
        counter[x] += 1
        maxFreq = Math.max(maxFreq, counter[x])
    }
    const freqs = {}
    for (let key in counter) {
        const f = counter[key]
        if (f in freqs == false) {
            freqs[f] = []
        }
        freqs[f].push(key)
    }
    let res = []
    for (let i = 0; i <= maxFreq; i++) {
        if (i in freqs) {
            const arr = freqs[i]
            arr.sort((a, b) => b - a)
            for (let x of arr) {
                res = res.concat(Array(i).fill(x))
            }
        }
    }
    return res
};