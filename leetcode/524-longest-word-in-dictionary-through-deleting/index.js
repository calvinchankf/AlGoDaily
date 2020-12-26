/*
    1st approach: string checking
    - check if each of the words can be formed by deleting characters from s
    - there are 2 conditions to update the intermediate result
        1. length of this word is longer than the intermediate result
        2. this word is lexicologically lower than intermediate result if both lengths are the same
    
    Time    O(nk) n: number of the words in dictionary, k: length of the s
    Space   O(k) at worst case it would be s
    96 ms, faster than 67.50% 
*/
var findLongestWord = function(s, d) {
    let res = ''
    for (let w of d) {
        let i = 0 // s
        let j = 0 // w
        while (i < s.length && j < w.length) {
            if (s[i] == w[j]) {
                i += 1
                j += 1
            } else {
                i += 1
            }
        }
        if (j == w.length) {
            if (w.length > res.length) {
                res = w
            } else if (w.length == res.length && w < res) {
                res = w
            }
        }
    }
    return res
};