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
    items.sort((a, b) => b[1] - a[1])
    const counter = {}
    for (let [sid, score] of items) {
        if (sid in counter === false) {
            counter[sid] = []
        }
        if (counter[sid].length < 5) {
            counter[sid].push(score)
        }
    }
    const res = []
    for (let sid in counter) {
        const n = Math.min(counter[sid].length, 5)
        const scores = counter[sid]
        const average = Math.floor(sum(scores) / n)
        res.push([sid, average])
    }
    res.sort((a, b) => a[0] - b[0])
    return res
};

const sum = (nums) => {
    let total = 0
    nums.forEach(x => total += x)
    return total
}