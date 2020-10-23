/*
    binary search
    - similar to lc278

    Time    O(RlogC)
    Space   O(1)
    76 ms, faster than 72.32%
*/
var leftMostColumnWithOne = function(binaryMatrix) {
    const [R, C] = binaryMatrix.dimensions()
    let res = 2**31
    for (let i = 0; i < R; i++) {
        
        let left = 0
        let right = C
        while (left < right) {
            const mid = Math.floor((left + right) / 2)
            if (binaryMatrix.get(i, mid) === 1) {
                right = mid
            } else {
                left = mid + 1
            }
        }
        if (left < C) {
            res = Math.min(res, left)
        }
    }
    if (res == 2**31) {
        return -1
    }
    return res
};