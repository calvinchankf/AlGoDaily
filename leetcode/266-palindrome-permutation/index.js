/*
    1st approach: hashtable
    - for a valid palindrome, 
    the occurence of a number can only be even or there is only one odd occurence number

    Time    O(n)
    Space   O(n)
    80 ms, faster than 37.27%
*/
var canPermutePalindrome = function(s) {
    const counter = countFreq(s)
    let oddAppeared = false
    for (let key in counter) {
        if (counter[key] % 2 != 0) {
            if (oddAppeared) {
                return false
            }
            oddAppeared = true
        }
    }
    return true
};

const countFreq = (s) => {
    const counter = {}
    for (let c of s) {
        if (c in counter) {
            counter[c] += 1
        } else {
            counter[c] = 1
        }
    }
    return counter
}