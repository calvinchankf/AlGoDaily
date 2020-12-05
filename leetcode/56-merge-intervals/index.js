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
    intervals.sort((a, b) => a[0] - b[0])
    const res = []
    for (let [s, e] of intervals) {
        if (res.length > 0 && s <= res[res.length-1][1]) {
            res[res.length-1][1] = Math.max(res[res.length-1][1], e)
        } else {
            res.push([s, e])
        }
    }
    return res
};
