/*
    1st approach
	- hashtable
	1. in each iteration, transform the string into a key(diff between characters)
	2. keep in mind that, az, ba are in the same group

	Time		O(N)
	Space		O(N)
	84 ms, faster than 78.20% 
*/
var groupStrings = function(strings) {
    const ht = {}
    for (let s of strings) {
        const k = generateKey(s)
        if (k in ht == false) {
            ht[k] = []
        }
        ht[k].push(s)
    }
    const res = []
    for (let k in ht) {
        res.push(ht[k])
    }
    return res
};

const generateKey = (s) => {
    let diffs = []
    for (let i = 1; i < s.length; i++) {
        let diff = s[i].charCodeAt() - s[i-1].charCodeAt()
        diff = (diff + 26) % 26
        diffs.push(diff)
    }
    return diffs.join(',')
}