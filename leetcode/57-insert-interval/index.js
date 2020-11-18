/*
    1st: merge intervals

    Time    O(NlogN)
    Space   O(N)
    96 ms, faster than 40.35%
*/
var insert = function(intervals, newInterval) {
    intervals.push(newInterval)
    
    intervals = intervals.sort((a, b) => {
        if (a[0] == b[0]) {
            return a[1] - b[1]
        }
        return a[0] - b[0]
    })
    
    const res = [intervals[0]]
    for (let i = 0; i < intervals.length; i++) {
        const n = res.length
        const [s, e] = intervals[i]
        if (s <= res[n-1][1]) {
            res[n-1][1] = Math.max(res[n-1][1], e)
        } else {
            res.push(intervals[i])
        }
    }
    return res
};