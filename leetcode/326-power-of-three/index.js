/*
    2nd approach: math
    - divide by 3 until mod != 0

    Time    O(logn)
    Space   O(1) 
    260 ms, faster than 57.80%
*/
var isPowerOfThree = function(n) {
    if (n < 1) {
        return false
    }
    while (n > 1) {
        if (n % 3 != 0) {
            return false
        }
        n /= 3
    }
    return true
};