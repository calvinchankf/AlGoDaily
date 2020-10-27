/*
    2nd: array interation
    - same logic as 1st approach

    Time    O(N)
    Space   O(1)
    84 ms, faster than 74.01%
*/
var maxPower = function(s) {
    let res = 1
    let count = 1
    for (let i = 1; i < s.length; i++) {
        if (s[i] == s[i-1]) {
            count += 1
        } else {
            count = 1
        }
        res = Math.max(res, count)
    }
    return res
};