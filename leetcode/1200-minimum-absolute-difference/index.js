/*
    1st: sort

    Time    O(NlogN)
    Space   O(N)
    164 ms, faster than 68.86%
*/
var minimumAbsDifference = function(arr) {
    arr.sort((a, b) => a - b)
    let res = []
    let gDiff = 2**32
    for (let i = 1; i < arr.length; i++) {
        const diff = arr[i] - arr[i-1]
        if (diff < gDiff) {
            res = [ [arr[i-1], arr[i]] ]
            gDiff = diff
        } else if (diff == gDiff) {
            res.push([arr[i-1], arr[i]])
        }
    }
    return res
};