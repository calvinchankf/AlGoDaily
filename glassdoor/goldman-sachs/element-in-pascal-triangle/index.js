/*
    https://leetcode.com/discuss/interview-question/374394/Goldman-Sachs-or-Coderpad-or-Experienced-Hire-or-2019

    Given a R and C, find the element at corresponding location in a pascal's triangle.
    [
        [1],
        [1,1],
        [1,2,1],
        [1,3,3,1],
        [1,4,6,4,1],
        [1,5,10,10,5,1],
        [1,6,15,20,15,6,1],
        [1,7,21,35,35,21,7,1],
        [1,8,28,56,70,56,28,8,1],
        [1,9,36,84,126,126,84,36,9,1]
    ]
                ^ R = 9, C = 3
*/
var elementInPascalTriangle = function(R, C) {
    let row = [1]
    for (let i = 1; i <= R; i++) {
        const _row = Array(i+1).fill(1)
        for (let j = 1; j < row.length; j++) {
            _row[j] = row[j] + row[j-1]
        }
        row = _row
    }
    return row[C]
};

console.log(elementInPascalTriangle(9, 3))