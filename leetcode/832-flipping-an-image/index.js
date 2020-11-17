/*
    0th: brute force

    Time		O(N)
	Space		O(N)
	92 ms, faster than 26.96%
*/
var flipAndInvertImage = function(A) {
    const R = A.length
    const C = A[0].length
    for (let i = 0; i < R; i++) {
        const r = A[i].reverse()
        const newRow = Array(C).fill(0)
        for (let j = 0; j < C; j++) {
            if (r[j] == 0) {
                newRow[j] = 1
            }
        }
        A[i] = newRow
    }
    return A
};