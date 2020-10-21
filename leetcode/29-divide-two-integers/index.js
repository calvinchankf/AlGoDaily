/*
    3rd: binary search
    - the best way for interviews to tackle this problem

    Time    O(logN)
    Space   O(1)
    96 ms, faster than 73.76%
*/
var divide = function(dividend, divisor) {
    let sign = 1
    if ((dividend < 0 && divisor > 0) || (dividend > 0 && divisor < 0)) {
        sign = -1
    }
    dividend = Math.abs(dividend)
    divisor = Math.abs(divisor)
    let left = -(2**31)
    let right = 2**31
    let res = null
    while (left <= right) {
        const mid = Math.floor((left + right) / 2)
        if (dividend < mid * divisor) {
            right = mid - 1
        } else if (dividend > mid * divisor) {
            left = mid + 1
        } else {    
            res = mid * sign
            break
        }
    }
    if (res == null) {
        res = right * sign
    }
    if (res < -(2**31)) {
        return -(2**31)
    } else if (res > (2**31)-1) {
        return (2**31)-1
    }
    return res
};