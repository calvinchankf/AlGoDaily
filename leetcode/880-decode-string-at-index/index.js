/*
    2nd: math, learned from the solution
    - when we go back, we reduce the size
        - one by one if the last character is an alphabet
        - /= if the last character is a digit
    
    case1: S = leet2code, K = 10
    - total size = 12
    - remove one by one until size = k = 10

    case2: S = leet2code, K = 2
    - total size = 12
    - remove one by one until size = 8. since the last character is a digit, we divide the size by the digit, then we get size = 4
    - when size = 4, the last character is 't', so we keep subtracting
    - subtract until size = k = 2, we done

    ref:
    - https://leetcode.com/problems/decoded-string-at-index/solution/

    Time    O(n)
    Space   O(1)
    20 ms, faster than 44.68%
*/
var decodeAtIndex = function(S, K) {
    let totalLength = 0
    for (let c of S) {
        if (isDigit(c)) {
            totalLength *= parseInt(c)
        } else {
            totalLength += 1
        }
    }
    for (let i = S.length-1; i >= 0; i--) {
        K %= totalLength
        if (K == 0 && isDigit(S[i]) == false) {
            return S[i]
        }
        if (isDigit(S[i])) {
            totalLength = Math.round(totalLength / parseInt(S[i]))
        } else {
            totalLength -= 1
        }
    }
};
const isDigit = (c) => {
    const x = parseInt(c)
    return x >= 0 && x <= 9
}