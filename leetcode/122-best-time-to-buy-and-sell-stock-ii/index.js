/*
    1st: array

    Time     O(N)
    Space    O(1)
    84 ms, faster than 50.20%
*/
var maxProfit = function (prices) {
	let res = 0
    for (let i = 1; i < prices.length; i++) {
        if (prices[i] > prices[i-1]) {
            res += prices[i] - prices[i-1]
        }
    }
    return res
};
