/*
    1st: hashtable

    Time    O(S+T)
    Space   O(S)
    120 ms, faster than 52.74%
*/
var findRestaurant = function(list1, list2) {
    const seen = {}
    for (let i = 0; i < list1.length; i++) {
        const w = list1[i]
        seen[w] = i
    }
    let minIndexSum = 2**32
    let res = []
    for (let i = 0; i < list2.length; i++) {
        const w = list2[i]
        if (w in seen) {
            const j = seen[w]
            const k = i + j
            if (k < minIndexSum) {
                minIndexSum = k
                res = [w]
            } else if (k == minIndexSum) {
                res.push(w)
            }
        }
    }
    return res
};