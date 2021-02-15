/*
    1st: math
    - diagonal = i+j, group them and put them into the result

    Time    O(RC)
    Space   O(RC)
    340 ms, faster than 73.42%
*/
var findDiagonalOrder = function(nums) {
    const ht = {}
    const R = nums.length
    let maxKey = 0
    for (let i = 0; i < R; i++) {
        for (let j = 0; j < nums[i].length; j++) {
            const key = i+j
            if (key in ht === false) {
                ht[key] = []
            }
            ht[key].push(nums[i][j])
            maxKey = Math.max(maxKey, key)
        }
    }
    let res = []
    for (let i = 0; i <= maxKey; i++) {
        if (i in ht) {
            // ht[i].reverse()
            // res = res.concat(ht[i]) // array.concat is slow and gets LTE
            const n = ht[i].length
            for (let j = n-1; j >= 0 ; j--) {
                res.push(ht[i][j])
            }
        }
    }
    return res
};