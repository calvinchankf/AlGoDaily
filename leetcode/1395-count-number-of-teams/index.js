/*
    1st: array
    - for each number
        - count the number of items less then itself from the left
        - count the number of items bigger then itself from the right
    - same idea vice versa
    - e.g. 
            [1, 2, 3, 4, 5, 6]
                   ^
            _____    ________
              2          3
    we can form 2*3 = 6 increasing sequences
    [1,3,4]
    [1,3,5]
    [1,3,6]
    [2,3,4]
    [2,3,5]
    [2,3,6]

    Time    O(n^2)
    Space   O(1)
    76 ms, faster than 96.64%
*/
var numTeams = function(rating) {
    const n = rating.length
    let res = 0
    for (let j = 0; j < n; j++) {
        let left_smaller = 0
        let left_larger = 0
        for (let i = j - 1; i >= 0; i--) {
            if (rating[i] < rating[j]) {
                left_smaller += 1
            }
            if (rating[i] > rating[j]) {
                left_larger += 1
            }
        }
        let right_smaller = 0
        let right_larger = 0
        for (let k = j + 1; k < n; k++) {
            if (rating[j] < rating[k]) {
                right_larger += 1
            }
            if (rating[j] > rating[k]) {
                right_smaller += 1
            }
        }
        const a = left_smaller * right_larger
        const b = left_larger * right_smaller
        res += a + b
    }
    return res
};