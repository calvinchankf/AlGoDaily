/**
 * Definition for read4()
 * 
 * @param {character[]} buf4 Destination buffer
 * @return {number} The number of actual characters read
 * read4 = function(buf4) {
 *     ...
 * };
 */


/*
    1st: array
    - bad description
    - in short, lets say we want to read the first 5 characters from "leetcode" using read4()

    1. when we call read4(interanlBuffer), interanlBuffer = [l, e, e, t]
    so then we push all 4 items from interanlBuffer to our result by buf.push()

    2. when we call read4(interanlBuffer), interanlBuffer = [c, o, d, e]
    since we only need 1 more character, we only have to push the "c" into buff

    As a result,
    interanlBuffer = [o, d, e]
    buff = [l, e, e, t, c]

    Time    O(N)
    Space   O(4)
    80 ms, faster than 45.87%
*/
var solution = function(read4) {
    /**
     * @param {character[]} buf Destination buffer
     * @param {number} n Number of characters to read
     * @return {number} The number of actual characters read
     */
    return function(buf, n) {
        
        let cands = []
        let total = 0
        
        while (total < n) {
            
            if (cands.length == 0) {
                const count = read4(cands)
                if (count == 0) {
                    break
                }
            }
            
            while (cands.length > 0 && total < n) {
                buf.push(cands.shift())
                total += 1
            }
        }
        return total
    };
};