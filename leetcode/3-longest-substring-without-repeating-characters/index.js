/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
    const ht = {}
    let j = 0
    let res = 0
    for (let i = 0; i < s.length; i++) {
        const c = s[i]
        if (c in ht === false) {
            ht[c] = 0
        }
        ht[c] += 1
        while (ht[c] > 1) {
            const left = s[j]
            ht[left] -= 1
            if (ht[left] == 0) { // optimization to save storage
				delete ht[left];
            }
            j += 1
        }
        res = Math.max(res, i - j + 1)
    }
    return res
};
