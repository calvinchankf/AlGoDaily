/*
    2nd approach: sliding window
    - similar to lc438, 567
    - check if each substring is an anagram but dont use slice in every iteration

    Time    O(n*m)
    Space   O(m)
    208 ms, faster than 37.02% 
*/
/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function(s, p) {
    const m = p.length
    const target = Array(26).fill(0)
    for (let c of p) {
        const idx = c.charCodeAt() - "a".charCodeAt()
        target[idx] += 1
    }
    
    const res = []
    const cur = Array(26).fill(0)
    for (let i = 0; i < s.length; i++) {
        const c = s[i]
        const idx = c.charCodeAt() - "a".charCodeAt()
        cur[idx] += 1
        if (i >= m) {
            const left = s[i-m]
            const idx = left.charCodeAt() - "a".charCodeAt()
            cur[idx] -= 1
        }
        if (ifAhasB(cur, target)) {
            res.push(i-m+1)
        }
    }
    return res
};

const ifAhasB = (cur, target) => {
    for (let i = 0; i < 26; i++) {
        if (cur[i] != target[i]) {
            return false
        }
    }
    return true
}