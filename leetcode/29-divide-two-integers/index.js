/*
    3rd: binary search
    - the best way for interviews to tackle this problem

    Time    O(logN)
    Space   O(1)
    96 ms, faster than 73.76%
*/
var divide = function(dividend, divisor) {
    const sign = dividend * divisor > 0 ? 1 : -1
    dividend = Math.abs(dividend)
    divisor = Math.abs(divisor)
    const res = bsearch(dividend, divisor) * sign
    if (res < -(2**31) || res > 2**31-1) {
        return 2**31 - 1
    }
    return res
};

const bsearch = (dividend, divisor) => {
    let left = 1
    let right = dividend
    while (left <= right) {
        const mid = Math.floor((left + right) / 2)
        if (dividend < mid * divisor) {
            right = mid - 1
        } else if (dividend > mid * divisor) {
            left = mid + 1
        } else {
            return mid
        }
    }
    return right
}