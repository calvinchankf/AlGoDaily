/*
    1st: hashtable
    - count the number fo each character
    - subtract the source from target, to get the diff

    Time    O(S+T)
    Space   O(S+T)
    104 ms, faster than 84.16%
*/
var minSteps = function(s, t) {
    const counterA = Array(26).fill(0)
    const counterB = Array(26).fill(0)
    for (let c of s) {
        const i = c.charCodeAt() - 'a'.charCodeAt()
        counterA[i] += 1
    }
    for (let c of t) {
        const i = c.charCodeAt() - 'a'.charCodeAt()
        counterB[i] += 1
    }
    let diff = 0
    for (let i = 0; i < 26; i++) {
        diff += Math.abs(counterA[i] - counterB[i])
    }
    return diff/2
};