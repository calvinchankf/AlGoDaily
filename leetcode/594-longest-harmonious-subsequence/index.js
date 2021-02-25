/*
    1st approach: hashtable
    - count the occurence of each number
    - harmonic subsequence is actually the count[num] + count[num+1] or (count[num-1] + count[num])

    e.g. [1,2,1,3,0,0,2,2,1,3,3]

    [1,2,1,3,0,0,2,2,1,3,3]
               ^   ^ ^   ^ arrows represent the last occurence of each number
    
    count = {
        0: 2,
        1: 3,
        2: 3,
        3: 3,
    }

    the answer is count[2] + count[3] = 6

    Time    O(N)
    Space   O(N)
    272 ms, faster than 67.92%
*/
var findLHS = function(nums) {
    const n = nums.length
    const counter = {}
    for (let i = 0; i < n; i++) {
        const x = nums[i]
        if (x in counter) {
            counter[x] += 1
        } else {
            counter[x] = 1
        }
    }
    let res = 0
    for (let i = 0; i < n; i++) {
        const x = nums[i]
        if (x-1 in counter) {
            res = Math.max(res, counter[x] + counter[x-1])
        }
        if (x+1 in counter) {
            res = Math.max(res, counter[x] + counter[x+1])
        }
    }
    return res
};