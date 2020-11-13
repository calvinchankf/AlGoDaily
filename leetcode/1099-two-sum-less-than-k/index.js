/*
    1st approach: sort + 2 pointers
    - 2 sum closest

    Time    O(nlogn)
    Space   O(1)
    32 ms, faster than 67.83%
*/
var twoSumLessThanK = function (A, K) {
	A.sort((a, b) => a - b)
    const n = A.length
    let i = 0
    let j = n - 1
    let res = -1
    while (i < j) {
        const sum = A[i] + A[j]
        if (sum < K) {
            res = Math.max(res, sum)
            i += 1
        } else {
            j -= 1
        }
    }
    return res
};
