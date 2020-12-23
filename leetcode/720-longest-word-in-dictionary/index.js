/*
    1st: sort + hashtable
    - sort the array
    - if the current word is a single character, put that in hashset
    - if the prefix of current word is in the hashset, put that in hashset
    - the longest key in hashset is the result

    Time    O(NlogN)
    Space   O(N)
    84 ms, faster than 97.21%
*/
var longestWord = function(words) {
    const hs = new Set()
    words.sort((a, b) => a.length - b.length)
    for (let w of words) {
        if (w.length == 1) {
            hs.add(w)
        } else {
            const prefix = w.slice(0, w.length-1)
            if (hs.has(prefix)) {
                hs.add(w)
            }
        }
    }
    let res = ''
    for (let w of hs) {
        if (w.length > res.length) {
            res = w
        } else if (w.length == res.length && w < res) {
            res = w
        }
    }
    return res
};