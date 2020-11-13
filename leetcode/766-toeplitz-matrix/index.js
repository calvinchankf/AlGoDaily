/*
    0th: iterate from the top & left edges

    Time    O(RC)
    Space   O(RC)
    96 ms, faster than 44.63%
*/
var isToeplitzMatrix = function(m) {
    if (m.length == 0 || m[0].length == 0) {
        return true
    }
    const R = m.length
    const C = m[0].length
    const starts = []
    for (let i = 0; i < R; i++) {
        starts.push([i, 0])
    }
    for (let j = 0; j < C; j++) {
        starts.push([0, j])
    }
    for (let [i, j] of starts) {
        let _i = i
        let _j = j
        while (_i+1 < R && _j+1 < C) {
            if (m[_i][_j] != m[_i+1][_j+1]) {
                return false
            }
            _i += 1
            _j += 1
        }
    }
    return true
};