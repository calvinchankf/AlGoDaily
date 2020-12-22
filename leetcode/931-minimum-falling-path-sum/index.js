/*
    2nd: dynamic programming, bottom up
    - storing the minimum running sum from bottom of the matrix
    
    Time    O(RC)
    Space   O(RC)
    88 ms, faster than 61.21%
*/
var minFallingPathSum = function(A) {
    const R = A.length
    const C = A[0].length
    for (let i = R - 2; i >= 0; i--) {
        for (let j = 0; j < C; j++) {
            let minFromBottom = 2**32
            if (j-1 >= 0) {
                minFromBottom = Math.min(minFromBottom, A[i+1][j-1])
            }
            minFromBottom = Math.min(minFromBottom, A[i+1][j])
            if (j+1 < C) {
                minFromBottom = Math.min(minFromBottom, A[i+1][j+1])
            }
            A[i][j] += minFromBottom
        }
    }
    return Math.min(...A[0])
};