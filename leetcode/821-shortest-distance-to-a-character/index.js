/*
    2nd approach: loop forward and backward

    e.g. S = "loveleetcoded", C = 'e'

    l o v e l e e t c o d e d
    * * * 0 1 0 0 1 2 3 4 0 1 <- nearest diff when we go forward
    3 2 1 0 1 0 0 4 3 2 1 0 * <- nearest diff when we go backward

    3,2,1,0,1,0,0,1,2,2,1,0,1 <- min of forward[i] and backward[i]

    Time    O(3n)
    Space   O(2n)
    92 ms, faster than 63.92%
*/
var shortestToChar = function(s, c) {
    const n = s.length
    const forward = Array(n).fill(2**32)
    const backward = Array(n).fill(2**32)
    let lastC = -(2**32)
    for (let i = 0; i < n; i++) {
        if (s[i] == c) {
            lastC = i
        }
        forward[i] = i - lastC
    }
    lastC = 2**32
    for (let i = n-1; i >= 0; i--) {
        if (s[i] == c) {
            lastC = i
        }
        backward[i] = lastC - i
    }
    const res = Array(n).fill(-1)
    for (let i = 0; i < n; i++) {
        res[i] = Math.min(forward[i], backward[i])
    }
    return res
};