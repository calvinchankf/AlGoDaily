/*
    naive approach

    Time    O(N^2)
    Space   O(N)
    72 ms, faster than 93.96%
*/
var getRow = function(rowIndex) {
    let row = [1]
    for (let i = 1; i <= rowIndex; i++) {
        const _row = Array(i+1).fill(1)
        for (let j = 1; j < row.length; j++) {
            _row[j] = row[j] + row[j-1]
        }
        row = _row
    }
    return row
};
