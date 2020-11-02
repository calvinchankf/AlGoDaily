/*
    1st approach: hashtable

	Time	O(n)
	Space	O(n)
	176 ms, faster than 19.58%
*/
var findRepeatedDnaSequences = function(s) {
    const n = s.length
    let window = ''
    const seen = {}
    for (let i = 0; i < n; i++) {
        window += s[i]
        if (i >= 10) {
            window = window.slice(1)
        }
        if (window in seen) {
            seen[window] += 1
        } else {
            seen[window] = 1
        }
    }
    const res = []
    for (let key in seen) {
        if (seen[key] > 1) {
            res.push(key)
        }
    }
    return res
};