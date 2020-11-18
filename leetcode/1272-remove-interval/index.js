/*
    1st: brute-force all cases

    Time    O(N) N: number of intervals
    Space   O(N)
    332 ms, faster than 34.48%
*/
var removeInterval = function(intervals, toBeRemoved) {
    const res = []
    for (let [s, e] of intervals) {
        if (e < toBeRemoved[0] || s > toBeRemoved[1]) {
            res.push([s, e])
        } else if (s < toBeRemoved[0] && e > toBeRemoved[1]) {
            res.push([s, toBeRemoved[0]])
            res.push([toBeRemoved[1], e])
        } else if (s < toBeRemoved[0] && e > toBeRemoved[0]) {
            res.push([s, toBeRemoved[0]])
        } else if (s < toBeRemoved[1] && e > toBeRemoved[1]) {
            res.push([toBeRemoved[1], e])
        } 
    }
    return res
};