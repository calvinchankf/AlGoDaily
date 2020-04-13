/**
 * 1st approach: stack

	Time	O(S+T)
	Space	O(S+T)
    56 ms, faster than 81.69%
    
 * @param {string} S
 * @param {string} T
 * @return {boolean}
 */
var backspaceCompare = function(S, T) {
    let s = ''
    for (let c of S) {
        if (c === '#') {
            if (s.length > 0) {
                s = s.substring(0, s.length - 1)
            }
        } else {
            s += c
        }
    }
    let t = ''
    for (let c of T) {
        if (c === '#') {
            if (t.length > 0) {
                t = t.substring(0, t.length - 1)
            }
        } else {
            t += c   
        }
    }
    return s == t
};