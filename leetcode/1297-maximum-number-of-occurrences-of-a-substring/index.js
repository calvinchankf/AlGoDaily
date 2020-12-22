/*
    kinda brute force with a hashtable
    - explore all substrings in O(n * maxSize)
    - use a hashtable as a counter for every substring

    Time    O(NK) K = maxSize
    Space   O(NK)
    1748ms beats 13.63%
*/
var maxFreq = function(s, maxLetters, minSize, maxSize) {
    const counter = {}
    for (let i = 0; i < s.length; i++) {
        
        const seen = new Set() // ensure unique chars <= maxLetters
        let sub = ''
        
        for (let j = 0; j < maxSize; j++) {
            if (i + j >= s.length) {
                break
            }
            const c = s[i+j]
            seen.add(c)
            if (seen.size > maxLetters) {
                break
            }
            sub += c
            if (sub in counter == false) {
                counter[sub] = 0
            }
            counter[sub] += 1
        }
    }
    let res = 0
    for (let sub in counter) {
        const f = counter[sub]
        if (sub.length >= minSize) {
            res = Math.max(res, f)
        }
    }
    return res
};