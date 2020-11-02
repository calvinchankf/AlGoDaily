/*
    1st approach: sort
    - similar to lc56, 452, 616, 758
    1. sort the intervals by start time
    2. iterate the intervals and compare the cur interval start time with the last interval end time

    Time    O(nlogn)
    Space   O(n)
    88 ms, faster than 24.16%
    20apr2019
*/

/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function (intervals) {
	if (intervals.length == 0) {
        return []
    }
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
