/*
    1st approach: math
    - for each number, see if it is a self dividing number by using %

    Time    O(NlogX) X = every item
    Space   O(N)
    84 ms, faster than 67.31%
*/
var selfDividingNumbers = function(left, right) {
    const res = []
    for (let i = left; i <= right; i++) {
        const s = `${i}`
        let isDivisible = true
        for (let c of s) {
            const j = parseInt(c)
            if (i%j != 0) {
                isDivisible = false
                break
            }
        }
        if (isDivisible) {
            res.push(i)
        }
    }
    return res
};