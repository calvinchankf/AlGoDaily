/*
    1st approach: hashtable counter

    Time    O(N)
    Space   O(N)
    96 ms, faster than 50.00%
*/
var findPairs = function(nums, k) {
    const counter = {}
    for (let x of nums) {
        if (x in counter == false) {
            counter[x] = 0
        }
        counter[x] += 1
    }
    const keys = Object.keys(counter)
    let res = 0
    for (let key of keys) {
        const remain = key - k
        if (remain in counter) {
            if (k == 0) {
                if (counter[remain] > 1) {
                    res += 1
                }
            } else {
                res += 1
            }
        }
    }
    return res
};

/*
    2nd approach: sort + hashtable

    Time    O(NlogN)
    Space   O(N)
    60 ms, faster than 85.40%
*/
var findPairs = function(nums, k) {
    nums.sort((a, b) => a - b)
    const seen = new Set()
    const res = new Set()
    for (let x of nums) {
        if (seen.has(x- k)) {
            res.add(`${x-k},${x}`)
        }
        seen.add(x)
    }
    return res.size
};