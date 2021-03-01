/**
 * @param {number[]} prices
 * @return {number}
 * 
 * 
 *  1st approach: classic dp problem
    - keep the dip when we traverse the list
    - when there is a new peak and the current diff is larger than the previous diff, update the diff
    
 * 52 ms, faster than 95.20%
 */
var maxProfit = function (prices) {
    let res = 0
    let dip = 2**32
    for (let p of prices) {
        dip = Math.min(dip, p)
        res = Math.max(res, p - dip)
    }
    return res
};