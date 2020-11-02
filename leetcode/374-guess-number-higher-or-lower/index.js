/** 
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	            -1 if num is lower than the guess number
 *			             1 if num is higher than the guess number
 *                       otherwise return 0
 * var guess = function(num) {}
 */

/*
    binary search

    Time    O(logN)
    Space   O(1)
    80 ms, faster than 36.99%
*/
var guessNumber = function(n) {
    let left = 1
    let right = n
    while (left <= right) {
        const mid = Math.floor((left + right) / 2)
        const gueseRes = guess(mid)
        if (gueseRes == 0) {
            return mid
        } else if (gueseRes == -1) {
            right = mid - 1
        } else {
            left = mid + 1
        }
    }
};