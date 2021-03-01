/*
    naive approach

    Time    O(N^2)
    Space   O(N)
    72 ms, faster than 93.96%
*/
var getRow = function(rowIndex) {
    let res = []
    for (let i = 1; i <= rowIndex + 1; i++) {
        const row = Array(i).fill(1)
        for (let j = 1; j < i-1; j++) {
            row[j] = res[j-1] + res[j]
        }
        res = row
    }
    return res
};
