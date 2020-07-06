/*
    1st: brute force

    Time    O(N^2)
    Space   O(1)
    88 ms, faster than 100.00%
*/

/**
 * @param {number[]} prices
 * @return {number[]}
 */
var finalPrices = function (prices) {
	const res = [];
	for (let i = 0; i < prices.length; i++) {
		let target = null;
		for (let j = i + 1; j < prices.length; j++) {
			if (prices[j] <= prices[i]) {
				target = j;
				break;
			}
		}
		if (target == null) {
			res.push(prices[i]);
		} else {
			res.push(prices[i] - prices[target]);
		}
	}
	return res;
};

/*
    2nd: stack
    - the array stores numbers in an increasing manner
    - while a new item is <= stack[-1], pop the stack and update the result at prices[stack[-1]]

    Time    O(N)
    Space   O(N)
    92 ms, faster than 100.00% <- What, why it is slower than 1st approach???
*/
/**
 * @param {number[]} prices
 * @return {number[]}
 */
var finalPrices = function (prices) {
	const res = [...prices];
	const stack = [];
	for (let i = 0; i < prices.length; i++) {
		const p = prices[i];
		if (stack.length == 0) {
			stack.push(i);
		} else {
			while (prices[stack[stack.length - 1]] >= prices[i]) {
				const idx = stack.pop();
				res[idx] = prices[idx] - prices[i];
			}
			stack.push(i);
		}
	}
	return res;
};
