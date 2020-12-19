/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findPairs = function(nums, k) {
    const counter = {}
    for (let x of nums) {
        if (x in counter === false) {
            counter[x] = 0
        }
        counter[x] += 1
    }
    nums.sort((a, b) => a - b)
    const res = new Set()
    for (let x of nums) {
        const remain = x - k
        if (remain in counter) {
            if (remain != x || counter[x] > 1) {
                const key = `${remain},${x}`
                res.add(key)
            }
        }
    }
    return res.size
};