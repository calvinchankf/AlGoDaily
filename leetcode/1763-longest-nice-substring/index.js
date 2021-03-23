
/**
 * @param {string} s
 * @return {string}
 */
var longestNiceSubstring = function(S) {
    const n = S.length
    let s = S.toLowerCase()
    let res = ''
    for (let i = 0; i < n; i++) {
        let cur = ''
        for (let j = i; j < n; j++) {
            cur += S[j]
            const b = check(cur)
            // console.log(b)
            if (b && cur.length > res.length) {
                res = cur
            }
        }
    }
    return res
};

const check = (s) => {
    const upper = Array(26).fill(0)
    const lower = Array(26).fill(0)
    for (let c of s) {
        const i = c.charCodeAt() - 'A'.charCodeAt()
        const j = c.charCodeAt() - 'a'.charCodeAt()
        if (i >= 0 && i < 26) {
            upper[i] += 1
        } else if (j >= 0 && j < 26) {
            lower[j] += 1
        }
    }
    // console.log(s, upper, lower)
    for (let i = 0; i < 26; i++) {
        if (upper[i] > 0 && lower[i] == 0) {
            return false
        }
        if (upper[i] == 0 && lower[i] > 0) {
            return false
        }
    }
    return true
}