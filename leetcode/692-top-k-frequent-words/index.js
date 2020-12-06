/*
    1st approach
	1. count num: freq into a hashtable
	2. sort the hashtable keys
	3. put the hashtable key&value into a bucket with freq as an index
	4. the first k elements are the top k elements in the bucket

	Time	O(nlogn * klogk)
	Space	O(n)
	96 ms, faster than 59.15%
*/
var topKFrequent = function (words, k) {
	const counter = {}
    for (let w of words) {
        if ((w in counter) === false) {
            counter[w] = 0
        }
        counter[w] += 1
    }
    const freqs = {}
    let maxFreq = 0
    for (let key in counter) {
        const count = counter[key]
        maxFreq = Math.max(maxFreq, count)
        if ((count in freqs) === false) {
            freqs[count] = []
        }
        freqs[count].push(key)
    }
    const res = []
    for (let f = maxFreq; f >= 0; f--) {
        if (f in freqs) {
            const words = freqs[f].sort()
            for (let w of words) {
                res.push(w)
                if (res.length == k) { return res }
            }
        }
    }
    return res
};
