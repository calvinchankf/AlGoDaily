/*
    naive approach

    Time    O(N^2)
    Space   O(N)
    72 ms, faster than 93.96%
*/
var getRow = function(rowIndex) {
    if (rowIndex == 0) {
        return [1]
    }
    let row = [1,1]
    for (let i = 2; i <= rowIndex; i++) {
        const newRow = Array(i+1).fill(1)
        for (let j = 1; j < row.length; j++) {
            newRow[j] = row[j-1] + row[j]
        }
        row = newRow
    }
    return row
};
