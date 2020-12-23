/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
    const counter = {}
    let j = 0
    let res = 0
    for (let i = 0; i < s.length; i++) {
        const c = s[i]
        if (c in counter === false) {
            counter[c] = 0
        }
        counter[c] += 1
        while (counter[c] > 1) {
            const left = s[j]
            j += 1
            counter[left] -= 1
            if (counter[left] === 0) {
                delete counter[left]
            }
        }
        res = Math.max(res, i - j + 1)
    }
    return res
};
