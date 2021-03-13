/*
    1st approach: sort + hashtable
    - sort the scores from high to low so the higher scores come first
    - use hashtable to put the scores to corresponding sids(student id)
    - construct result by iterating the sid from ascendingly

    Time    O(NlogN)
    Space   O(N)
    84 ms, faster than 84.04%
*/
var highFive = function(items) {
    const ht = {}
    for (let [sid, score] of items) {
        if (sid in ht == false) {
            ht[sid] = []
        }
        ht[sid].push(score)
    }
    const res = []
    for (let key in ht) {
        ht[key].sort((a, b) => b - a)
        const topFive = ht[key].slice(0, 5)
        const count = topFive.length
        const total = topFive.reduce((_total, num) => _total + num, 0)
        res.push([key, Math.floor(total / count)])
    }
    res.sort((a, b) => a[0] - b[0])
    return res
};