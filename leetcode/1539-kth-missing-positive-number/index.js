/*
    1st: hashtable

    Time    O(N + K)
    Space   O(N + K)
*/
var findKthPositive = function(arr, k) {
    let res = []
    const hs = new Set(arr)
    let i = 1
    while (res.length < k) {
        if (!hs.has(i)) {
            res.push(i)
        }
        i += 1
    }
    return res[k-1]
};