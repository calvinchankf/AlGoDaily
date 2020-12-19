/*
    1st approach: expand from center like lc5

    Time    O(N^2)
    Space   O(1)
    88 ms, faster than 77.71%
*/
var countSubstrings = function(s) {
    let res = 0
    for (let i = 0; i < s.length; i++) {
        res += explore(s, i-1, i)
        res += explore(s, i, i)
    }
    return res
};

const explore = (s, i ,j) => {
    if (i < 0 || s[i] != s[j]) {
        return 0
    }
    let count = 1
    while (i-1 >= 0 && j+1 < s.length && s[i-1] == s[j+1]) {
        count += 1
        i -= 1
        j += 1
    }
    return count
}