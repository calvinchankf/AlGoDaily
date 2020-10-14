/*
    2nd: interval problem
    - similar to lc56, 252, 253, 435, 452, 646

    Time    O(NlogN)
    Space   O(N)
*/
var findMinArrowShots = function(points) {
    if (points.length == 0) {
        return 0
    }
    points.sort((a, b) => {
        if (a[0] === b[0]) {
            return a[1] - b[1]
        }
        return a[0] - b[0]
    })
    const arrows = [points[0][1]]
    for (let i = 1; i < points.length; i++) {
        const [s, e] = points[i]
        const n = arrows.length
        if (s > arrows[n-1]) {
            arrows.push(e)
        } else {
            arrows[n-1] = Math.min(arrows[n-1], e)
        }
    }
    return arrows.length
};