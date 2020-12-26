/**
 *  3rd attempt: shorten the 2nd approach by just using tuples as keys

    Time O(nk) n:number of words, k:length of charactors
    Space O(nk)
    136ms beats 70.28%

 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const ht = {}
    for (let s of strs) {
        const key = getSignature(s)
        if (key in ht === false) {
            ht[key] = []
        }
        ht[key].push(s)
    }
    const res = []
    for (let key in ht) {
        res.push(ht[key])
    }
    return res
};

const getSignature = (s) => {
    const counter = Array(26).fill(0)
    for (let c of s) {
        const i = c.charCodeAt() - 'a'.charCodeAt()
        counter[i] += 1
    }
    return counter.join(',')
}
