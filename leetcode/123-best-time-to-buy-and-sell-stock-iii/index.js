/*
    2nd: dynamic programming
    - reuse lc121
    - profit from the front[i] + profit frome the back[i]
*/
var maxProfit = function(prices) {
    const n = prices.length
    
    const forward = Array(n).fill(0)
    let dip = 2**32
    let maxDiff = 0
    for (let i = 0; i < n; i++) {
        dip = Math.min(dip, prices[i])
        maxDiff = Math.max(maxDiff, prices[i] - dip)
        forward[i] = maxDiff
    }
    
    const backward = Array(n).fill(0)
    let peak = 0
    maxDiff = 0
    for (let i = n-1; i >= 0; i--) {
        peak = Math.max(peak, prices[i])
        maxDiff = Math.max(maxDiff, peak - prices[i])
        backward[i] = maxDiff
    }
    
    let res = 0
    for (let i = 0; i < n; i++) {
        const p = forward[i] + backward[i]
        res = Math.max(res, p)
    }
    return res
};