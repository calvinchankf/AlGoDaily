/*
    1st approach: hashtable

    Time    O(s+t)
    Space   O(52) -> O(1)
    88 ms, faster than 86.74%
*/
var isAnagram = function(s, t) {
    const a = countFreq(s)
    const b = countFreq(t)
    for (let i = 0; i < 26; i++) {
        if (a[i] != b[i]) {
            return false
        }
    }
    return true
};

const countFreq = (s) => {
    const counter = Array(26).fill(0)
    for (let c of s) {
        const i = c.charCodeAt(0) - 'a'.charCodeAt(0)
        counter[i] += 1
    }
    return counter
}