/*
    1st approach: hashtable

    Time    O(S+T)
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


/*
    followup: ascii characters

    Time    O(S+T)
    Space   O(S+T)
    76ms beats 99.62
*/
var isAnagram = function(s, t) {
    const a = countFreq(s)
    const b = countFreq(t)
    const keys = new Set([...Object.keys(a), ...Object.keys(b)])
    for (let c of keys) {
        if (c in a && c in b) {
            if (a[c] != b[c]) {
                return false
            }
        } else if (c in a || c in b) {
            return false
        }
    }
    return true
};

const countFreq = (s) => {
    const counter = {}
    for (let c of s) {
        if ((c in counter) === false) {
            counter[c] = 0
        }
        counter[c] += 1
    }
    return counter
}