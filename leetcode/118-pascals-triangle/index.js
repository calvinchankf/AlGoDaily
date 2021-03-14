/*
    naive approach

    Time    O(n!)
    Space   O(n)
    76 ms, faster than 48.45%
*/
var generate = function(numRows) {
    const res = []
    for (let i = 1; i < numRows + 1; i++) {
        const row = Array(i).fill(1)
        for (let j = 1; j < i-1; j++) {
            row[j] = res[res.length-1][j-1] + res[res.length-1][j]
        }
        res.push(row)
    }
    return res
};
