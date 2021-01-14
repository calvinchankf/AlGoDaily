/*
    2nd: optimized the 1st
    - we just store the indcies for non-zero cells

    e.g.
    A = [
        [1,0,0],
        [-1,0,3]
    ]
    B = [
        [7,0,0],
        [0,0,0],
        [0,0,1]
    ]

    htA = {
        0: {0},
        1: {0, 2}
    }
    htB = {
        0: {0}, 
        2: {2}
    }

    Time    O(A + B + ABA) <- it also depends on the number of non-zero
    Space   O(A+B)
    80 ms, faster than 93.97%
*/
var multiply = function(A, B) {
    const htA = {}
    const htB = {}
    const RA = A.length
    const CA = A[0].length
    const RB = B.length
    const CB = B[0].length
    for (let i = 0; i < RA; i++) {
        for (let j = 0; j < CA; j++) {
            if (A[i][j] != 0) {
                if (i in htA === false) {
                    htA[i] = new Set()
                }
                htA[i].add(j)
            }
        }
    }
    for (let i = 0; i < RB; i++) {
        for (let j = 0; j < CB; j++) {
            if (B[i][j] != 0) {
                if (j in htB === false) {
                    htB[j] = new Set()
                }
                htB[j].add(i)
            }
        }
    }
    const res = []
    for (let i = 0; i < RA; i++) {
        res.push(Array(CB).fill(0))
    }
    for (let i in htA) {
        for (let j in htB) {
            for (let key of htA[i]) {
                if (htB[j].has(key)) {
                    const x = parseInt(A[i][key])
                    const y = parseInt(B[key][j])
                    res[i][j] += x * y
                }
            }
        }
    }
    return res
};