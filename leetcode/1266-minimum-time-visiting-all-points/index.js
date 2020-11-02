/*
    1st: math

    Time    O(N)
    Space   O(1)
    80 ms, faster than 73.71%
*/
var minTimeToVisitAllPoints = function(points) {
    const n = points.length
    let res = 0
    for (let i = 1; i < n; i++) {
        const [x1, y1] = points[i-1]
        const [x2, y2] = points[i]
        const d1 = Math.abs(x1 - x2)
        const d2 = Math.abs(y1 - y2)
        const diff = Math.min(d1, d2)
        const d = diff + Math.abs(diff - d1) + Math.abs(diff - d2)
        res += d
    }
    return res
};