/*
    appraoch: sliding window
    - similar to lc438, 567
    - check if each substring is an anagram but dont use slice in every iteration

    Time    O(M + N)
    Space   O(26 + 26)
    88 ms, faster than 92.81%
*/
var checkInclusion = function(s1, s2) {
    const m = s1.length
    const target = Array(26).fill(0)
    for (let c of s1) {
        const idx = c.charCodeAt() - "a".charCodeAt()
        target[idx] += 1
    }
    
    const cur = Array(26).fill(0)
    for (let i = 0; i < s2.length; i++) {
        const c = s2[i]
        const idx = c.charCodeAt() - "a".charCodeAt()
        cur[idx] += 1
        if (i >= m) {
            const left = s2[i-m]
            const idx = left.charCodeAt() - "a".charCodeAt()
            cur[idx] -= 1
        }
        if (ifAhasB(cur, target)) {
            return true 
        }
    }
    return false
};

const ifAhasB = (cur, target) => {
    for (let i = 0; i < 26; i++) {
        if (cur[i] != target[i]) {
            return false
        }
    }
    return true
}