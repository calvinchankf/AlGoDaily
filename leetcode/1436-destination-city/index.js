/*
    1st: outdegree

    Time    O(N)
    Space   O(N)
    88 ms, faster than 51.44%
*/
var destCity = function(paths) {
    const outdegrees = {}
    for (let [u, v] of paths) {
        if (u in outdegrees == false) {
            outdegrees[u] = 0
        }
        if (v in outdegrees == false) {
            outdegrees[v] = 0
        }
        outdegrees[u] += 1
    }
    for (let key in outdegrees) {
        if (outdegrees[key] == 0) {
            return key
        }
    }
    return ''
};