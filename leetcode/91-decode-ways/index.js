/*
    2nd approach: brute force with memorization
    1. go through all the paths
    2. for each path, when it comes to an end return 1
    3. memorize the substrings and their "ways" to avoid duplicate calculations
    3. the result is the sum of recursion
    Time    O(n) the length of the string, we use map to avoid duplicate substring
    Space   O(h) the height of recursion
    16 ms, faster than 89.55%
*/
var numDecodings = function(s) {
    return dfs(s, {})
};
const dfs = (s, ht) => {
    if (s.length === 0) {
        return 1
    }
    if (s in ht) {
        return ht[s]
    }
    let total = 0
    const a = s.slice(0, 1)
    const b = s.slice(0, 2)
    if (parseInt(a) >= 1 && parseInt(a) <= 9) {
        const remain = s.slice(1, s.length)
        total += dfs(remain, ht)
    }
    if (parseInt(b) >= 10 && parseInt(b) <= 26) {
        const remain = s.slice(2, s.length)
        total += dfs(remain, ht)
    }
    ht[s] = total
    return total
}