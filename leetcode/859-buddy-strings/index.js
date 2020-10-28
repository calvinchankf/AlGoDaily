/*
    2nd: find the indices where A[i] != B[i]
    - there are 2 cases to return true
        1. A[1] + A[0] == B[0] + B[1]
        2. no indices need to swap and the count[A[i]] >= 2, e.g. A = 'aa', B = 'aa' <- we can swap the indices of A to get the same string 'aa'
    - otherwise, return false
*/
var buddyStrings = function(A, B) {
    if (A.length !== B.length) {
        return false
    }
    const n = A.length
    let a = ''
    let b = ''
    const ht = {}
    let maxFreq = 0
    for (let i = 0; i < n; i++) {
        if (A[i] != B[i]) {
            a += A[i]
            b += B[i]
        }
        if (A[i] in ht) {
            ht[A[i]] += 1
        } else {
            ht[A[i]] = 1
        }
        maxFreq = Math.max(maxFreq, ht[A[i]])
    }
    if (a.length == 2) {
        return a[1] + a[0] == b
    } else if (a.length == 0 && maxFreq >= 2) {
        return true
    }
    return false
};